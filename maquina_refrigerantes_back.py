# Alfabeto
I = ['m25','m50','m100','b']
# Tabela de estados
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

def proximo_estado(estado, entrada):
    if entrada not in I:
        return ("Entrada inválida", None)
    return T.get((estado, entrada), ("Transição não definida", None))

def inicia_maquina():
    estado_atual = 's0'
    while True:
        try:
            entradas = input("Insira uma moeda (m25, m50, m100) ou 'b' para comprar, seprado por virgulas: ").split(",")
            for entrada in entradas:
                estado_atual, saida = proximo_estado(estado_atual, entrada)
                print(f"Entrada: {entrada}, Próximo estado: {estado_atual}, Saída: {saida}")
                if estado_atual == 's0' and entrada == 'b':
                    print("Máquina reiniciada, pronta para nova operação.")
                    break
        except KeyboardInterrupt:
            print("\nProcesso encerrado pelo usuário.")
            break

inicia_maquina()