#include <stdio.h>
#include <math.h>

#define A 8
#define x1 20 
#define x2 30

double f(double L);
double bisec(double a, double b, double tol);

double f(double L){
	return 1.0/(sqrt(x2*x2 - L*L)) + 1.0/(sqrt(x1*x1 - L*L)) - 1.0/A;
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



int main(void){
        double a, b, r, tol;

        printf("Digite um ponto e o erro: ");
        scanf("%lf %lf %lf", &a, &b, &tol);
	r = bisec(a, b, tol);
	printf("f(%lf) = %lf\n", r , f(r));

        return 0;
}