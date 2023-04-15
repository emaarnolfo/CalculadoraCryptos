# Variables para los nombres de los archivos y directorios
BUILD_DIR = ./build

# Opciones de compilación para el ensamblador NASM y el compilador GCC
NASMFLAGS = -f elf32
# Regla para construir el archivo ejecutable
main: suma.o
	gcc -m32 -o main ./convert.c $(BUILD_DIR)/suma.o 
	mv main ./build/main

# Regla para construir el archivo objeto de la suma
suma.o:
	mkdir -p $(BUILD_DIR)
	nasm $(NASMFLAGS) -o $(BUILD_DIR)/suma.o ./convert.asm
	
