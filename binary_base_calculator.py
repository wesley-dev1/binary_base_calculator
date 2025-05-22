
#!/usr/bin/env python3
"""Binary & Base Conversion Calculator

Features
--------
1. Convert between hexadecimal ↔ binary, decimal ↔ binary/hexadecimal.
2. Perform arithmetic on binary numbers: addition, subtraction,
   multiplication, and division (integer division and remainder).

Usage
-----
Run the script and follow the interactive menu.
"""

import sys

def hex_to_bin(hex_str: str) -> str:
    try:
        return bin(int(hex_str, 16))[2:]
    except ValueError:
        raise ValueError("Entrada hexadecimal inválida.")

def bin_to_hex(bin_str: str) -> str:
    try:
        return hex(int(bin_str, 2))[2:].upper()
    except ValueError:
        raise ValueError("Entrada binária inválida.")

def bin_to_dec(bin_str: str) -> int:
    try:
        return int(bin_str, 2)
    except ValueError:
        raise ValueError("Entrada binária inválida.")

def dec_to_bin(dec_str: str) -> str:
    try:
        return bin(int(dec_str))[2:]
    except ValueError:
        raise ValueError("Entrada decimal inválida.")

def dec_to_hex(dec_str: str) -> str:
    try:
        return hex(int(dec_str))[2:].upper()
    except ValueError:
        raise ValueError("Entrada decimal inválida.")

def calculate_binary(op: str, a_str: str, b_str: str) -> str:
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
        return f'Quociente: {bin(quotient)[2:]}, Resto: {bin(remainder)[2:]}'
    else:
        raise ValueError("Operação inválida.")

    return bin(result)[2:]

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
            h = input("Hexadecimal (sem 0x): ")
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
