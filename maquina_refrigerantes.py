import tkinter as tk
from tkinter import messagebox

# Alfabeto
I = ['m25', 'm50', 'm100', 'b']
# Tabela de estados (mesma que você forneceu)
T = {
    # Estado s0
    ('s0', 'b'): ('s0', 'n'), 
    ('s0', 'm25'): ('s1', 'n'),
    ('s0', 'm50'): ('s2', 'n'),
    ('s0', 'm100'): ('s4', 'n'),

    # Estado s1
    ('s1', 'b'): ('s1', 'n'),
    ('s1', 'm25'): ('s2', 'n'),
    ('s1', 'm50'): ('s3', 'n'),
    ('s1', 'm100'): ('s5', 'n'),

    # Estado s2
    ('s2', 'b'): ('s2', 'n'),
    ('s2', 'm25'): ('s3', 'n'),
    ('s2', 'm50'): ('s4', 'n'),
    ('s2', 'm100'): ('s6', 'n'),

    # Estado s3
    ('s3', 'b'): ('s3', 'n'),
    ('s3', 'm25'): ('s4', 'n'),
    ('s3', 'm50'): ('s5', 'n'),
    ('s3', 'm100'): ('s7', 'n'),

    # Estado s4
    ('s4', 'b'): ('s4', 'n'),
    ('s4', 'm25'): ('s5', 'n'),
    ('s4', 'm50'): ('s6', 'n'),
    ('s4', 'm100'): ('s8', 'n'),

    # Estado s5
    ('s5', 'b'): ('s5', 'n'),
    ('s5', 'm25'): ('s6', 'n'),
    ('s5', 'm50'): ('s7', 'n'),
    ('s5', 'm100'): ('s8', 't25'),  

    # Estado s6
    ('s6', 'b'): ('s6', 'n'),
    ('s6', 'm25'): ('s7', 'n'),
    ('s6', 'm50'): ('s8', 'n'),
    ('s6', 'm100'): ('s8', 't50'),  

    # Estado s7
    ('s7', 'b'): ('s7', 'n'),
    ('s7', 'm25'): ('s8', 'n'),
    ('s7', 'm50'): ('s8', 't25'),
    ('s7', 'm100'): ('s8', 't75'),

    # Estado s8
    ('s8', 'b'): ('s0', 'r'), 
    ('s8', 'm25'): ('s8', 't25'),
    ('s8', 'm50'): ('s8', 't50'),
    ('s8', 'm100'): ('s8', 't100')
}

# Formatação das saídas
formatacao_saida = {
    'n': '',
    'm25': 'R$0,25',
    'm50': 'R$0,50',
    'm100': 'R$1,00',
    'r': 'Refrigerante',
    't25': 'Entregue: R$0,25',
    't50': 'Entregue: R$0,50',
    't75': 'Entregue: R$0,75',
    't100': 'Entregue: R$1,00'
}

def proximo_estado(estado, entrada):
    if entrada not in I:
        return ("Entrada inválida", None)
    return T.get((estado, entrada), ("Transição não definida", None))

class MaquinaDeVenda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Máquina de Venda")
        self.geometry("300x300")
        
        self.estado_atual = 's0'
        
        self.label_estado = tk.Label(self, text="Estado: s0")
        self.label_estado.pack(pady=10)

        self.label_saida = tk.Label(self, text="Saída: n")
        self.label_saida.pack(pady=10)

        self.botoes_frame = tk.Frame(self)
        self.botoes_frame.pack(pady=20)

        self.btn_m25 = tk.Button(self.botoes_frame, text="25 centavos", command=lambda: self.adicionar_moeda('m25'))
        self.btn_m25.grid(row=0, column=0, padx=5)

        self.btn_m50 = tk.Button(self.botoes_frame, text="50 centavos", command=lambda: self.adicionar_moeda('m50'))
        self.btn_m50.grid(row=0, column=1, padx=5)

        self.btn_m100 = tk.Button(self.botoes_frame, text="1 real", command=lambda: self.adicionar_moeda('m100'))
        self.btn_m100.grid(row=0, column=2, padx=5)

        self.btn_entrar = tk.Button(self.botoes_frame, text="Entrar", command=lambda: self.adicionar_moeda('b'))
        self.btn_entrar.grid(row=0, column=3, padx=5)

    def atualizar_interface(self, saida):
        # Formata a saída usando o dicionário
        saida_formatada = formatacao_saida.get(saida, "Saída desconhecida")
        self.label_estado.config(text=f"Estado: {self.estado_atual}")
        self.label_saida.config(text=f"Saída: {saida_formatada}")
        print(f"Estado Atual: {self.estado_atual}, Saída: {saida_formatada}")

    def adicionar_moeda(self, entrada):
        print(f"Tentando adicionar moeda: {entrada}")
        self.estado_atual, saida = proximo_estado(self.estado_atual, entrada)
        print(f"Novo Estado: {self.estado_atual}, Saída: {saida}")
        self.atualizar_interface(saida)
        if self.estado_atual == 's0' and entrada == 'b':
            messagebox.showinfo("Info", "Máquina reiniciada, pronta para nova operação.")

if __name__ == "__main__":
    app = MaquinaDeVenda()
    app.mainloop()
