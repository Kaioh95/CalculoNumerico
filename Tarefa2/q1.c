#include <stdio.h>
#include <math.h>

double f(double x);
double hf(double x);
double g(double x);
double bisec(double a, double b, double tol);
double fixPoint(double initPT, double tol);
double secante(double p0, double p1, double tol);
double regulaFalse(double p0, double p1, double tol);
double newton(double initPT, double tol);

double f(double x){
        return x*x*x-1.7*x*x-12.78*x-10.08;
}

double hf(double x){
	return 3*x*x-3.4*x-12.78;
}

double g(double x){
	return cbrt(1.7*x*x+12.78*x+10.08);
}

double bisec(double a, double b, double tol){
        double FA = f(a);
        double FP;
        double p;
	int count = 0;

        while((double)fabs(b-a) > tol){
                p = (b+a)/2;
                FP = f(p);

                if(FP==0 || (double)(b-a)/2 < tol){
                        printf("Bissecao: Apos %d iteracoes temos, %lf como raiz\n", count, p);
                        return p;
                }
                if(FA*FP > 0){
                        a = p;
                        FA = FP;
                }
                else{
                        b=p;
                }

                count += 1;
        }

        printf("Bissecao: Apos %d iteracoes temos, %lf como uma aproximacao da raiz\n", count, p);
	return p;
}

double fixPoint(double initPT, double tol){
	double p = g(initPT);
	int count = 0;

	while((double)fabs(p-initPT) >= tol){
		p = g(initPT);

		if((double)fabs(p-initPT) < tol || p == g(p)){
			printf("Fix Point: Apos %d iteracoes temos, %lf como raiz\n", count, p);			
			return p;
		}

		initPT = p;
		p = g(initPT);
		count += 1;
	}

	printf("Fix Point: Apos %d iteracoes temos, %lf como uma aproximacao da raiz\n", count, p);
        return p;

}

double newton(double initPT, double tol){
        double p = initPT - (double)f(initPT)/hf(initPT);
	double p0 = initPT;
        int count = 0;

        while((double)fabs(p-p0) >= tol){
                p = initPT - (double)f(initPT)/hf(initPT);
		p0 = initPT;

                if((double)fabs(p-p0) < tol){
                        printf("Newton: Apos %d iteracoes temos, %lf como raiz\n", count, p);
                        return p;
                }

                initPT = p;
                count += 1;
        }

        printf("Newton: Apos %d iteracoes temos, %lf como uma aproximacao da raiz\n", count, p);
        return p;

}

double secante(double p0, double p1, double tol){
	double q0 = f(p0);
	double q1 = f(p1);
        double p;
        int count = 0;

        while((double)fabs(p1-p0) >= tol){
                p = p1 - (double)q1*(p1-p0)/(q1-q0);

                if((double)fabs(p-p1) < tol){
                        printf("Secante: Apos %d iteracoes temos, %lf como raiz\n", count, p);
                        return p;
                }

                p0 = p1;
		p1 = p;
		q0 = q1;
		q1 = f(p);
                count += 1;
        }

        printf("Secante: Apos %d iteracoes temos, %lf como uma aproximacao da raiz\n", count, p);
        return p;

}

double regulaFalse(double p0, double p1, double tol){
        double q0 = f(p0);
        double q1 = f(p1);
        double p, q;
        int count = 0;

        while((double)fabs(p1-p0) >= tol){
                p = p1 - (double)q1*(p1-p0)/(q1-q0);

                if((double)fabs(p-p1) < tol){
                        printf("Ponto Falso: Apos %d iteracoes temos, %lf como raiz\n", count, p);
                        return p;
                }

		q = f(p);

		if(q*q1 < 0){
			p0 = p1;
			q0 = q1;
		}
                p1 = p;
                q1 = q;
                count += 1;
        }

        printf("Ponto Falso: Apos %d iteracoes temos, %lf como uma aproximacao da raiz\n", count, p);
        return p;

}


int main(void){
        double a, b, tol;

        printf("Digite a e b para [a, b] e o erro: ");
        scanf("%lf %lf %lf", &a, &b, &tol);
        bisec(a, b, tol);
	fixPoint(a, tol);
	newton(a, tol);
	secante(a, a+0.01, tol);
	regulaFalse(a, b, tol);

        return 0;
}