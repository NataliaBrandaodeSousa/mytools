#Esse arquivo ele só define funções e constantes

#string que representa as 100 primeiras casas decimais do número pi
PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

#string que representa as 100 primeiras casas decimais do número neperiano
E_INT = "7182818284590452353602874713526624977572524413243165414564852932174670892742421803113962602491412737"

#Uma função chamada pi_real que dado um número natural N maior que 0 e menor que 100 que retorna uma string
#de uma aproximação pro número pi com N casa decimais
def pi_real(N):
    v = PI_INT[0: N]
    return "3" + "," + v

#print(pi_real(3))

#análogo a função de cima
def e_real(M):
    k = E_INT[0: M]
    return "2" + "," + k

#print(e_real(3))
