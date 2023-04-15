section .text
global calc

calc:
    enter 0, 0
    ;push ebp           ; guardar el puntero de pila actual
    mov ebp, esp        ; establecer un nuevo puntero de pila

    mov  eax, [ebp+12]
    imul eax, [ebp+8]

;   mov eax, [ebp+8]    ; mover el primer argumento a eax
;   add eax, [ebp+12]   ; sumar el segundo argumento a eax
;   mov edx, [ebp+16]   ; mover la dirección del tercer argumento a edx
;   mov [edx], eax      ; mover el resultado a la dirección del tercer argumento

    ;pop ebp            ; restaurar el puntero de pila original
;    mov eax, 0
    leave
    ret                 ; retornar