%include "./src/asm_io.inc"

segment .data

segment .bss

segment .text
    global calc

calc:
    enter 0, 0              ; Guarda los bytes que se van a utilizar localmente en la funcion
                            ; En nuestro caso 0 porqque no utilizamos variables locales
    pusha                   ; Pushea en la pila los registros

    fld qword [ebp+8]       ; cargar el primer número en el registro ST0
    fld qword [ebp+16]      ; cargar el segundo número en el registro ST1
    fmul st1, st0           ; multiplicar los dos números (el resultado queda en ST0)
    fstp qword [ebp+8]      ; mover el resultado a la variable de retorno
    
    dump_regs 1             ; Imprime los valores de todos los registros 
    dump_stack 1, 2, 4      ; Imprime las posiciones de la pila y la informacion de cada registro

    popa                    ; Limpia los registros pusheados por pusha
    leave                   ; Limpia las variables locales y hace un pop del ebp 
    ret                     ; Retorna a la funcion llamadora