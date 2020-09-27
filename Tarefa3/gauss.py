import math

class EliminacaoGauss:
	N = 0;
	matriz = [];
	matrizR = [];
	b = [];
	x = [];
	Ax = [];
	arquivo = None;

	def __init__(self, arquivo):
		self.arquivo = arquivo;
		self.lerArquivo(arquivo);

	def lerArquivo(self, str):
		arq = open(str, 'r');
		self.N = int(arq.readline());
		print(self.N);

		for i in range(self.N):
			linha = arq.readline().split(' ');
			for j in range(self.N+1):
				linha[j] = float(linha[j]);
			self.matriz.append(linha[0: self.N+1]);

		self.matrizR = self.matriz;
		self.x = [None]*(self.N);
		self.set_b();

		arq.close();

	def set_b(self):
		[self.b.append(linha[-1]) for linha in self.matriz];
		print(self.b);

	def eliminacao(self, N, parcial):
		for passo in range(N-1):
			pivot = 0;
			ip = 0;

			if(parcial==1):
				for ipivot in range(passo, N):
					if(abs(self.matrizR[ipivot][passo]) > pivot):
						pivot = abs(self.matrizR[ipivot][passo]);
						ip = ipivot;

				aux = self.matrizR[passo];
				self.matrizR[passo] = self.matrizR[ip];
				self.matrizR[ip] = aux;
			else:
				pivot = self.matrizR[passo][passo];

			for ipasso in range(passo+1, N):
				m = self.matrizR[ipasso][passo] / pivot;

				for j_op in range(N+1):
					self.matrizR[ipasso][j_op] = self.matrizR[ipasso][j_op] - m*self.matrizR[passo][j_op];

		print("*********************************************************")
		for i in range(self.N):
			for j in range(self.N+1):
				print(self.matrizR[i][j], end = " ");
			print();
		print("*********************************************************\n\n");
		self.calcular_x();

	def calcular_x(self):
		fst_X = self.matrizR[self.N-1][self.N]/self.matrizR[self.N-1][self.N-1];
		self.x[self.N-1] = fst_X;

		for i in range(self.N-2, -1, -1):
			soma = 0;
			for j in range(i+1, self.N):
				soma += self.matrizR[i][j] * self.x[j];

			xi = (self.matrizR[i][self.N] - soma)/self.matrizR[i][i];
			self.x[i] = xi;

		print(self.x);

	def resetMatriz(self):
		self.matriz = [];
		self.matrizR = [];
		self.b = [];
		self.x = [];
		self.Ax = [];
		self.lerArquivo(self.arquivo);


#m1 = EliminacaoGauss("m1.in");
#m1.eliminacao(m1.N, 0);
#m1.resetMatriz();
#m1.eliminacao(m1.N, 1);

m2 = EliminacaoGauss("m2.in");
m2.eliminacao(m2.N, 0);
m2.resetMatriz();
m2.eliminacao(m2.N, 1);

#m3 = EliminacaoGauss("m3.in");
#m3.eliminacao(m3.N, 0);
#m3.resetMatriz();
#m3.eliminacao(m3.N, 1);