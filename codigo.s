.data
	var_x: .word 0:1
	var_z: .word 0:1
.text
main:

 	li $v0,10 
 	syscall     li $a0, None
    sw $a0 0($sp) 
    add $sp $sp -4 
    li $a0, None
    lw $t1 4($sp) 
    add $a0 $t1 $a0 
    add $sp $sp 4 
    la $ t1, var_x 
    jr $ra 
