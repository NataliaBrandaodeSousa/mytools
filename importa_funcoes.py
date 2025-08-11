#Já esse arquivo usa as funções 

#pega o arquivo MYTOOLS e guarda as funções e constantes
import MYTOOLS

#puxando as fuções pra cá
f = MYTOOLS.e_real
g = MYTOOLS.pi_real

#numero escolhido pelo usuario
n = int(input())

print(f(n))
print(g(n))

#puxando as constantes pra cá
i = MYTOOLS.E_INT
j = MYTOOLS.PI_INT

print(i)
print(j)