#Script em python que tem todas as atividades passadas em aula de "Pensamento Computacional" do 1º Semestre.
#Libs usadas
import math
import math

#Nível Básico
#21.08.24
def Login():
#Elabore um programa que verifica se o usuário digitou a senha correta. Mostre a mensagem "senha incorreta" ou "Acesso liberado". Supondo que a senha correta seja 123.
    Senha = '123'

    login = str(input('Digite a senha: '))

    if login == Senha:
        print('Acesso liberado.')
    else:
        print('Acesso Negado.')

def MaiorQCem():
#Faça um programa que leia um valor numérico e mostre uma mensagem
    num1 = float(input('Digite o numero: '))

    if (num1 >= 100):
        print ('número maior que cem')

    elif (num1 <= 100):
        print ('numero é menor que cem')

    elif (num1 == 100):
        print ('os dois sao iguais')
    else:
        print('digire o número')

def NumerosIguais():
#Faça um programa que leia dois valores quaisquer e mostre o maior deles ou mostre a mensagem "os valores são iguas"
    num1 = float(input('primeiro numero: '))
    num2 = float(input('Segundo numero: ' ))

    if (num2 > num1):
        print ('segundo numero é maior que o primeiro numero')

    if (num1 > num2):
        print ('primeiro numero é maior que o segundo numero')

    if (num1 == num2):
        print ('os dois sao iguais')

def NecessidadeDAgua():
# A água é um nutriente essencial. sem ela, o corpo não pode funcionar com perfeição. Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo. A dose ideal, ou seja, a necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.
    kg = float(input('Quantos quilos você tem?: '))
    cal = kg * 0.03
    print(f'Você precisa tomar {cal} litros de água')

def ImparPar():
#Elabore um programa que verifica se o valor inteiro fornecido pelo usuário é impar ou par.;
    num = int(input('Digite um número: '))

    if (num%2) == 0:
        resto = num%2
        print(f"Par (número {num} e seu resto é: {resto})")
    else:
        print("Ímpar")

def AprovadoReprovado():
#Programa que calcule a média aritmética de um aluno que realizou duas avaliações. Além do valor da média, inclua na tela de saída uma das mensagens: "Aluno aprovado" ou "Aluno reprovado". Considere que o aluno será aprovado com a média maior ou igual a 5.

    nota = int(input('Digite a nota do aluno: '))
    nota2 = int(input('Digite a segunda nota do aluno: '))

    media = (nota + nota2)/2

    if (media >= 5):
        print ('APROVADO')

    elif (media <= 5):
        print ('REPROVADO')

    elif (media == 5):
        print ('APROVADO')
    else:
        print('digite o número')
#28.08.24
def ValorDVenda():
#Recebe os valores de compra e de venda, lê os valores, converta para float e atribui à variavel.
    vl_compra = float(input('Digite o valor de compra: '))
    vl_venda = float(input('Digite o valor de venda: '))
    if vl_compra < vl_venda:
        print(f'Lucro, o valor da compra foi {vl_compra} e o valor da venda foi {vl_venda}, lucro foi de {vl_venda - vl_compra}')
    elif vl_compra > vl_venda:
        print(f'Prejuízo. o valor da compra foi {vl_compra} e o valor da venda foi {vl_venda}, o valor de prejuízo foi de {vl_compra - vl_venda}')
    else:
        print('Empate')
    
def AnoDeNascimento():
#Calcule o programa que leia o ano de nascimento de uma pessoa e mostre se ela tem idade para votar (16 anos ou mais). Mostre a imagem informando a situação.
    idade = int(input('Digite a sua idade: '))
    if (idade >= 16 and idade <= 17):
        print(f'Você tem {idade} anos, pode votar')
    elif idade >= 18:
        print(f'Você tem {idade} anos, pode votar e tirar CNH')
    else:
        print(f'Você tem {idade} anos, não pode votar')
        
def CalculoRaiz():
# Projete o programa que calcule as raízes de uma equação do segundo grau. O usuário fornecerá os valores dos coeficientes a, b e c. Levando em consideração  a análise da existencia de raízes nos reais.; Se delta for igual a zero, existem duas raízes iguais; se delta for igual a zero, existem duas raízes iguais; se delta for maior que zero, existem duas raizes reais e distintas. 
    a = float(input("Digite o valor do coeficiente a: "))
    b = float(input("Digite o valor do coeficiente b: "))
    c = float(input("Digite o valor do coeficiente c: "))

    delta = b**2 - 4*a*c
    print(delta)
    if (a == 0 or b == 0 or c == 0):
        print("O coeficiente a não pode ser zero.")
    elif delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são {raiz1} e {raiz2}")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz dupla: {raiz}")
    else:
        print("A equação não possui raízes reais.")
