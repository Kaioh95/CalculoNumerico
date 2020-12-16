reset
set terminal eps
set output "pesos.eps"
set xtics 1
set ytics 1
set samples 5000
set style fill pattern 5
set xzeroaxis
set yzeroaxis
set ytics font 'arial, 8'
set grid

f(x) = -60.06608318746963 + 70.33368435736804*x

plot "pesos.pts" with dots, f(x)
