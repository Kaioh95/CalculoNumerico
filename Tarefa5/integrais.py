import math

def f(x):
	return x*math.sin(x);

def trapezio(funcao, a, b, numeroPontos):
	h = (b-a)/(numeroPontos-1);
	somaFirstLast = funcao(a) + funcao(b);
	somaMeio = 0;

	for i in range(1, numeroPontos-1):
		ponto = a + i*h;
		somaMeio += funcao(ponto);
		#print(i, ponto);

	return (somaFirstLast + 2*somaMeio)*(h/2);


def simpson13(funcao, a, b, numeroPontos):
	h = (b-a)/(numeroPontos-1);
	somaFirstLast = funcao(a) + funcao(b);
	somai2 = 0;
	somai1 = 0;

	for i in range(1, numeroPontos-1):
		ponto = a + i*h;

		if(i%2!=0):
			somai1 += funcao(ponto);
		else:
			somai2 += funcao(ponto);
		#print(i, ponto);

	return (somaFirstLast + 4*somai1 + 2*somai2)*(h/3);

def simpson38(funcao, a, b, numeroPontos):
	h = (b-a)/(numeroPontos-1);
	somaFirstLast = funcao(a) + funcao(b);
	somaiMult3 = 0;
	somai = 0;

	for i in range(1, numeroPontos-1):
		ponto = a + i*h;

		if(i%3==0):
			somaiMult3 += funcao(ponto);
		else:
			somai += funcao(ponto);
		#print(i, ponto);

	return (somaFirstLast + 2*somaiMult3 + 3*somai)*(3*h/8);


print(trapezio(f, -5, 5, 37));
print(simpson13(f, -5, 5, 37));
print(simpson38(f, -5, 5, 37));