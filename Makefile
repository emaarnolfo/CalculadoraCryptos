# Variables para los nombres de los archivos y directorios
BUILD_DIR = ./build
SRC_DIR = ./src

# Opciones de compilación para el ensamblador NASM y el compilador GCC
NASMFLAGS = -f elf32

all: main

# Regla para construir el archivo ejecutable
main: mult.o asm_io.o
	gcc -m32 -o ./build/main $(SRC_DIR)/convert.c $(BUILD_DIR)/mult.o $(BUILD_DIR)/asm_io.o

# Regla para construir el archivo objeto de la suma
mult.o: asm_io.o
	nasm $(NASMFLAGS) -o $(BUILD_DIR)/mult.o $(SRC_DIR)/mult.asm
	
asm_io.o:
	mkdir -p $(BUILD_DIR)
	nasm $(NASMFLAGS) -d ELF_TYPE -o $(BUILD_DIR)/asm_io.o $(SRC_DIR)/asm_io.asm
	