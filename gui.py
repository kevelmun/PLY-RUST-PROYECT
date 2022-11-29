from tkinter import *
import tkinter.scrolledtext as st
from main import get_lexer, getTokens, lex_errors
from pyacc import get_yacc, yacc_errors, get_yacc_analisis
#------------------------------- FUNCION PARA EL ANALISIS LEXICO --------------------------------------
lexer_analizer = get_lexer()

def lexer_analisis():
    codigo = inputCode.get("1.0", END)
    outputCode.configure(state='normal')

    # Limpieza de el contenedor outputCode
    outputCode.delete("1.0", END)

    #Aquí se hace el análisis léxico con el código ingresado

    lexer_analizer.lineno = 1

    lexer_analizer.input(codigo)
    outputResults = getTokens(lexer_analizer)    

    #Formacion del string de salida para la pantalla outputCode
    result = ""
    for elem in outputResults:
        result += repr(elem)
        result += '\n'

    # Salida del output
    outputCode.insert("1.0", result)

    if len(lex_errors) > 0:
        errores = '\n'.join(lex_errors) + '\n'
        outputCode.insert("1.0", errores, 'warning')
        lex_errors.clear() 

    outputCode.configure(state='disabled')

#------------------------------- FUNCION PARA EL ANALISIS SINTACTICO --------------------------------------
sintactic_analizer = get_yacc()

def sintactic_analisis():
    codigo = inputCode.get("1.0", END)
    outputCode.configure(state='normal')

    # Limpieza de el contenedor outputCode
    outputCode.delete("1.0", END)
    sintactic_analizer.lineno = 1
    result = get_yacc_analisis(codigo)

    print(yacc_errors)
    # Salida del output
    if len(yacc_errors) > 0:
        errores = '\n'.join(yacc_errors) + '\n'
        
        outputCode.insert("1.0", errores, 'warning')
        yacc_errors.clear() 

    if len(yacc_errors) == 0:
        outputCode.insert("1.0", repr(result))
    
    outputCode.configure(state='disabled')




root = Tk()
root.title("PLY PROYECT")
root.resizable(False, False)
#-------------------------------CREACION FRAME PRINCIPAL--------------------------------------

mainFrame = Frame()
mainFrame.pack()

#-------------------------------CONFIGURACION LOOP DE EJECUCION--------------------------------------


mainFrame.config(bg="#252525")
mainFrame.config(width="1200", height="600")

#-------------------------------HEADER--------------------------------------
Label(mainFrame, text="GRUPO #7").grid(row=0, column=0, padx=10, pady=10, columnspan=60)

#-------------------------------SECCION DE ENTRADA--------------------------------------

Label(mainFrame, text="Escribe tu codigo:", bg="white").grid(row=1, column=0, sticky="w", padx=10, pady=10)
inputCode = st.ScrolledText(mainFrame, width=60, height=12, insertbackground="#149414")
inputCode.grid(row=2, column=0, sticky="w", padx=10, pady=10, columnspan=60)
inputCode.config(background="#000000", fg="#149414")

#------------------------------- SECCION DE RESULTADO --------------------------------------

Label(mainFrame, text="Resultado:", bg="white").grid(row=7, column=0, sticky="w", padx=10, pady=10)
outputCode =  st.ScrolledText(mainFrame, width=60, height=12)
outputCode.grid(row=8, column=0, sticky="w", padx=10, pady=10, columnspan=60)
outputCode.config(background="#000000", fg="#149414")





#------------------------------- SECCION DE OPCIONES --------------------------------------

lexicButton = Button(mainFrame, text="Lexico", command=lexer_analisis).grid(row=9, column=0, sticky="w",padx=10,pady=10)

sintacticButton = Button(mainFrame, text="Sintactico", command=sintactic_analisis ).grid(row=9, column=0, sticky="e", pady=10)

#-------------------------------LOOP DE EJECUCION--------------------------------------
root.mainloop()
