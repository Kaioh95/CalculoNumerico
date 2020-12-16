reset
set terminal eps
set output "barco.eps"
set xtics 1
set ytics 1
set samples 5000
set style fill pattern 5
set xzeroaxis
set yzeroaxis
set grid

p(x) = 376.0255756310777 - 75.88511802780468*x + 3.8645661987598308*x*x

plot "barco.pts" with dots, p(x)
