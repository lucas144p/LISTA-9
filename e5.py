reais=float(input('Valor em reais (R$): '))
cotacaodolar=float(input("Digite a cotação atual do dólar: "))

dolares=reais/cotacaodolar

print(f'Você pode comprar US$ {dolares:.2f}, com R$ {reais:.2f}')
