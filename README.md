# A Caixa Potencial
Um código escrito em python para solucionar potenciação simples

Esse projeto faz parte de uma pesquisa pessoal que visa criar sistemas que possam solucionar diferentes equaçoes, sendo essas das mais simples ate as mais complexas. 
# Sobre potenciação

A potenciação é uma operaçao matematica que representa a multiplicaçao de fatores iguais, sendo a potencia considerada como valor de N e a base A. 

sua forma de resoluçao mais simples é a multiplicaçao sucessiva de fatores iguais onde: 

A^n (A elevado a N) = A.A.A....

2^3 = 2.2.2 = 8. 

# Por dentro do Código

A linha que faz a operaçao basica de potenciação segue os mesmos padrões do calculo acima. Logo temos: 

1º O usuario coloca os valores desejados

potencia = int(input('Digite o valor da potencia: '))
base = int(input('Digite o valor da base: '))

2º Com os valores da linha acima temos o calculo: 

resp = base**potencia

# Regra de 0 e 1. 

Subsutituindo o If por matchcase temos a seguinte condição:
match potencia: 
  case '1': 
    print ('o valor é: ',base)
  case '0':
    print ('O valor é: 1')


Acima temos uma representaçao escrita incluida também no código fonte da caixa potencial, onde toda potência com expoente igual a zero, o resultado será 1. 
E também toda potencia com expoente igual a 1, o resultado sera a propria base. 
    

