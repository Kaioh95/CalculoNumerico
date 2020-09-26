#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

class EliminacaoGauss{
public:
	int N;
	string str;
	double **mat = NULL;

	//metodo
	EliminacaoGauss(){}

	EliminacaoGauss(string str){
		lerArquivo(str);
	}

	void lerArquivo(string str){
		ifstream arq;
		string linha;
		
		arq.open(str);
		if(arq.is_open()){
			
			int counti = 0;
			int countj = 0;

			getline(arq, linha);
			N = stod (linha);
			mat = new double *[N];
			
			for(int i = 0; i<N; i++){
				mat[i] = new double[N+1];
			}

			while(getline(arq, linha)){
				stringstream ss(linha);
				string token;
				while(getline(ss, token, ' ')){
					mat[counti][countj] = stod(token);
					countj++;
				}
				countj = 0;
				counti++;
			}
			arq.close();
		} 
		else{
			cout << "Falha ao abrir arquivo" << endl;
		}
	}

	void eliminar(){
		for(int i=0; i<N; i++){
			for(int j=0; j<=N; j++)
				cout << mat[i][j];
			cout << endl;
		}
	}

	~EliminacaoGauss(){
		for(int i=0; i<N; i++)
			delete[] mat[i];
	}

};

int main(int argc, char const *argv[]){

	EliminacaoGauss* EG = new EliminacaoGauss("m1.in");
	EG->eliminar();

	return 0;
}