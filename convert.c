// conversion.c
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cdecl.h"

int PRE_CDECL calc (int, int) POST_CDECL;

//Cantidad a multiplicar
// Moneda que queremos multiplicar
/* int calculadora(int cantidad, int moneda) {
    
    int total;
    calc(moneda, cantidad, &total);
    //Revisar como limpiar stack
    return total;
} */

int main(int argc, char const *argv[])  //12, euro, BTC
{
    //if(argc = 4){
    int cantidad = atoi(argv[1]);
    int valorBTC = atoi(argv[2]);
    //char* monedaFinal = argv[3];

    int total = calc(cantidad, valorBTC);

    printf("El total es: %d\n", total);

    return 0;
}
