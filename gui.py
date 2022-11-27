from tkinter import *
import tkinter.scrolledtext as st
from main import get_lexer, getTokens, errors
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
inputCode = st.ScrolledText(mainFrame, width=60, height=12)
inputCode.grid(row=2, column=0, sticky="w", padx=10, pady=10, columnspan=60)
inputCode.config(background="#000000", fg="#149414")

#------------------------------- SECCION DE RESULTADO --------------------------------------

Label(mainFrame, text="Resultado:", bg="white").grid(row=7, column=0, sticky="w", padx=10, pady=10)
outputCode =  st.ScrolledText(mainFrame, width=60, height=12)
outputCode.grid(row=8, column=0, sticky="w", padx=10, pady=10, columnspan=60)
outputCode.config(background="#000000", fg="#149414")

#------------------------------- SECCION DE OPCIONES --------------------------------------
lexer_analizer = get_lexer()

def lexer_analisis():
    codigo = inputCode.get("1.0", END)
    outputCode.configure(state='normal')

    # Limpieza de el contenedor output
    outputCode.delete("1.0", END)

    #Aquí se hace el análisis léxico con el código ingresado
    userInput = []
    lexer_analizer.lineno = 1

    lexer_analizer.input(codigo)
    getTokens(lexer_analizer, userInput)    

    result = ""
    for elem in userInput:
        result += repr(elem)
        result += '\n'

    # Salida del output
    outputCode.insert("1.0", result)

    if len(errors) > 0:
        errores = '\n'.join(errors) + '\n'
        outputCode.insert("1.0", errores, 'warning')
        errors.clear() 

    outputCode.configure(state='disabled')


lexicButton = Button(mainFrame, text="Lexico", command=lexer_analisis).grid(row=9, column=0, sticky="w",padx=10,pady=10)

sintacticButton = Button(mainFrame, text="Sintactico" ).grid(row=9, column=0, sticky="e", pady=10)

#-------------------------------LOOP DE EJECUCION--------------------------------------
root.mainloop()
