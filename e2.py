def contavogais(frase):
    vogais='aeiouAEIOU'
    contador=sum(1 for letra in frase if letra in vogais)
    return contador

frase=input('Digite uma frase: ')

vogaistotais=contavogais(frase)

print(f'Número de vogais: {vogaistotais}')
