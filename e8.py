nomes=[]
for i in range(5):
    nome=input(f'Digite o {i+1}º nome:')
    nomes.append(nome)

nomesA=[]
for nome in nomes:
    # O 'nome.lower' deixa as letras dos nomes digitados minúsculas
    if nome.lower().startswith('a'): # O startswith('a') verifica se a string começa com 'a'
        nomesA.append(nome)

print(f"Quantidade de nomes que começam com 'A': {len(nomesA)}")