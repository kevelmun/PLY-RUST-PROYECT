
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDE CADENA CHAR COLON COMMA COMMENT DIVEQUAL DIVIDE DOT EQ EQUALS FLOAT FLOAT_32 FLOAT_64 GE GT HASH INTEGER KW_ABSTRACT KW_AS KW_ASYNC KW_AWAIT KW_BECOME KW_BOOLEAN KW_BOX KW_BREAK KW_CHARACTER KW_CONST KW_CONTINUE KW_CRATE KW_DO KW_DYN KW_ELSE KW_ENUM KW_EXPECT KW_EXTERN KW_FALSE KW_FINAL KW_FN KW_FOR KW_FROM KW_HASHMAP KW_IF KW_IMPL KW_IN KW_INSERT KW_LET KW_LINKEDLIST KW_LOOP KW_MACRO KW_MATCH KW_MOD KW_MOVE KW_MUT KW_NEW KW_OVERRIDE KW_PRINT KW_PRIV KW_PUB KW_PUSH_BACK KW_READ_LINE KW_REF KW_REMOVE KW_RETURN KW_SELFTYPE KW_SELFVALUE KW_STATIC KW_STATICLIFETIME KW_STDIN KW_STRING KW_STRUCT KW_SUPER KW_TRAIT KW_TRUE KW_TRY KW_TYPE KW_TYPEOF KW_UNION KW_UNSAFE KW_UNSIZED KW_USE KW_VIRTUAL KW_WHERE KW_WHILE KW_YIELD LAND LBRACE LBRACKET LE LNOT LOR LPAREN LT MINUS MINUSEQUAL MODULUS MODULUSEQUAL NE ORE OREXE PLUS PLUSEQUAL QMARK QUOTE RBRACE RBRACKET RPAREN SEMI SIG_INT_128 SIG_INT_16 SIG_INT_32 SIG_INT_64 SIG_INT_8 TIMES TIMESEQUAL UNSIG_INT_128 UNSIG_INT_16 UNSIG_INT_32 UNSIG_INT_64 UNSIG_INT_8 VARIABLEmain_rule : father_rule\n    | father_rule main_rulefather_rule : print\n    | dvariable\n    | function\n    | variables\n    | control_str\n    | expression\n    | void\n    | data_str\n    | array\n    | linkedlist_methods\n    | hashmap_methods\n    | initializationexpression : expression PLUS expression\n    | expression MINUS expression\n    | expression TIMES expression\n    | expression DIVIDE expression\n    | LPAREN expression RPAREN\n    | numbernumber : INTEGER\n    | FLOAT\n    | VARIABLEdata_type : UNSIG_INT_8\n                | UNSIG_INT_16\n                | UNSIG_INT_32\n                | UNSIG_INT_64\n                | UNSIG_INT_128\n                | SIG_INT_8\n                | SIG_INT_16\n                | SIG_INT_32\n                | SIG_INT_64\n                | SIG_INT_128\n                | FLOAT_32\n                | FLOAT_64\n                | KW_BOOLEAN\n                | KW_STRINGdata : CADENA\n    | INTEGER\n    | CHAR\n    | FLOAT\n    | KW_FALSE\n    | KW_TRUE\n    | tuplecomparator :\n    | EQ\n    | NE\n    | GE\n    | LE\n    | GT\n    | LTand : VARIABLE LAND VARIABLEconditional : VARIABLE comparator data\n    | and comparator dataor : VARIABLE LOR VARIABLEmdata : data\n    | data COMMA mdataprint : KW_PRINT LPAREN CADENA RPAREN SEMIdvariable : KW_LET VARIABLE SEMIarray : KW_LET VARIABLE EQUALS LBRACKET mdata RBRACKET\n    | LBRACKET mdata RBRACKETvariables : VARIABLE \n    | VARIABLE COMMA variableswhile : KW_WHILE LPAREN VARIABLE tuple : LPAREN mdata RPARENinitialization : let_initialization SEMI \n    | const_initialization SEMI \n    | data_str SEMIlet_initialization : KW_LET VARIABLE EQUALS data\n    | KW_LET VARIABLE COLON data_type EQUALS data\n    | KW_LET KW_MUT VARIABLE EQUALS data\n    | KW_LET KW_MUT VARIABLE COLON data_type EQUALS data\n    | KW_LET VARIABLE EQUALS expression_var\n    | KW_LET VARIABLE COLON data_type EQUALS expression_var\n    | KW_LET KW_MUT VARIABLE EQUALS expression_var\n    | KW_LET KW_MUT VARIABLE COLON data_type EQUALS expression_varconst_initialization : KW_CONST VARIABLE COLON data_type EQUALS dataarguments : void\n    | variablesfunction : KW_FN VARIABLE LPAREN arguments RPAREN LBRACE main_rule RBRACEcontrol_str : for_str\n    | for_str_tagged\n    | if\n    | else\n    | else_if\n    | whilefor_str : KW_FOR VARIABLE KW_IN range LBRACE main_rule RBRACE\n    | KW_FOR VARIABLE KW_IN VARIABLE LBRACE main_rule RBRACEfor_str_tagged : label COLON for_strrange : INTEGER DOT DOT INTEGER\n    | VARIABLE DOT DOT VARIABLElabel : QUOTE VARIABLEdata_str : array\n    | hashmap\n    | linkedlisthashmap : KW_LET VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN\n    | KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN\n    | KW_LET VARIABLE EQUALS KW_HASHMAP COLON COLON KW_FROM LPAREN array RPAREN\n    | KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_FROM LPAREN array RPARENhashmap_methods : VARIABLE hashmap_insert\n    | VARIABLE hashmap_removehashmap_insert : DOT KW_INSERT LPAREN mdata RPAREN SEMIhashmap_remove : DOT KW_REMOVE LPAREN AND data RPAREN SEMIvoid : linkedlist : KW_LET VARIABLE COLON KW_LINKEDLIST LT data_type GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN\n                  | KW_LET KW_MUT VARIABLE COLON KW_LINKEDLIST LT data_type GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPARENlinkedlist : KW_LET VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN\n                  | KW_LET KW_MUT VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPARENlinkedlist_methods : VARIABLE linkedlist_push\n    | VARIABLE linkedlist_removelinkedlist_push : DOT KW_PUSH_BACK LPAREN data RPAREN SEMIlinkedlist_remove : DOT KW_REMOVE LPAREN INTEGER RPAREN SEMIif : KW_IF conditional LBRACE main_rule RBRACEelse : KW_ELSE LBRACE main_rule RBRACEelse_if : KW_ELSE KW_IF conditional LBRACE main_rule RBRACEfunction : KW_FN VARIABLE LPAREN arguments RPAREN MINUS GT data_type LBRACE return RBRACEexpression_var : expression\n                    | VARIABLEreturn : main_rule\n              | main_rule KW_RETURN expression_var SEMI'
    
