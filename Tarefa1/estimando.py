import math

def hf(x):
	return math.cos(x)-x*math.sin(x)

def f(x, y, a):
	return y-hf(a)*(x-a)

alpha = 0
beta = 0

arquivo = open("arquivo.pts", 'w')

x_anterior = 0
y_anterior = 1
pontos_negativos = []

#Cálculo dos pontos no intervalo [-6:0] a partir do ponto ponto (0, f(x)).
while(beta >= -6):
	x_anterior = beta+0.1

	if(beta == 0):
		print("PONTO CONHECIDO")
		pontos_negativos.append(str(beta)+ " " + str(f(0, 1, beta)) + "\n")
		y_anterior = f(0, 1, beta)
	else:
		pontos_negativos.append(str(beta) + " " + str(f(x_anterior, y_anterior, beta)) + "\n") 
		y_anterior = f(x_anterior, y_anterior, beta)

	beta -= 0.1

#Escrita em ordem crescente
for i in reversed(pontos_negativos):
	arquivo.write(i)

x_anterior = 0
y_anterior = 1

#Cálculo dos pontos no intervalo [0:6] a partir do ponto ponto (0, f(x)).
while(alpha <= 6):
	x_anterior = alpha-0.1

	if(alpha == 0):
		print("PONTO CONHECIDO")
		y_anterior = f(0, 1, alpha)
	else:
		arquivo.write(str(alpha) + " " + str(f(x_anterior, y_anterior, alpha)) + "\n")
		y_anterior = f(x_anterior, y_anterior, alpha)

	alpha += 0.1

arquivo.close()