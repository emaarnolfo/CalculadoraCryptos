%include "./src/asm_io.inc"



segment .data

segment .bss

segment .text
    global calc

calc:
    enter 0, 0
    pusha

    fld qword [ebp+8]       ; cargar el primer número en el registro ST0
    fld qword [ebp+16]      ; cargar el segundo número en el registro ST1
    fmul st1, st0           ; multiplicar los dos números (el resultado queda en ST0)
    fstp qword [ebp+8]      ; mover el resultado a la variable de retorno
    
    dump_regs 1
    dump_stack 1, 2, 4

    popa
    leave
    ret                     ; retornar