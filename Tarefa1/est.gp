reset
set terminal eps
set output "aprox.eps"
set xrange[-10:10]
set yrange[-10:10]
set xtics 1
set ytics 1
set samples 1000
set style fill pattern 5
set xzeroaxis
set yzeroaxis
set grid

plot "arquivo.pts" with lp, x*cos(x)+1
