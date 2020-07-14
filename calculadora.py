#função: Realizar operações básicas como adição, subtração, multiplicação e divisão
#autor: João Cândido

#definir função
def calculate():
    operação = input('''
Por favor digite a operação matemática que você deseja concluir:
+ for adição
- for subtração
* for multiplicação
/ for divisão
''')

    number_1 = int(input('entre seu primeiro número: ') )
    number_2 = int(input('entre seu segundo número: ') )

    #adição

    if operação == '+':
        print ('{} + {} = '.format (number_1, number_2))
        print (number_1 + number_2)

    #subtração

    elif operação == '-':
        print ('{} - {} = '.format (number_1, number_2))
        print (number_1 - number_2)

    #multiplicação

    elif operação == '*':
        print ('{} * {} = '.format (number_1, number_2))
        print (number_1 * number_2)

    #divisão

    elif operação == '/':
        print ('{} / {} = '.format (number_1, number_2))
        print (number_1 / number_2)

    else:
	    print('Você não digitou um operador válido, execute o programa novamente.')

    #adicionar novamente
    again ()

#para calcular novamente

def again():
    calc_again = input('''
Você quer calcular novamente?
Por favor digite S para sim ou N para não.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()

calculate()





