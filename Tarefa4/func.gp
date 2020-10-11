reset
set terminal eps
set output "functions.eps"
set xrange[-4:20]
set yrange[-10:10]
set xtics 1
set ytics 1
set samples 1000
set style fill pattern 5
set xzeroaxis
set yzeroaxis
set grid

n(x) = (89*x*x*x-849*x*x+1762*x+420)/420
l(x) = (89*x*x*x-849*x*x+1762*x+420)/420

p1(x) = x >= 0 && x <= 2 ? x + 1 : 1/0
p2(x) = x >= 2 && x <= 4 ? -2*x + 7 : 1/0
p3(x) = x >= 4 && x <= 7 ? (5*x-23)/3 : 1/0

plot "pontos.pts", n(x) lw 3, l(x) lw 1, p1(x) lw 1, p2(x) lw 1, p3(x) lw 1
