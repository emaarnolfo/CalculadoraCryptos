section .text
global calc

calc:
    enter 0, 0
    ;pusha
    mov ebp, esp        ; establecer un nuevo puntero de pila

    mov  eax, [ebp+12]
    imul eax, [ebp+8]

    ;popa
    leave
    ret                 ; retornar