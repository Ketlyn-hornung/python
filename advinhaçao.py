#advinhaçao.py

import random
def jogar():

    print('*******************************')
    print('bem vindo ao jogo de advinhaçao')
    print('*******************************')

    numero_secreto=random.randrange(1,101)
    total_tentativas=0
    pontos=1000



    print('Qual o nivel de dificulade?')
    print('(1) Facil (2)Medio (3) Dificil')

    nivel=int(input('defina o nivel:'))

    if (nivel==1):
        total_tentativas=20
    elif(nivel==2):
         total_tentativas=10
    else:
        total_tentativas=5

    for tentativa in range(1, total_tentativas+1):
        print(f'tentativa{tentativa}de {total_tentativas}')
        chute=int(input('digite um numero entre 1 e 100:'))

        if(chute == numero_secreto):
            print('acertou')
            break
        
        else:
            pontos_perdidos= abs(numero_secreto-chute)
            if(chute>numero_secreto):
             print('Errou! seu chute foi maior que o numero secreto')
            else:
             print('Errou! seu chute foi menor que o numero secreto')

 print('***Fim de jogo***')
 print(f' O numero secreto era {numero_secreto}. Voce fez {pontos}pontos.')

if(__name__=='__main__'):
    jogar()
