preco=float(input('Preço do produto: '))
valordesc=float(input('Porcentagem de desconto: '))

desc=valordesc/100
precototal=preco*desc

print(f'Preço do produto com desconto: R${precototal}')