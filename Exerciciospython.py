'''exercício 1 - 1. Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.'''

numero1 = float(input("me do o primeiro numero"))
numero2 = float(input("me do o segundo numero"))

if numero1 > numero2:
    print("o primeiro número é maior")
if numero1 == numero2:
    print("os numeros são iguais")
else:
    print("o segundo número é maior")

'''exercicio 2 - Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano
(não é necessário considerar o mês em que ela nasceu).'''

nascimento = float(input("me diga seu ano de nascimento"))
if nascimento <= 2007:
    print("Parabens, você pode votar")
else:
    print("você não pode votar")


'''exercicio 3 - Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234.
Devem ser impressas as seguintes mensagens:

ACESSO PERMITIDO caso a senha seja válida.

ACESSO NEGADO caso a senha seja inválida.'''

senha = input("digite sua senha com 4 dígitos:")

if senha == "1234":
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

'''exercicio 4 - As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze.
Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.'''

qtdmaca = int(input("quantas maçãs você quer comprar"))
if qtdmaca < 12:
    print(f"Você irá pagar {qtdmaca * 0.30} nas maçãs e 0,30 por maçã")
else: print(f"Você irá pagar {qtdmaca * 0.25} nas maçãs e 0,25 pro maçã")

'''exercício 5 - Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.'''

valor1 = int(input("Me fale um valor"))
valor2 = int(input("Me fale outro valor"))
valor3 = int(input("Me fale mais um valor"))

numeromaior = valor1 > valor2
print(numeromaior)
numeromeio = valor1 > valor3
print(numeromeio)
numerofinal = valor3 > valor2
print(numerofinal)

if valor1 > valor2 > valor3:
    print(f"{valor1} > {valor2} > {valor3}")
elif valor2 > valor1 > valor3:
    print(f"{valor2} > {valor1} > {valor3}")
elif valor3 > valor1 and valor2:
    print(f"{valor3} > {valor1} > {valor2}")






'''6. Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule
e imprima seu peso ideal, utilizando as seguintes

Fórmulas:
- para homens: (72.7 * Altura) - 58
para mulheres: (62.1 * Altura) - 44.7

7. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área
Se o número de lados for igual a 5 escrever PENTÁGONO.

8. Adicione as seguintes mensagens à solução do exercício anterior conforme o caso.
Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

9. Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
Considere que o usuário não informará valores iguais.

10. Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isóscele: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.

11. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)'''