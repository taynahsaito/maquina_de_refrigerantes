import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

I = ['m25', 'm50', 'm100', 'b']
T = {
    ('s0', 'b'): ('s0', 'n'), 
    ('s0', 'm25'): ('s1', 'n'),
    ('s0', 'm50'): ('s2', 'n'),
    ('s0', 'm100'): ('s4', 'n'),

    ('s1', 'b'): ('s1', 'n'),
    ('s1', 'm25'): ('s2', 'n'),
    ('s1', 'm50'): ('s3', 'n'),
    ('s1', 'm100'): ('s5', 'n'),

    ('s2', 'b'): ('s2', 'n'),
    ('s2', 'm25'): ('s3', 'n'),
    ('s2', 'm50'): ('s4', 'n'),
    ('s2', 'm100'): ('s6', 'n'),

    ('s3', 'b'): ('s3', 'n'),
    ('s3', 'm25'): ('s4', 'n'),
    ('s3', 'm50'): ('s5', 'n'),
    ('s3', 'm100'): ('s7', 'n'),

    ('s4', 'b'): ('s4', 'n'),
    ('s4', 'm25'): ('s5', 'n'),
    ('s4', 'm50'): ('s6', 'n'),
    ('s4', 'm100'): ('s8', 'n'),

    ('s5', 'b'): ('s5', 'n'),
    ('s5', 'm25'): ('s6', 'n'),
    ('s5', 'm50'): ('s7', 'n'),
    ('s5', 'm100'): ('s8', 't25'),  

    ('s6', 'b'): ('s6', 'n'),
    ('s6', 'm25'): ('s7', 'n'),
    ('s6', 'm50'): ('s8', 'n'),
    ('s6', 'm100'): ('s8', 't50'),  

    ('s7', 'b'): ('s7', 'n'),
    ('s7', 'm25'): ('s8', 'n'),
    ('s7', 'm50'): ('s8', 't25'),
    ('s7', 'm100'): ('s8', 't75'),

    ('s8', 'b'): ('s0', 'r'), 
    ('s8', 'm25'): ('s8', 't25'),
    ('s8', 'm50'): ('s8', 't50'),
    ('s8', 'm100'): ('s8', 't100')
}

estado_atual = 's0'
saldo_atual = 0.00
preco_refrigerante = 2.00

def proximo_estado(estado, entrada):
    if entrada not in I:
        return ("Entrada inválida", None)
    return T.get((estado, entrada), ("Transição não definida", None))

def transicao(entrada):
    global estado_atual, saldo_atual

    novo_estado, saida = proximo_estado(estado_atual, entrada)

    if entrada == "m25":
        saldo_atual += 0.25
    elif entrada == "m50":
        saldo_atual += 0.50
    elif entrada == "m100":
        saldo_atual += 1.00

    estado_atual = novo_estado 

    if entrada == 'b':
        if saldo_atual >= preco_refrigerante:
            messagebox.showinfo("Refrigerante", "Refrigerante liberado!")
            saldo_atual = 0 
            estado_atual = 's0' 
        else:
            messagebox.showwarning("Saldo Insuficiente", "Saldo insuficiente.")

    atualizar_saldo()

def liberar_refrigerante():
    global saldo_atual
    if saldo_atual >= preco_refrigerante:
        troco = saldo_atual - preco_refrigerante
        if troco > 0:
            messagebox.showinfo("Refrigerante", f"Refrigerante liberado! Troco: R${troco:.2f}")
        else:
            messagebox.showinfo("Refrigerante", "Refrigerante liberado! Sem troco.")
        
        saldo_atual = 0 
        estado_atual = 's0'  
    else:
        messagebox.showwarning("Saldo Insuficiente", "Saldo insuficiente.")
    
    atualizar_saldo()


def atualizar_saldo():
    saldo_label.config(text=f"Saldo: R${saldo_atual:.2f}")

def inserir_moeda(valor):
    transicao(valor)

janela = tk.Tk()
janela.title("Simulador de Máquina de Vendas")
janela.geometry("1000x1000")

imagem_fundo = Image.open("fundo_maquina.png") 
imagem_fundo = imagem_fundo.resize((1000, 1000), Image.Resampling.LANCZOS) 
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

fundo_label = tk.Label(janela, image=imagem_fundo)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1) 

container_frame = tk.Frame(janela, bg="#7d2423")
container_frame.pack(side="right", padx=85, pady=85, anchor="e")

saldo_label = tk.Label(container_frame, text=f"Saldo: R$0.00", font=("Poppins", 18, "bold"), bg="#7d2423", fg="#f9e4d2")
saldo_label.pack(pady=10)

botao_frame = tk.Frame(container_frame, bg="#7d2423")
botao_frame.pack(pady=20)

moeda_25 = tk.Button(botao_frame, text="R$0,25", font=("Poppins", 12), width=30, height=2, bg="#f9e4d2", fg="#333", command=lambda: inserir_moeda("m25"))
moeda_25.grid(row=0, column=0, padx=10, pady=5)

moeda_50 = tk.Button(botao_frame, text="R$0,50", font=("Poppins", 12), width=30, height=2, bg="#f9e4d2", fg="#333", command=lambda: inserir_moeda("m50"))
moeda_50.grid(row=1, column=0, padx=10, pady=5)

moeda_100 = tk.Button(botao_frame, text="R$1,00", font=("Poppins", 12), width=30, height=2, bg="#f9e4d2", fg="#333", command=lambda: inserir_moeda("m100"))
moeda_100.grid(row=2, column=0, padx=10, pady=5)

botao_refrigerante = tk.Button(container_frame, text="Comprar", font=("Poppins", 14, "bold"), width=10, height=1, bg="#101010", fg="#f9e4d2", command=liberar_refrigerante)
botao_refrigerante.pack(pady=20)
janela.mainloop()
