reset
set terminal eps
set output "sTaylor.eps"
set xrange[-10:10]
set yrange[-10:10]
set xtics 1
set ytics 1
set samples 1000
set style fill pattern 5
set xzeroaxis
set yzeroaxis
set grid

fac(n) = (n==0) ? 1 : n*fac(n-1)

hf(x, i) = (i%2 != 0) ? (-1)**((i-1)/2)*i*cos(x) + (-1)**((i+1)/2)*x*sin(x) : (-1)**(i/2)*i*sin(x) + (-1)**(i/2)*x*cos(x)

f(x) = sum [i=0:100] hf(0, i)*(x**i)/fac(i)
plot f(x) title "f(x)", x*cos(x)+1 lw 2 lc 0
