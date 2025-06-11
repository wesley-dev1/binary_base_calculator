import tkinter as tk
from tkinter import ttk, messagebox

# Funções de conversão e cálculo (mesmas do script original)

def hex_to_bin(hex_str: str) -> str:
    sign = '-' if hex_str.startswith('-') else ''
    clean = hex_str.lstrip('+-').lstrip('0x').lstrip('0X')
    try:
        return sign + bin(int(clean, 16))[2:]
    except ValueError:
        raise ValueError("Entrada hexadecimal inválida.")


def validate_binary(bin_str: str):
    if not all(c in '01' for c in bin_str):
        raise ValueError("Entrada binária inválida. Use apenas 0s e 1s.")


def bin_to_hex(bin_str: str) -> str:
    sign = '-' if bin_str.startswith('-') else ''
    clean = bin_str.lstrip('+-')
    validate_binary(clean)
    try:
        return sign + hex(int(clean, 2))[2:].upper()
    except ValueError:
        raise ValueError("Entrada binária inválida.")


def bin_to_dec(bin_str: str) -> int:
    sign = -1 if bin_str.startswith('-') else 1
    clean = bin_str.lstrip('+-')
    validate_binary(clean)
    return sign * int(clean, 2)


def dec_to_bin(dec_str: str) -> str:
    num = int(dec_str)
    return ('-' if num < 0 else '') + bin(abs(num))[2:]


def dec_to_hex(dec_str: str) -> str:
    num = int(dec_str)
    return ('-' if num < 0 else '') + hex(abs(num))[2:].upper()


def calculate_binary(op: str, a_str: str, b_str: str) -> str:
    a = bin_to_dec(a_str)
    b = bin_to_dec(b_str)
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        q = a // b
        r = a % b
        return f"Quociente: {dec_to_bin(str(q))}, Resto: {dec_to_bin(str(r))}"
    else:
        raise ValueError("Operação inválida.")
    return dec_to_bin(str(res))

# Interface gráfica
class BaseCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Bases e Binários")
        self.geometry("400x300")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        # Aba de conversão
        conv_frame = ttk.Frame(notebook)
        notebook.add(conv_frame, text='Conversões')
        self._build_conversion_tab(conv_frame)

        # Aba de operações binárias
        op_frame = ttk.Frame(notebook)
        notebook.add(op_frame, text='Operações Binárias')
        self._build_binary_tab(op_frame)

    def _build_conversion_tab(self, frame):
        options = [
            "Hex → Bin",
            "Bin → Hex",
            "Bin → Dec",
            "Dec → Bin",
            "Dec → Hex"
        ]
        ttk.Label(frame, text="Tipo de Conversão:").pack(pady=5)
        self.conv_type = ttk.Combobox(frame, values=options, state='readonly')
        self.conv_type.current(0)
        self.conv_type.pack()

        ttk.Label(frame, text="Entrada:").pack(pady=5)
        self.conv_input = ttk.Entry(frame)
        self.conv_input.pack()

        ttk.Button(frame, text="Converter", command=self._on_convert).pack(pady=10)
        self.conv_result = ttk.Label(frame, text="Resultado: ")
        self.conv_result.pack(pady=5)

    def _on_convert(self):
        typ = self.conv_type.get()
        val = self.conv_input.get().strip()
        try:
            if typ == "Hex → Bin":
                res = hex_to_bin(val)
            elif typ == "Bin → Hex":
                res = bin_to_hex(val)
            elif typ == "Bin → Dec":
                res = str(bin_to_dec(val))
            elif typ == "Dec → Bin":
                res = dec_to_bin(val)
            elif typ == "Dec → Hex":
                res = dec_to_hex(val)
            else:
                res = ""
            self.conv_result.config(text=f"Resultado: {res}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def _build_binary_tab(self, frame):
        ttk.Label(frame, text="Primeiro binário:").pack(pady=5)
        self.bin_a = ttk.Entry(frame)
        self.bin_a.pack()

        ttk.Label(frame, text="Segundo binário:").pack(pady=5)
        self.bin_b = ttk.Entry(frame)
        self.bin_b.pack()

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        for sym in ['+', '-', '*', '/']:
            ttk.Button(btn_frame, text=sym, width=3,
                       command=lambda op=sym: self._do_bin_op(op)).pack(side='left', padx=5)

        self.bin_result = ttk.Label(frame, text="Resultado: ")
        self.bin_result.pack(pady=5)

    def _do_bin_op(self, op: str):
        a = self.bin_a.get().strip()
        b = self.bin_b.get().strip()
        try:
            res = calculate_binary(op, a, b)
            self.bin_result.config(text=f"Resultado: {res}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    app = BaseCalculatorApp()
    app.mainloop()
