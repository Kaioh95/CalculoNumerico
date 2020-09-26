#include <stdio.h>
#include <math.h>

#define s0 300
#define g 32.17
#define m 0.25
#define k 0.1

double s(double t);
double secante(double p0, double p1, double tol);

double s(double t){
	return s0 - ((m*g)/k)*t + ((m*m*g)/(k*k)) * (1-exp(-k*t/m));
}

double secante(double p0, double p1, double tol){
	double q0 = s(p0);
	double q1 = s(p1);
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
		q1 = s(p);
                count += 1;
        }

        printf("Secante: Apos %d iteracoes temos, %lf como uma aproximacao da raiz\n", count, p);
        return p;
}


int main(void){
        double a, r, tol;

        printf("Digite um ponto e o erro: ");
        scanf("%lf %lf", &a, &tol);
	r = secante(a, a+0.00001, tol);
	printf("f(%lf) = %lf\n", r , s(r));

        return 0;
}
