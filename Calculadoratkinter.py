import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x500")
janela.configure(bg="black")

for i in range(4):
    janela.columnconfigure(i, weight=1)
for i in range(6):
    janela.rowconfigure(i, weight=1)

visor = tk.Entry(janela, font=("Arial", 32), justify="right", bg="black", fg="white", bd=0)
visor.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew", ipady=10)

def digitar(caractere):
    if visor.get() == "Erro":
        visor.delete(0, tk.END)
    texto_atual = visor.get()
    if caractere in "+-*/":
        if texto_atual == "" or texto_atual[-1] in "+-*/":
            return
        for op in "+-*/":
            if op in texto_atual:
                return
    visor.insert(tk.END, caractere)



def somar():
    texto_completo = visor.get()
    partes = texto_completo.split("+")
    n1 = float(partes[0])
    n2 = float(partes[1])
    resultado = n1 + n2
    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))

def subtrair():
    texto_completo = visor.get()
    partes = texto_completo.split("-")
    n1 = float(partes[0])
    n2 = float(partes[1])
    resultado = n1 - n2
    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))

def multiplicar():
    texto_completo = visor.get()
    partes = texto_completo.split("*")
    n1 = float(partes[0])
    n2 = float(partes[1])
    resultado = n1 * n2
    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))

def dividir():
    texto_completo = visor.get()
    partes = texto_completo.split("/")
    n1 = float(partes[0])
    n2 = float(partes[1])
    visor.delete(0, tk.END)
    if n2!= 0:
        resultado = n1 / n2
        visor.insert(0, str(resultado))
    else:
        visor.insert(0, "Erro")

def limpar():
    visor.delete(0, tk.END)

def apagar_ultimo():
    if visor.get() == "Erro":
        visor.delete(0, tk.END)
    else:
        texto_atual = visor.get()
        visor.delete(0, tk.END)
        visor.insert(0, texto_atual[:-1])

def pressionar_ponto():
    texto = visor.get()
    if texto == "" or texto[-1] in "+-*/":
        return
    numero_atual = texto
    for op in "+-*/":
        if op in texto:
            numero_atual = texto.split(op)[-1]
    if "." not in numero_atual:
        visor.insert(tk.END, ".")

def executar_calculo():
    try:
        texto = visor.get()
        if "+" in texto: somar()
        elif "-" in texto: subtrair()
        elif "*" in texto: multiplicar()
        elif "/" in texto: dividir()
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")


cor_num = "#333333"
cor_func = "#a5a5a5"
cor_op = "#ff9f0a"

tk.Button(janela, text="C", bg=cor_func, fg="black", font=("Arial", 18, "bold"), bd=0, command=limpar).grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="⌫", bg=cor_func, fg="black", font=("Arial", 18, "bold"), bd=0, command=apagar_ultimo).grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="/", bg=cor_op, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("/")).grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

tk.Button(janela, text="7", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("7")).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="8", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("8")).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="9", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("9")).grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="*", bg=cor_op, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("*")).grid(row=2, column=3, sticky="nsew", padx=5, pady=5)

tk.Button(janela, text="4", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("4")).grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="5", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("5")).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="6", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("6")).grid(row=3, column=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="-", bg=cor_op, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("-")).grid(row=3, column=3, sticky="nsew", padx=5, pady=5)

tk.Button(janela, text="1", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("1")).grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="2", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("2")).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="3", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("3")).grid(row=4, column=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="+", bg=cor_op, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("+")).grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

tk.Button(janela, text="0", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=lambda: digitar("0")).grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text=".", bg=cor_num, fg="white", font=("Arial", 18, "bold"), bd=0, command=pressionar_ponto).grid(row=5, column=2, sticky="nsew", padx=5, pady=5)
tk.Button(janela, text="=", bg=cor_op, fg="white", font=("Arial", 18, "bold"), bd=0, command=executar_calculo).grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

janela.mainloop()

