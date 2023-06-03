def calculo_da_refeicao(preco_do_quilo, tara_prato, peso_da_refeicao):
    peso_liquido = peso_da_refeicao - tara_prato
    preco_da_refeicao = preco_do_quilo * peso_liquido
    return f"Um prato no peso de {peso_da_refeicao}g, vai ficar em um valor total de: R${preco_da_refeicao:.2f}"

while True:
    try:
        preco_do_quilo = float(input('Digite o preço do quilo: '))
        break
    except ValueError:
        print("Digite um valor, válido para preço do quilo.")


while True:
    try:
        tara_prato = float(input('Digite o peso da tara do prato (digite o valor em kg): '))
        valor_em_gramas = tara_prato / 1000
        break
    except ValueError:
        print("Digite um valor válido para o peso da tara do prato.")

while True:
    try:
        peso_da_refeicao = float(input('Digite o peso do refeição (digite o em kg): '))
        valor_em_gramas_da_refeicao = peso_da_refeicao * 1000
        mensagem = f"O prato de {valor_em_gramas_da_refeicao:.0f} gramas custa: R${(preco_do_quilo * (peso_da_refeicao - valor_em_gramas)):.2f}"
        print(mensagem)
        break
    except ValueError:
        print("Digite um valor válido para o peso da refeição.")