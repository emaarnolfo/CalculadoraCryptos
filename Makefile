# Variables para los nombres de los archivos y directorios
BUILD_DIR = ./build

# Opciones de compilación para el ensamblador NASM y el compilador GCC
NASMFLAGS = -f elf32

all: main

# Regla para construir el archivo ejecutable
main: mult.o asm_io.o
	gcc -m32 -o main ./convert.c $(BUILD_DIR)/mult.o $(BUILD_DIR)/asm_io.o
	mv main ./build/main

# Regla para construir el archivo objeto de la suma
mult.o:
	mkdir -p $(BUILD_DIR)
	nasm $(NASMFLAGS) -o $(BUILD_DIR)/mult.o ./mult.asm
	
asm_io.o:
	nasm $(NASMFLAGS) -d ELF_TYPE -o $(BUILD_DIR)/asm_io.o ./asm_io.asm
	