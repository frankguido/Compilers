from AnalizadorLex import get_tokens
from Ll1 import parser
from AnalizadorSem import findVal

file_out = open ("codigo.s","w")
def genera_assembler(root):
    file_out.write(".data\n")
    crea_variable(root)#escribe cada variable
    file_out.write(".text\nmain:\n")
    file_out.write("\n \tli $v0,10 \n \tsyscall ")
    
def crea_variable (node):
    #if len(node.children) > 0:
    if node.symbol.symbol == 'TYPE':
        if node.father.symbol.symbol == 'STATEMENT':
            expre = node.father.children[1].children[2]
            term = expre.children[0].children[0]
            val = term.children[0]
            file_out.write("\tvar_" + str(node.father.children[1].children[0].lexeme) + ": .word 0:1"+"\n")
    for child in node.children:
        crea_variable(child)
def suma(node):
    if node.symbol.symbol=="OPER" and node.children[0].symbol.symbol=="opesuma":
        file_out.write("    li $a0, ")
        file_out.write(str(node.father.father.children[1].children[0].lexeme))
        file_out.write("\n")
        file_out.write("    sw $a0 0($sp) \n")
        file_out.write("    add $sp $sp -4 \n")
        file_out.write("    li $a0, ")
        file_out.write(str(node.father.children[1].children[0].lexeme))
        file_out.write("\n")
        file_out.write("    lw $t1 4($sp) \n")
        file_out.write("    add $a0 $t1 $a0 \n")
        file_out.write("    add $sp $sp 4 \n")
        file_out.write("    la $ t1, var_x \n")
        file_out.write("    jr $ra \n")
    for child in node.children:
        suma(child)
"""
def iff(node):
    if node.symbol.symbol=="OPER" and node.symbol.symbol=="if":
        file_out.write("    la $t0, var_")
        file_out.write(str(node.father.children[2].children[0].lexeme))
        file_out.write("\n")
        file_out.write("    lw $a0, 0($t0) \n")
        file_out.write("    sw $a0, 0($sp) \n")
        file_out.write("    add $sp, $sp, -4 \n")
        file_out.write("    li $a0,")
        file_out.write(str(node.father.children[4].children[0].lexeme))
        file_out.write("\n")
        file_out.write("    lw $t1, 4($sp) \n")
        file_out.write("    add $sp, $sp, 4\n")
        file_out.write("    bit $a0, $t1, label_true \n")
        if node.symbol.symbol=="OPER" and node.father.father.children[1].children[0].children[0].symbol.symbol=="else":
            elsee=node.father.father.children[1].children[0].children[0]
            file_out.write("    label_false\n")
            file_out.write("    li $a0, \n")
            file_out.write(str(elsee.father.children[2].children[0].children[2].children[0].lexeme))
            file_out.write("\n")
            file_out.write("    la $t0, var_")
            file_out.write(str(elsee.father.children[2].children[0].children[0].lexeme))
            file_out.write("\n")
            file_out.write("    la #t0, var_")
            file_out.write("    label_end: \n")
            file_out.write("    jr $ra")
    for child in node.children:
        iff(child)


 """


if __name__ == "__main__":
    file_name="test/test1.txt"
    tokens = get_tokens (file_name)
    tokens.append (['$', None, None])
    
    root, node_list = parser(tokens)
    findVal(root)
    genera_assembler(root)
    suma(root)
    #iff(root)
    file_out.close()