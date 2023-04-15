// conversion.c
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "cdecl.h"

extern double calc (double, double);

int main(int argc, char const *argv[])  //12, euro, BTC
{
    //if(argc = 4){
    double cantidad = atof(argv[1]);
    double valorBTC = atof(argv[2]);
    //char* monedaFinal = argv[3];

    double total = calc(cantidad, valorBTC);

    printf("El total es: %.2f\n", total);

    return 0;
}