_lr_action_items = {'KW_PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,15,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,15,-64,-114,15,-58,15,15,-113,-60,15,-115,-111,-112,-102,-88,-87,-103,-80,-96,15,-98,-107,-97,-99,-108,-116,-105,-106,]),'KW_LET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,232,233,239,240,242,248,249,251,253,254,256,264,265,267,275,277,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,17,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,17,-64,-114,17,-58,17,17,-113,-60,17,-115,-111,-112,-102,-88,-87,243,243,-103,-80,-96,243,243,17,-98,-107,-97,-99,-108,-116,-105,-106,]),'KW_FN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,19,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,19,-64,-114,19,-58,19,19,-113,-60,19,-115,-111,-112,-102,-88,-87,-103,-80,-96,19,-98,-107,-97,-99,-108,-116,-105,-106,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,32,34,37,38,39,40,42,43,44,45,46,49,51,52,53,54,55,56,69,70,76,77,78,81,82,83,84,86,87,88,91,92,96,97,100,101,102,104,114,120,143,160,161,163,166,169,181,183,185,188,199,204,207,210,221,222,224,227,229,239,240,242,243,251,253,254,256,264,265,267,268,275,277,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,49,50,-23,58,-81,-82,-83,-84,-85,-86,-20,-94,-95,71,74,-21,-22,79,80,49,49,49,49,-68,-23,90,91,-109,-110,-100,-101,-66,-67,18,74,114,-15,-16,-17,-18,-19,-59,117,-62,-63,91,-61,153,-89,18,158,-64,49,117,-114,18,-58,49,117,18,18,-113,-60,117,18,228,-115,-111,-112,-102,-88,-87,-103,-80,-96,252,18,-98,-107,-97,-99,-108,-116,117,-105,-106,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,25,26,27,28,29,36,37,38,42,43,44,45,46,49,53,54,55,56,58,68,69,70,74,75,76,81,82,83,84,86,87,88,91,92,93,94,95,97,98,101,102,103,105,106,107,108,109,110,111,114,118,120,143,145,147,158,160,161,163,166,169,178,181,183,185,187,188,199,204,210,212,213,214,221,222,224,227,229,235,236,237,239,240,242,251,253,254,256,264,265,267,268,269,273,275,277,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,47,16,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,68,78,-21,-22,16,16,16,16,-68,-23,-109,-110,-100,-101,96,68,-66,-67,-45,-45,16,-15,-16,-17,-18,-19,-59,120,-62,-63,145,146,147,-61,68,-89,16,68,-46,-47,-48,-49,-50,-51,68,-64,68,166,120,68,68,-52,-114,16,-58,166,120,68,16,16,-113,68,-60,120,16,-115,231,232,233,-111,-112,-102,-88,-87,247,248,249,-103,-80,-96,16,-98,-107,-97,-99,-108,-116,16,272,276,-105,-106,]),'LBRACKET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,88,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,232,233,239,240,242,248,249,251,253,254,256,262,264,265,267,275,277,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,29,-15,-16,-17,-18,-19,-59,118,-62,-63,-61,-89,29,-64,-114,29,-58,29,29,-113,-60,29,-115,-111,-112,-102,-88,-87,29,29,-103,-80,-96,29,29,29,-98,-107,-97,118,-99,-108,-116,-105,-106,]),'KW_FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,72,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,32,32,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,32,-64,-114,32,-58,32,32,-113,-60,32,-115,-111,-112,-102,-88,-87,-103,-80,-96,32,-98,-107,-97,-99,-108,-116,-105,-106,]),'KW_IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,35,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[34,34,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,77,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,34,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,34,-64,-114,34,-58,34,34,-113,-60,34,-115,-111,-112,-102,-88,-87,-103,-80,-96,34,-98,-107,-97,-99,-108,-116,-105,-106,]),'KW_ELSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[35,35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,35,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,35,-64,-114,35,-58,35,35,-113,-60,35,-115,-111,-112,-102,-88,-87,-103,-80,-96,35,-98,-107,-97,-99,-108,-116,-105,-106,]),'KW_WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[36,36,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,36,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,36,-64,-114,36,-58,36,36,-113,-60,36,-115,-111,-112,-102,-88,-87,-103,-80,-96,36,-98,-107,-97,-99,-108,-116,-105,-106,]),'INTEGER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,20,21,22,23,24,25,26,27,28,29,37,38,42,43,44,45,46,49,53,54,55,56,68,69,70,74,75,76,81,82,83,84,86,87,88,91,92,97,98,100,101,102,103,105,106,107,108,109,110,111,114,118,120,143,145,146,147,158,160,161,163,166,169,178,181,183,185,187,188,199,204,209,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,268,275,277,],[37,37,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,37,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,62,-21,-22,37,37,37,37,-68,-23,-109,-110,-100,-101,62,-66,-67,-45,-45,37,-15,-16,-17,-18,-19,-59,124,-62,-63,-61,62,155,-89,37,62,-46,-47,-48,-49,-50,-51,62,-64,62,124,124,62,177,62,-52,-114,37,-58,190,124,62,37,37,-113,62,-60,124,37,230,-115,-111,-112,-102,-88,-87,-103,-80,-96,37,-98,-107,-97,-99,-108,-116,37,-105,-106,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,20,21,22,23,24,25,26,27,28,29,37,38,42,43,44,45,46,49,53,54,55,56,68,69,70,74,75,76,81,82,83,84,86,87,88,91,92,97,98,101,102,103,105,106,107,108,109,110,111,114,118,120,143,145,147,158,160,161,163,166,169,178,181,183,185,187,188,199,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,268,275,277,],[38,38,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,38,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,64,-21,-22,38,38,38,38,-68,-23,-109,-110,-100,-101,64,-66,-67,-45,-45,38,-15,-16,-17,-18,-19,-59,125,-62,-63,-61,64,-89,38,64,-46,-47,-48,-49,-50,-51,64,-64,64,125,125,64,64,-52,-114,38,-58,191,125,64,38,38,-113,64,-60,125,38,-115,-111,-112,-102,-88,-87,-103,-80,-96,38,-98,-107,-97,-99,-108,-116,38,-105,-106,]),'KW_CONST':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[39,39,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,39,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,39,-64,-114,39,-58,39,39,-113,-60,39,-115,-111,-112,-102,-88,-87,-103,-80,-96,39,-98,-107,-97,-99,-108,-116,-105,-106,]),'QUOTE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,114,160,161,163,181,183,185,188,204,210,221,222,224,227,229,239,240,242,251,253,254,256,264,265,267,275,277,],[40,40,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-68,-23,-109,-110,-100,-101,-66,-67,40,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,40,-64,-114,40,-58,40,40,-113,-60,40,-115,-111,-112,-102,-88,-87,-103,-80,-96,40,-98,-107,-97,-99,-108,-116,-105,-106,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,41,46,49,53,54,55,56,69,70,81,82,83,84,86,87,91,92,97,101,114,160,163,185,188,210,221,222,224,227,229,239,240,242,253,254,256,264,265,267,275,277,],[-104,0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-2,-68,-23,-109,-110,-100,-101,-66,-67,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,-64,-114,-58,-113,-60,-115,-111,-112,-102,-88,-87,-103,-80,-96,-98,-107,-97,-99,-108,-116,-105,-106,]),'RBRACE':([2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,41,46,49,53,54,55,56,69,70,76,81,82,83,84,86,87,91,92,97,101,102,112,114,156,160,161,163,181,183,185,186,188,204,206,208,210,221,222,224,225,227,229,239,240,242,251,253,254,256,260,261,264,265,267,274,275,277,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-2,-68,-23,-109,-110,-100,-101,-66,-67,-104,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,-104,160,-64,185,-114,-104,-58,-104,-104,-113,210,-60,-104,227,229,-115,-111,-112,-102,240,-88,-87,-103,-80,-96,-104,-98,-107,-97,267,-119,-99,-108,-116,-120,-105,-106,]),'KW_RETURN':([2,3,4,5,6,7,8,9,10,11,12,13,14,18,20,21,22,23,24,25,26,27,28,37,38,41,46,49,53,54,55,56,69,70,81,82,83,84,86,87,91,92,97,101,114,160,163,185,188,210,221,222,224,227,229,239,240,242,251,253,254,256,261,264,265,267,275,277,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-23,-81,-82,-83,-84,-85,-86,-20,-94,-95,-21,-22,-2,-68,-23,-109,-110,-100,-101,-66,-67,-15,-16,-17,-18,-19,-59,-62,-63,-61,-89,-64,-114,-58,-113,-60,-115,-111,-112,-102,-88,-87,-103,-80,-96,-104,-98,-107,-97,268,-99,-108,-116,-105,-106,]),'PLUS':([8,18,26,37,38,48,49,81,82,83,84,86,117,124,125,126,190,191,],[42,-23,-20,-21,-22,42,-23,42,42,42,42,-19,-23,-21,-22,42,-21,-22,]),'MINUS':([8,18,26,37,38,48,49,81,82,83,84,86,117,124,125,126,180,190,191,],[43,-23,-20,-21,-22,43,-23,43,43,43,43,-19,-23,-21,-22,43,205,-21,-22,]),'TIMES':([8,18,26,37,38,48,49,81,82,83,84,86,117,124,125,126,190,191,],[44,-23,-20,-21,-22,44,-23,44,44,44,44,-19,-23,-21,-22,44,-21,-22,]),'DIVIDE':([8,18,26,37,38,48,49,81,82,83,84,86,117,124,125,126,190,191,],[45,-23,-20,-21,-22,45,-23,45,45,45,45,-19,-23,-21,-22,45,-21,-22,]),'SEMI':([10,11,26,27,28,30,31,37,38,49,50,61,62,63,64,65,66,67,81,82,83,84,86,97,116,117,122,123,124,125,126,152,172,173,188,194,195,200,201,203,211,219,220,223,242,253,254,256,264,265,271,275,277,],[46,-93,-20,-94,-95,69,70,-21,-22,-23,87,-38,-39,-40,-41,-42,-43,-44,-15,-16,-17,-18,-19,-61,163,-23,-69,-73,-21,-22,-117,-65,-71,-75,-60,-70,-74,221,222,224,-77,-72,-76,239,-96,-98,-107,-97,-99,-108,274,-105,-106,]),'KW_MUT':([17,],[51,]),'COMMA':([18,60,61,62,63,64,65,66,67,91,124,125,152,190,191,],[52,98,-38,-39,-40,-41,-42,-43,-44,52,-39,-41,-65,-39,-41,]),'DOT':([18,153,155,182,184,],[57,182,184,207,209,]),'RPAREN':([26,37,38,48,49,60,61,62,63,64,65,66,67,81,82,83,84,85,86,91,92,96,97,99,124,125,148,149,150,151,152,176,177,179,188,190,191,202,231,244,245,247,257,258,272,276,],[-20,-21,-22,86,-23,-56,-38,-39,-40,-41,-42,-43,-44,-15,-16,-17,-18,116,-19,-62,-63,-104,-61,152,-21,-22,180,-78,-79,-57,-65,200,201,203,-60,-21,-22,223,242,253,254,256,264,265,275,277,]),'CADENA':([29,47,68,74,75,88,98,103,105,106,107,108,109,110,111,118,120,143,145,147,158,166,169,178,187,199,],[61,85,61,-45,-45,61,61,61,-46,-47,-48,-49,-50,-51,61,61,61,61,61,61,-52,61,61,61,61,61,]),'CHAR':([29,68,74,75,88,98,103,105,106,107,108,109,110,111,118,120,143,145,147,158,166,169,178,187,199,],[63,63,-45,-45,63,63,63,-46,-47,-48,-49,-50,-51,63,63,63,63,63,63,-52,63,63,63,63,63,]),'KW_FALSE':([29,68,74,75,88,98,103,105,106,107,108,109,110,111,118,120,143,145,147,158,166,169,178,187,199,],[65,65,-45,-45,65,65,65,-46,-47,-48,-49,-50,-51,65,65,65,65,65,65,-52,65,65,65,65,65,]),'KW_TRUE':([29,68,74,75,88,98,103,105,106,107,108,109,110,111,118,120,143,145,147,158,166,169,178,187,199,],[66,66,-45,-45,66,66,66,-46,-47,-48,-49,-50,-51,66,66,66,66,66,66,-52,66,66,66,66,66,]),'COLON':([33,50,79,80,90,119,121,165,167,170,171,196,197,246,255,259,266,],[72,89,115,-92,144,165,167,189,192,196,197,216,217,255,263,266,270,]),'LBRACE':([35,61,62,63,64,65,66,67,73,113,129,130,131,132,133,134,135,136,137,138,139,140,141,142,152,153,154,157,159,180,228,230,241,],[76,-38,-39,-40,-41,-42,-43,-44,102,161,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-65,181,183,-53,-54,204,-91,-90,251,]),'EQUALS':([50,90,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,162,175,215,238,252,],[88,143,169,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,187,199,234,250,262,]),'KW_PUSH_BACK':([57,],[93,]),'KW_REMOVE':([57,],[94,]),'KW_INSERT':([57,],[95,]),'RBRACKET':([59,60,61,62,63,64,65,66,67,151,152,164,],[97,-56,-38,-39,-40,-41,-42,-43,-44,-57,-65,188,]),'KW_IN':([71,],[100,]),'LAND':([74,],[104,]),'EQ':([74,75,158,],[105,105,-52,]),'NE':([74,75,158,],[106,106,-52,]),'GE':([74,75,158,],[107,107,-52,]),'LE':([74,75,158,],[108,108,-52,]),'GT':([74,75,129,130,131,132,133,134,135,136,137,138,139,140,141,142,158,193,205,218,],[109,109,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-52,215,226,238,]),'LT':([74,75,127,158,174,],[110,110,168,-52,198,]),'KW_HASHMAP':([88,143,],[119,170,]),'KW_LINKEDLIST':([88,89,143,144,234,250,],[121,127,171,174,246,259,]),'UNSIG_INT_8':([89,115,144,168,198,226,],[129,129,129,129,129,129,]),'UNSIG_INT_16':([89,115,144,168,198,226,],[130,130,130,130,130,130,]),'UNSIG_INT_32':([89,115,144,168,198,226,],[131,131,131,131,131,131,]),'UNSIG_INT_64':([89,115,144,168,198,226,],[132,132,132,132,132,132,]),'UNSIG_INT_128':([89,115,144,168,198,226,],[133,133,133,133,133,133,]),'SIG_INT_8':([89,115,144,168,198,226,],[134,134,134,134,134,134,]),'SIG_INT_16':([89,115,144,168,198,226,],[135,135,135,135,135,135,]),'SIG_INT_32':([89,115,144,168,198,226,],[136,136,136,136,136,136,]),'SIG_INT_64':([89,115,144,168,198,226,],[137,137,137,137,137,137,]),'SIG_INT_128':([89,115,144,168,198,226,],[138,138,138,138,138,138,]),'FLOAT_32':([89,115,144,168,198,226,],[139,139,139,139,139,139,]),'FLOAT_64':([89,115,144,168,198,226,],[140,140,140,140,140,140,]),'KW_BOOLEAN':([89,115,144,168,198,226,],[141,141,141,141,141,141,]),'KW_STRING':([89,115,144,168,198,226,],[142,142,142,142,142,142,]),'AND':([146,],[178,]),'KW_NEW':([189,216,263,270,],[212,235,269,273,]),'KW_FROM':([189,192,216,217,],[213,214,236,237,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main_rule':([0,2,76,102,161,181,183,204,251,],[1,41,112,156,186,206,208,225,261,]),'father_rule':([0,2,76,102,161,181,183,204,251,],[2,2,2,2,2,2,2,2,2,]),'print':([0,2,76,102,161,181,183,204,251,],[3,3,3,3,3,3,3,3,3,]),'dvariable':([0,2,76,102,161,181,183,204,251,],[4,4,4,4,4,4,4,4,4,]),'function':([0,2,76,102,161,181,183,204,251,],[5,5,5,5,5,5,5,5,5,]),'variables':([0,2,52,76,96,102,161,181,183,204,251,],[6,6,92,6,150,6,6,6,6,6,6,]),'control_str':([0,2,76,102,161,181,183,204,251,],[7,7,7,7,7,7,7,7,7,]),'expression':([0,2,16,42,43,44,45,76,88,102,120,143,161,166,169,181,183,199,204,251,268,],[8,8,48,81,82,83,84,8,126,8,48,126,8,48,126,8,8,126,8,8,126,]),'void':([0,2,76,96,102,161,181,183,204,251,],[9,9,9,149,9,9,9,9,9,9,]),'data_str':([0,2,76,102,161,181,183,204,251,],[10,10,10,10,10,10,10,10,10,]),'array':([0,2,76,102,161,181,183,204,232,233,248,249,251,],[11,11,11,11,11,11,11,11,244,245,257,258,11,]),'linkedlist_methods':([0,2,76,102,161,181,183,204,251,],[12,12,12,12,12,12,12,12,12,]),'hashmap_methods':([0,2,76,102,161,181,183,204,251,],[13,13,13,13,13,13,13,13,13,]),'initialization':([0,2,76,102,161,181,183,204,251,],[14,14,14,14,14,14,14,14,14,]),'for_str':([0,2,72,76,102,161,181,183,204,251,],[20,20,101,20,20,20,20,20,20,20,]),'for_str_tagged':([0,2,76,102,161,181,183,204,251,],[21,21,21,21,21,21,21,21,21,]),'if':([0,2,76,102,161,181,183,204,251,],[22,22,22,22,22,22,22,22,22,]),'else':([0,2,76,102,161,181,183,204,251,],[23,23,23,23,23,23,23,23,23,]),'else_if':([0,2,76,102,161,181,183,204,251,],[24,24,24,24,24,24,24,24,24,]),'while':([0,2,76,102,161,181,183,204,251,],[25,25,25,25,25,25,25,25,25,]),'number':([0,2,16,42,43,44,45,76,88,102,120,143,161,166,169,181,183,199,204,251,268,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'hashmap':([0,2,76,102,161,181,183,204,251,],[27,27,27,27,27,27,27,27,27,]),'linkedlist':([0,2,76,102,161,181,183,204,251,],[28,28,28,28,28,28,28,28,28,]),'let_initialization':([0,2,76,102,161,181,183,204,251,],[30,30,30,30,30,30,30,30,30,]),'const_initialization':([0,2,76,102,161,181,183,204,251,],[31,31,31,31,31,31,31,31,31,]),'label':([0,2,76,102,161,181,183,204,251,],[33,33,33,33,33,33,33,33,33,]),'linkedlist_push':([18,],[53,]),'linkedlist_remove':([18,],[54,]),'hashmap_insert':([18,],[55,]),'hashmap_remove':([18,],[56,]),'mdata':([29,68,98,118,120,147,166,],[59,99,151,164,99,179,99,]),'data':([29,68,88,98,103,111,118,120,143,145,147,166,169,178,187,199,],[60,60,122,60,157,159,60,60,172,176,60,60,194,202,211,219,]),'tuple':([29,68,88,98,103,111,118,120,143,145,147,166,169,178,187,199,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'conditional':([34,77,],[73,113,]),'and':([34,77,],[75,75,]),'comparator':([74,75,],[103,111,]),'expression_var':([88,143,169,199,268,],[123,173,195,220,271,]),'data_type':([89,115,144,168,198,226,],[128,162,175,193,218,241,]),'arguments':([96,],[148,]),'range':([100,],[154,]),'return':([251,],[260,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main_rule","S'",1,None,None,None),
  ('main_rule -> father_rule','main_rule',1,'p_main_rule','pyacc.py',11),
  ('main_rule -> father_rule main_rule','main_rule',2,'p_main_rule','pyacc.py',12),
  ('father_rule -> print','father_rule',1,'p_father_rule','pyacc.py',17),
  ('father_rule -> dvariable','father_rule',1,'p_father_rule','pyacc.py',18),
  ('father_rule -> function','father_rule',1,'p_father_rule','pyacc.py',19),
  ('father_rule -> variables','father_rule',1,'p_father_rule','pyacc.py',20),
  ('father_rule -> control_str','father_rule',1,'p_father_rule','pyacc.py',21),
  ('father_rule -> expression','father_rule',1,'p_father_rule','pyacc.py',22),
  ('father_rule -> void','father_rule',1,'p_father_rule','pyacc.py',23),
  ('father_rule -> data_str','father_rule',1,'p_father_rule','pyacc.py',24),
  ('father_rule -> array','father_rule',1,'p_father_rule','pyacc.py',25),
  ('father_rule -> linkedlist_methods','father_rule',1,'p_father_rule','pyacc.py',26),
  ('father_rule -> hashmap_methods','father_rule',1,'p_father_rule','pyacc.py',27),
  ('father_rule -> initialization','father_rule',1,'p_father_rule','pyacc.py',28),
  ('expression -> expression PLUS expression','expression',3,'p_expression','pyacc.py',34),
  ('expression -> expression MINUS expression','expression',3,'p_expression','pyacc.py',35),
  ('expression -> expression TIMES expression','expression',3,'p_expression','pyacc.py',36),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','pyacc.py',37),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','pyacc.py',38),
  ('expression -> number','expression',1,'p_expression','pyacc.py',39),
  ('number -> INTEGER','number',1,'p_number','pyacc.py',44),
  ('number -> FLOAT','number',1,'p_number','pyacc.py',45),
  ('number -> VARIABLE','number',1,'p_number','pyacc.py',46),
  ('data_type -> UNSIG_INT_8','data_type',1,'p_data_type','pyacc.py',50),
  ('data_type -> UNSIG_INT_16','data_type',1,'p_data_type','pyacc.py',51),
  ('data_type -> UNSIG_INT_32','data_type',1,'p_data_type','pyacc.py',52),
  ('data_type -> UNSIG_INT_64','data_type',1,'p_data_type','pyacc.py',53),
  ('data_type -> UNSIG_INT_128','data_type',1,'p_data_type','pyacc.py',54),
  ('data_type -> SIG_INT_8','data_type',1,'p_data_type','pyacc.py',55),
  ('data_type -> SIG_INT_16','data_type',1,'p_data_type','pyacc.py',56),
  ('data_type -> SIG_INT_32','data_type',1,'p_data_type','pyacc.py',57),
  ('data_type -> SIG_INT_64','data_type',1,'p_data_type','pyacc.py',58),
  ('data_type -> SIG_INT_128','data_type',1,'p_data_type','pyacc.py',59),
  ('data_type -> FLOAT_32','data_type',1,'p_data_type','pyacc.py',60),
  ('data_type -> FLOAT_64','data_type',1,'p_data_type','pyacc.py',61),
  ('data_type -> KW_BOOLEAN','data_type',1,'p_data_type','pyacc.py',62),
  ('data_type -> KW_STRING','data_type',1,'p_data_type','pyacc.py',63),
  ('data -> CADENA','data',1,'p_data','pyacc.py',67),
  ('data -> INTEGER','data',1,'p_data','pyacc.py',68),
  ('data -> CHAR','data',1,'p_data','pyacc.py',69),
  ('data -> FLOAT','data',1,'p_data','pyacc.py',70),
  ('data -> KW_FALSE','data',1,'p_data','pyacc.py',71),
  ('data -> KW_TRUE','data',1,'p_data','pyacc.py',72),
  ('data -> tuple','data',1,'p_data','pyacc.py',73),
  ('comparator -> <empty>','comparator',0,'p_comparator','pyacc.py',76),
  ('comparator -> EQ','comparator',1,'p_comparator','pyacc.py',77),
  ('comparator -> NE','comparator',1,'p_comparator','pyacc.py',78),
  ('comparator -> GE','comparator',1,'p_comparator','pyacc.py',79),
  ('comparator -> LE','comparator',1,'p_comparator','pyacc.py',80),
  ('comparator -> GT','comparator',1,'p_comparator','pyacc.py',81),
  ('comparator -> LT','comparator',1,'p_comparator','pyacc.py',82),
  ('and -> VARIABLE LAND VARIABLE','and',3,'p_and','pyacc.py',85),
  ('conditional -> VARIABLE comparator data','conditional',3,'p_conditional','pyacc.py',88),
  ('conditional -> and comparator data','conditional',3,'p_conditional','pyacc.py',89),
  ('or -> VARIABLE LOR VARIABLE','or',3,'p_or','pyacc.py',92),
  ('mdata -> data','mdata',1,'p_mdata','pyacc.py',95),
  ('mdata -> data COMMA mdata','mdata',3,'p_mdata','pyacc.py',96),
  ('print -> KW_PRINT LPAREN CADENA RPAREN SEMI','print',5,'p_print','pyacc.py',99),
  ('dvariable -> KW_LET VARIABLE SEMI','dvariable',3,'p_declare_variable','pyacc.py',102),
  ('array -> KW_LET VARIABLE EQUALS LBRACKET mdata RBRACKET','array',6,'p_array','pyacc.py',105),
  ('array -> LBRACKET mdata RBRACKET','array',3,'p_array','pyacc.py',106),
  ('variables -> VARIABLE','variables',1,'p_variables','pyacc.py',109),
  ('variables -> VARIABLE COMMA variables','variables',3,'p_variables','pyacc.py',110),
  ('while -> KW_WHILE LPAREN VARIABLE','while',3,'p_while','pyacc.py',113),
  ('tuple -> LPAREN mdata RPAREN','tuple',3,'p_tuple','pyacc.py',120),
  ('initialization -> let_initialization SEMI','initialization',2,'p_initialization','pyacc.py',124),
  ('initialization -> const_initialization SEMI','initialization',2,'p_initialization','pyacc.py',125),
  ('initialization -> data_str SEMI','initialization',2,'p_initialization','pyacc.py',126),
  ('let_initialization -> KW_LET VARIABLE EQUALS data','let_initialization',4,'p_let_initialization','pyacc.py',130),
  ('let_initialization -> KW_LET VARIABLE COLON data_type EQUALS data','let_initialization',6,'p_let_initialization','pyacc.py',131),
  ('let_initialization -> KW_LET KW_MUT VARIABLE EQUALS data','let_initialization',5,'p_let_initialization','pyacc.py',132),
  ('let_initialization -> KW_LET KW_MUT VARIABLE COLON data_type EQUALS data','let_initialization',7,'p_let_initialization','pyacc.py',133),
  ('let_initialization -> KW_LET VARIABLE EQUALS expression_var','let_initialization',4,'p_let_initialization','pyacc.py',134),
  ('let_initialization -> KW_LET VARIABLE COLON data_type EQUALS expression_var','let_initialization',6,'p_let_initialization','pyacc.py',135),
  ('let_initialization -> KW_LET KW_MUT VARIABLE EQUALS expression_var','let_initialization',5,'p_let_initialization','pyacc.py',136),
  ('let_initialization -> KW_LET KW_MUT VARIABLE COLON data_type EQUALS expression_var','let_initialization',7,'p_let_initialization','pyacc.py',137),
  ('const_initialization -> KW_CONST VARIABLE COLON data_type EQUALS data','const_initialization',6,'p_const_initialization','pyacc.py',141),
  ('arguments -> void','arguments',1,'p_arguments','pyacc.py',145),
  ('arguments -> variables','arguments',1,'p_arguments','pyacc.py',146),
  ('function -> KW_FN VARIABLE LPAREN arguments RPAREN LBRACE main_rule RBRACE','function',8,'p_function','pyacc.py',150),
  ('control_str -> for_str','control_str',1,'p_control_str','pyacc.py',154),
  ('control_str -> for_str_tagged','control_str',1,'p_control_str','pyacc.py',155),
  ('control_str -> if','control_str',1,'p_control_str','pyacc.py',156),
  ('control_str -> else','control_str',1,'p_control_str','pyacc.py',157),
  ('control_str -> else_if','control_str',1,'p_control_str','pyacc.py',158),
  ('control_str -> while','control_str',1,'p_control_str','pyacc.py',159),
  ('for_str -> KW_FOR VARIABLE KW_IN range LBRACE main_rule RBRACE','for_str',7,'p_for_str','pyacc.py',163),
  ('for_str -> KW_FOR VARIABLE KW_IN VARIABLE LBRACE main_rule RBRACE','for_str',7,'p_for_str','pyacc.py',164),
  ('for_str_tagged -> label COLON for_str','for_str_tagged',3,'p_for_str_tagged','pyacc.py',168),
  ('range -> INTEGER DOT DOT INTEGER','range',4,'p_range','pyacc.py',172),
  ('range -> VARIABLE DOT DOT VARIABLE','range',4,'p_range','pyacc.py',173),
  ('label -> QUOTE VARIABLE','label',2,'p_label','pyacc.py',177),
  ('data_str -> array','data_str',1,'p_data_str','pyacc.py',181),
  ('data_str -> hashmap','data_str',1,'p_data_str','pyacc.py',182),
  ('data_str -> linkedlist','data_str',1,'p_data_str','pyacc.py',183),
  ('hashmap -> KW_LET VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN','hashmap',9,'p_hashmap','pyacc.py',187),
  ('hashmap -> KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_NEW LPAREN RPAREN','hashmap',10,'p_hashmap','pyacc.py',188),
  ('hashmap -> KW_LET VARIABLE EQUALS KW_HASHMAP COLON COLON KW_FROM LPAREN array RPAREN','hashmap',10,'p_hashmap','pyacc.py',189),
  ('hashmap -> KW_LET KW_MUT VARIABLE EQUALS KW_HASHMAP COLON COLON KW_FROM LPAREN array RPAREN','hashmap',11,'p_hashmap','pyacc.py',190),
  ('hashmap_methods -> VARIABLE hashmap_insert','hashmap_methods',2,'p_hashmap_methods','pyacc.py',194),
  ('hashmap_methods -> VARIABLE hashmap_remove','hashmap_methods',2,'p_hashmap_methods','pyacc.py',195),
  ('hashmap_insert -> DOT KW_INSERT LPAREN mdata RPAREN SEMI','hashmap_insert',6,'p_hashmap_insert','pyacc.py',199),
  ('hashmap_remove -> DOT KW_REMOVE LPAREN AND data RPAREN SEMI','hashmap_remove',7,'p_hashmap_remove','pyacc.py',203),
  ('void -> <empty>','void',0,'p_void','pyacc.py',207),
  ('linkedlist -> KW_LET VARIABLE COLON KW_LINKEDLIST LT data_type GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN','linkedlist',14,'p_linkedlist_empty','pyacc.py',215),
  ('linkedlist -> KW_LET KW_MUT VARIABLE COLON KW_LINKEDLIST LT data_type GT EQUALS KW_LINKEDLIST COLON COLON KW_NEW LPAREN RPAREN','linkedlist',15,'p_linkedlist_empty','pyacc.py',216),
  ('linkedlist -> KW_LET VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN','linkedlist',10,'p_linkedlist_array','pyacc.py',219),
  ('linkedlist -> KW_LET KW_MUT VARIABLE EQUALS KW_LINKEDLIST COLON COLON KW_FROM LPAREN array RPAREN','linkedlist',11,'p_linkedlist_array','pyacc.py',220),
  ('linkedlist_methods -> VARIABLE linkedlist_push','linkedlist_methods',2,'p_linkedlist_methods','pyacc.py',223),
  ('linkedlist_methods -> VARIABLE linkedlist_remove','linkedlist_methods',2,'p_linkedlist_methods','pyacc.py',224),
  ('linkedlist_push -> DOT KW_PUSH_BACK LPAREN data RPAREN SEMI','linkedlist_push',6,'p_linkedlist_push','pyacc.py',227),
  ('linkedlist_remove -> DOT KW_REMOVE LPAREN INTEGER RPAREN SEMI','linkedlist_remove',6,'p_linkedlist_remove','pyacc.py',230),
  ('if -> KW_IF conditional LBRACE main_rule RBRACE','if',5,'p_if','pyacc.py',235),
  ('else -> KW_ELSE LBRACE main_rule RBRACE','else',4,'p_else','pyacc.py',238),
  ('else_if -> KW_ELSE KW_IF conditional LBRACE main_rule RBRACE','else_if',6,'p_else_if','pyacc.py',241),
  ('function -> KW_FN VARIABLE LPAREN arguments RPAREN MINUS GT data_type LBRACE return RBRACE','function',11,'p_function_return','pyacc.py',246),
  ('expression_var -> expression','expression_var',1,'p_expression_var','pyacc.py',249),
  ('expression_var -> VARIABLE','expression_var',1,'p_expression_var','pyacc.py',250),
  ('return -> main_rule','return',1,'p_return_statement','pyacc.py',253),
  ('return -> main_rule KW_RETURN expression_var SEMI','return',4,'p_return_statement','pyacc.py',254),
]
