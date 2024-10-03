#codigo fonte da Caixa Potencial.


print ('CAIXA POTENCIAL ')
print ('''
A caixa potencial tem o objetivo de resolver questões simples de potenciação
A potenciação ou exponenciação é a operação matemática que representa a multiplicação de fatores iguais.
Ou seja, usamos a potenciação quando um número é multiplicado por ele mesmo várias vezes ''')

print ('Responda cada uma das perguntas abaixo...')

potencia = int(input('Qual o valor da potencia: '))
base = int(input('qual o valor da base: '))
resp = base**potencia

match potencia:
    case '1' :
        print ('o valor é ', base)
    case '0' :
        print ('O valor é 1')

print ('O valor e de ',resp)
print ('By SilverTech ')
