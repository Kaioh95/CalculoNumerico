reset
set terminal eps
set output "imagem.eps"
set xrange[-1.5:2.5]
set yrange[-7:8]
set xtics 1
set ytics 1
set samples 1000
set style fill pattern 5
set xzeroaxis
set yzeroaxis
set grid
f(x) = x**3-2*x**2-x+2
g(x) = 2.1126
h(x) = -0.6311
plot f(x) title "funcao cubica",\
-2*x+2,\
"pts1_1.pts",\
g(x),\
h(x)

