import math

N = 0;
matriz = [];

def lerArquivo(str):
	arq = open(str, 'r');
	N = int(arq.readline());

	for i in range(N):
		linha = arq.readline().split(' ');
		for j in range(N+1):
			linha[j] = float(linha[j]);
		matriz.append(linha);


	arq.close();
	return N;

def eliminacao(N, parcial):
	for passo in range(N-1):
		pivot = 0;
		ip = 0;

		if(parcial==1):
			for ipivot in range(passo, N):
				if(abs(matriz[ipivot][passo]) > pivot):
					pivot = abs(matriz[ipivot][passo])
					ip = ipivot;

			aux = matriz[passo];
			matriz[passo] = matriz[ip];
			matriz[ip] = aux;
		else:
			pivot = matriz[passo][passo]

		for ipasso in range(passo+1, N):
			m = matriz[ipasso][passo] / pivot;

			for j_op in range(N+1):
				matriz[ipasso][j_op] = matriz[ipasso][j_op] - m*matriz[passo][j_op];


N = lerArquivo("m2.in");	
eliminacao(N, 0);
print("*********************************************************")
for i in range(N):
	for j in range(N+1):
		print(matriz[i][j], end = " ");
	print();
print("*********************************************************\n\n");
