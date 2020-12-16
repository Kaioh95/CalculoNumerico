import math
import copy

class EliminacaoGauss:

	def __init__(self, arquivo):
		self.N = 0;
		self.matriz = [];
		self.matrizR = [];
		self.b = [];
		self.x = [];
		self.Ax = [];
		self.residuo = [];
		self.arquivo = arquivo;
		self.lerArquivo(arquivo);

	def lerArquivo(self, str, ref=0):
		arq = open(str, 'r');
		self.N = int(arq.readline());

		for i in range(self.N):
			linha = arq.readline().split(' ');
			for j in range(self.N+1):
				linha[j] = float(linha[j]);
			self.matriz.append(linha[0: self.N+1]);

		self.matrizR = copy.deepcopy(self.matriz);
		if(ref == 0):
			self.x = [None]*(self.N);
		self.set_b();

		arq.close();

	def set_b(self):
		print("*********************************************************");
		#print("Vetor b:");
		[self.b.append(linha[-1]) for linha in self.matriz];
		#print(self.b);

	def eliminacao(self, N, parcial, ref = 0):
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

		#print("\n Matriz apos a eliminacao: ");
		#for i in range(self.N):
		#	for j in range(self.N+1):
		#		print(self.matrizR[i][j], end = " ");
		#	print();
		self.calcular_x(ref);

	def calcular_x(self, ref):
		fst_X = self.matrizR[self.N-1][self.N]/self.matrizR[self.N-1][self.N-1];
		self.x[self.N-1] = fst_X;

		for i in range(self.N-2, -1, -1):
			soma = 0;
			for j in range(i+1, self.N):
				soma += self.matrizR[i][j] * self.x[j];

			xi = (self.matrizR[i][self.N] - soma)/self.matrizR[i][i];
			if(ref == 1):
				self.x[i] += xi;
			else:
				self.x[i] = xi;

		print("\nVetor x:");
		print(self.x);
		self.calcularVetorResiduo();
 
	def calcularVetorResiduo(self):
		soma = 0;

		for i in range(self.N):
			for j in range(self.N):
				soma += self.matriz[i][j]*self.x[j];
			self.Ax.append(soma);
			soma = 0;
			self.residuo.append(self.b[i] - self.Ax[i]);

		#print("\nVetor Residuo: ");
		#print(self.residuo);
		#print("*********************************************************\n\n");

	def calcularNorma(self):
		soma = math.fsum([math.pow(valor, 2) for valor in self.residuo]);
		print("\nNorma do vetor residual: ");
		print(math.sqrt(soma));
		print("*********************************************************\n\n");

	def resetMatriz(self):
		self.matriz = [];
		self.matrizR = [];
		self.b = [];
		self.x = [];
		self.Ax = [];
		self.residuo = [];
		self.lerArquivo(self.arquivo);

	def refReset(self):
		self.matriz = [];
		self.matrizR = [];
		self.b = [];
		#self.x = [];
		self.Ax = [];
		self.residuo = [];
		self.lerArquivo(self.arquivo, 1);


def refinamento(elGauss, totalIteracoes, pivotamento):
	r = copy.deepcopy(elGauss.residuo);
	n = elGauss.N;
	elGauss.refReset();

	for nIteracoes in range(totalIteracoes):
		print("Iteracao numero", nIteracoes+1);

		# Nova matriz Ay=r
		for i in range(n):
			elGauss.matriz[i][-1] = r[i];
			elGauss.matrizR[i][-1] = r[i];
		elGauss.set_b();
		elGauss.eliminacao(elGauss.N, pivotamento, 1);
		
		elGauss.calcularNorma();
		r = copy.deepcopy(elGauss.residuo);
		n = elGauss.N;
		elGauss.refReset();

print("Arquivo m1");
m1 = EliminacaoGauss("m1.in");
print("Sem pivotamento parcial: ");
m1.eliminacao(m1.N, 0);
m1.calcularNorma();
#refinamento(m1, 150, 0);

print("Arquivo m4");
m4 = EliminacaoGauss("m4.in");
print("Com pivotamento parcial: ");
m4.eliminacao(m4.N, 1);
m4.calcularNorma();
#refinamento(m4, 150, 1);

print("Arquivo m5");
m5 = EliminacaoGauss("m5.in");
print("Sem pivotamento parcial: ");
m5.eliminacao(m5.N, 0);
m5.calcularNorma();
#refinamento(m5, 40, 0);