#11.09.24
def MenorValor():
    vmaior = -999999
    vmenor = 999999
    contador = 0
    soma = 0
    while True:
        valor = int(input('Digite o valor, 0 para sair: '))
        if valor == 0:
            break
        contador += 1
        soma += valor
        if valor < vmenor:
            vmenor = valor
        if valor > vmaior:
            vmaior = valor
    print('o maior valor inserido:', vmaior)
    print('o menor valor é:', vmenor)
    print('Você inseriu', contador, 'números.')
    print('a soma de tudo é:', soma)
    print('a média de tudo é:', soma / contador)

def AlturaEGenero():
    #Elabore o programa que leia a altura e o genero ("m" para masculino e "f" para feminino) de um grupo de pessoas. Gere a tela de saida com maior altura do grupo (de todas as pessoas), quantidade de homens e mulheres.
    altura = 0
    maior_altura = 0
    qtd_homens = 0
    qtd_mulheres = 0
    while True:
        altura = float(input('Digite a altura em metros: '))
        if altura == 0:
            break
        genero = input('Digite o genero (m/f): ')
        if altura > maior_altura:
            maior_altura = altura
        if genero == 'm':
            qtd_homens += 1
        elif genero == 'f':
            qtd_mulheres += 1
    print('A maior altura do grupo é:', maior_altura)
    print('Quantidade de homens:', qtd_homens)
    print('Quantidade de mulheres:', qtd_mulheres)
#25.09.24
def Range():
    for i in range(11):
        print(i, end=' ')

def RangeA():
    for i in range(1, 11):
        print(i, end='     ')

def RangeB():
    for i in range(10):
        print(i, end=',')

def RangeC():
    for i in range(10):
        print(i, end=',')
    print(i +1 , '.')

def RangeD():
    for i in range(2, 13, 2): 
        print(i, end=' ')

def RangeE():
    for i in range(1, 14, 2):
        print(i, end=' ')

def RangeF():
    for i in range(7, -1, -1):
        print(i, end=' ')

def RangeG():
    somador = 0
    for i in range(10, 0, -1):
        print(i, end=' ')
        somador += i
    print("\nSoma da sequência:", somador)

def RangeH():
    inicio = int(input("Digite o valor inicial da sequência: "))
    fim = int(input("Digite o valor final da sequência: "))
    
    for num in range(inicio, fim, -1):
        print(num, end=' ')



#Run
RangeH()


#Avaliações Práticas - Básico 1º Semestre
#Avaliação Prática 1
def Avaliacao_Pratica_1A():
#A) Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
    raio = float(input('Digite o raio R : '))
    volume = (4/3) * 3.14 * (raio**2)

    print(f"O volume da efera de raio R {raio} é igual à: {volume:.2f}")

def Avaliacao_Pratica_1B():
#B) Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles.
    def calcular_distancia(x1, y1, x2, y2):
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia

    x1 = float(input("Digite a coordenada x1 de P: "))
    y1 = float(input("Digite a coordenada y1 de P: "))
    x2 = float(input("Digite a coordenada x2 de Q: "))
    y2 = float(input("Digite a coordenada y2 de Q: "))

    distancia = calcular_distancia(x1, y1, x2, y2)

    print(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é {distancia:.2f}")

def Avaliacao_Pratica_1C(): 
# C) Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário.
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    if valor1 < valor2:
        print(f"A ordem crescente dos valores é: {valor1}, {valor2}")
    elif valor1 > valor2:
        print(f"A ordem crescente dos valores é: {valor2}, {valor1}")
    else:
        print("Os valores são iguais.")

def Avaliacao_Pratica_1D():
#D) Construa o programa que calcule o peso ideal de uma pessoa.
# Utilize as seguintes fórmulas:
#- Se homem, o peso ideal é calculado assim: (72,7 . altura) - 58;
#- Se mulher, o peso ideal é calculado assim: (62,1 . altura) - 44,7.
#Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar).

    sexo = input("Digite o sexo (M para homem, F para mulher): ")
    altura = float(input("Digite a altura em metros: "))

    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido.")
        return

    print(f"O peso ideal para uma pessoa do sexo {sexo} com altura {altura} é {peso_ideal:.2f} kg")

#Avaliação Prática 2
def Avaliacao_Pratica_2A():
    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))
    valor3 = float(input("Insira o terceiro valor: "))
    valormax = max(valor1, valor2, valor3)
    print("O maior valor é:", valormax)

def Avaliacao_Pratica_2B():
    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))
    valor3 = float(input("Insira o terceiro valor: "))

    if valor1 >= valor2 and valor1 >= valor3:
        valormax = valor1
    elif valor2 >= valor1 and valor2 >= valor3:
        valormax = valor2
    else:
        valormax = valor3
    print("O maior valor é:", valormax)

def Avaliacao_Pratica_2C():
    print('''
░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░█▀▄░█▀█░█▀▄░█▀█
░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░█░█░█░█░█▀▄░█▀█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀░▀
''')
    print('Menu:\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n[5]Sair')
    escolha = int(input('Escolha: '))

    if escolha == 1:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 + n2)
    elif escolha == 2:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 - n2)
    elif escolha == 3:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 * n2)
    elif escolha == 4:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 / n2)
    elif escolha == 5:
        print('bye bye')