#!/usr/bin/env python3
"""Calculadora de Conversão Binária e de Bases

Recursos
--------
1. Converter entre hexadecimal ↔ binário, decimal ↔ binário/hexadecimal.
2. Realizar operações aritméticas com números binários: adição, subtração,
   multiplicação e divisão (divisão inteira e resto).

Uso
----
Execute o script e siga o menu interativo.
"""

import sys

def hex_to_bin(hex_str: str) -> str:
    # Remove o prefixo 0x se existir
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    try:
        return bin(int(hex_str, 16))[2:]
    except ValueError:
        raise ValueError("Entrada hexadecimal inválida.")

def validate_binary(bin_str: str):
    if bin_str.startswith('-'):
        # Valida a parte após o sinal de negativo
        if not all(char in '01' for char in bin_str[1:]):
            raise ValueError("Entrada binária inválida. Use apenas 0s e 1s.")
    else:
        if not all(char in '01' for char in bin_str):
            raise ValueError("Entrada binária inválida. Use apenas 0s e 1s.")

def bin_to_hex(bin_str: str) -> str:
    try:
        validate_binary(bin_str)
        # Trata números negativos
        if bin_str.startswith('-'):
            num = -int(bin_str[1:], 2)
        else:
            num = int(bin_str, 2)
        hex_result = hex(num)[2:].upper()
        return hex_result if not hex_result.startswith('-') else '-' + hex_result[1:]
    except ValueError as e:
        raise e

def bin_to_dec(bin_str: str) -> int:
    try:
        validate_binary(bin_str)
        # Trata números negativos
        if bin_str.startswith('-'):
            return -int(bin_str[1:], 2)
        return int(bin_str, 2)
    except ValueError as e:
        raise e

def dec_to_bin(dec_str: str) -> str:
    try:
        num = int(dec_str)
        # Trata números negativos
        if num < 0:
            return '-' + bin(abs(num))[2:]
        return bin(num)[2:]
    except ValueError:
        raise ValueError("Entrada decimal inválida.")

def dec_to_hex(dec_str: str) -> str:
    try:
        num = int(dec_str)
        # Trata números negativos
        if num < 0:
            return '-' + hex(abs(num))[2:].upper()
        return hex(num)[2:].upper()
    except ValueError:
        raise ValueError("Entrada decimal inválida.")

def calculate_binary(op: str, a_str: str, b_str: str) -> str:
    validate_binary(a_str)
    validate_binary(b_str)
    
    a = bin_to_dec(a_str)
    b = bin_to_dec(b_str)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        quotient = a // b
        remainder = a % b
        return f'Quociente: {dec_to_bin(str(quotient))}, Resto: {dec_to_bin(str(remainder))}'
    else:
        raise ValueError("Operação inválida.")

    # Converte o resultado de volta para binário
    return dec_to_bin(str(result))

def conversion_menu():
    print("\n*** Conversão de Bases ***")
    print("1) Hexadecimal → Binário")
    print("2) Binário → Hexadecimal")
    print("3) Binário → Decimal")
    print("4) Decimal → Binário")
    print("5) Decimal → Hexadecimal")
    print("0) Voltar")
    choice = input("Escolha: ").strip()

    try:
        if choice == '1':
            h = input("Hexadecimal (com ou sem 0x): ")
            print("Binário:", hex_to_bin(h))
        elif choice == '2':
            b = input("Binário: ")
            print("Hexadecimal:", bin_to_hex(b))
        elif choice == '3':
            b = input("Binário: ")
            print("Decimal:", bin_to_dec(b))
        elif choice == '4':
            d = input("Decimal: ")
            print("Binário:", dec_to_bin(d))
        elif choice == '5':
            d = input("Decimal: ")
            print("Hexadecimal:", dec_to_hex(d))
        elif choice == '0':
            return
        else:
            print("Opção inválida.")
    except Exception as e:
        print("Erro:", e)

def binary_calc_menu():
    print("\n*** Operações com Binários ***")
    print("Suporta: soma (+), subtração (-), multiplicação (*), divisão (/).")
    a = input("Primeiro número binário: ").strip()
    op = input("Operação (+, -, *, /): ").strip()
    b = input("Segundo número binário: ").strip()
    try:
        result = calculate_binary(op, a, b)
        print("Resultado:", result)
    except Exception as e:
        print("Erro:", e)

def main():
    while True:
        print("\n====== CALCULADORA DE BASES ======")
        print("1) Conversões de base")
        print("2) Operações com binários")
        print("0) Sair")
        option = input("Escolha: ").strip()
        if option == '1':
            conversion_menu()
        elif option == '2':
            binary_calc_menu()
        elif option == '0':
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
