// conversion.c
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "cdecl.h"


double PRE_CDECL calc (double, double) POST_CDECL;

int main(int argc, char const *argv[]) 
{
    if(argc != 3)
        printf("Faltan argumentos");

    //if(argc = 4){
    double cantidad = atof(argv[1]);
    double valorBTC = atof(argv[2]);
    //char* monedaFinal = argv[3];

    double total = calc(cantidad, valorBTC);

    printf("El total es: %.2f\n", total);

    return 0;
}
