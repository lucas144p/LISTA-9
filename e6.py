nums=[]
for i in range(10):
    num=int(input(f'Digite o {i+1}º número inteiro: '))
    nums.append(num)

pares=[]
impares=[]
for n in nums:
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Quantidade de números pares: {len(pares)}')
print(f'Quantidade de números ímpares: {len(impares)}')