# EXERCÍCIO 1: Montar um lanche personalizado
# 
# Crie funções para:
# - escolher o pão (ex: integral, francês, brioche)
# - escolher a carne (ex: frango, boi, vegetariano)
# - escolher os acompanhamentos (ex: alface, tomate, bacon)
# - montar_lanche(pão, carne, *acompanhamentos)
#
# A ideia é que o usuário consiga montar um lanche completo passando os ingredientes como parâmetros.
# Depois, imprima uma descrição do lanche montado.

def escolher_pao(tipo_do_pao):
    print(f"Pão escolhido > {tipo_do_pao}")

def escolher_carne(tipo_carne):
    print(f"Carne escolhida > {tipo_carne}")

def escolher_acompanhaento(salada, queijo):
    print(f"Salada > {salada}. Queijo> {queijo}.")

def lanche_montado(tipo_do_pao, tipo_carne, salada, queijo):
    escolher_pao(tipo_do_pao)
    escolher_carne(tipo_carne)
    escolher_acompanhaento(salada, queijo)

pao_escolhido = input("Qual nome do seu pão: ")
carne_escolhida = input("Nome da carne: ")
salada_escolhida = input("Tipo de salada: ")
queijo_escolhido = input("Tipo de queijo: ")

lanche_montado(pao_escolhido, carne_escolhida, salada_escolhida, queijo_escolhido)


# EXERCÍCIO 2: Montar uma viagem personalizada
#
# Crie funções para:
# - escolher o destino (ex: praia, montanha, cidade)
# - escolher o meio de transporte (ex: carro, avião, ônibus)
# - escolher os itens da mala (ex: roupa, protetor solar, óculos de sol)
# - montar_viagem(destino, transporte, *itens_mala)
#
# A ideia é permitir que o usuário monte uma viagem completa informando
# o destino, o transporte e os itens que deseja levar na mala.
# Depois, o programa deve imprimir uma descrição completa da viagem.


def escolher_destino(destino):
    print(f"Destino escolhido > {destino}")

def escolher_meio_de_transporte(transporte):
    print(f"Meio de transporte escolhido > {transporte}")

def escolher_itens(itens):
    print("Itens que vai levar:")
    for item in itens:
        print(f"- {item}")

def montar_viagem(destino, transporte, itens):
    escolher_destino(destino)
    escolher_meio_de_transporte(transporte)
    escolher_itens(itens)

# Aqui entra o input
destino_usuario = input("Digite o destino da viagem: ")
transporte_usuario = input("Digite o meio de transporte: ")
itens_usuario = input("Digite os itens que vai levar, separados por vírgula: ").split(',')

# Remove espaços extras dos itens
itens_usuario = [item.strip() for item in itens_usuario]

montar_viagem(destino_usuario, transporte_usuario, itens_usuario)



# 🧪 EXERCÍCIO: Verificador de temperatura
#
# Crie uma função chamada verificar_temperatura que receba como parâmetro
# uma temperatura em graus Celsius. A função deve:
#
# - Imprimir "Está frio!" se a temperatura for menor que 18 °C.
# - Imprimir "Está agradável!" se a temperatura estiver entre 18 °C e 30 °C.
# - Imprimir "Está calor!" se a temperatura for maior que 30 °C.
#
# Além disso, crie uma função principal chamada mostrar_previsao()
# que chama a função verificar_temperatura() passando diferentes
# valores como exemplo (por exemplo: 15, 25 e 35).

def verificar_temperatura(temperatura):
    if temperatura < 18:
        print(f"{temperatura}, está FRIO!")
    elif 18 <= temperatura <= 30:
        print(f"{temperatura}, está AGRADÁVEL!")
    else:
        print(f"{temperatura}, está muito quente!")

def mostrar_previsao(temperatura):
    verificar_temperatura(temperatura)

# Aqui entra o input
temperatura_usuario = int(input("Digite a temperatura em graus Celsius: "))
mostrar_previsao(temperatura_usuario)
