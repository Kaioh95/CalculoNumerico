set style fill transparent
set terminal eps
set samples 1000
set xrange[-10:10]
set output "simpson13.eps"

f(x) = sin(x)*x
f_1(x_0, x_1) = (f(x_1) - f(x_0)) / (x_1 - x_0)
f_2(x_0, x_1, x_2) = (f_1(x_1, x_2) - f_1(x_0, x_1))/(x_2 - x_0)

I0(x) = f(-5) + (x - (-5))*f_1(-5, -3.33333) + (x - (-5))*(x - (-3.33333))*f_2(-5, -3.33333, -1.66666)
I1(x) = f(-1.66666) + (x - (-1.66666))*f_1(-1.66666, 0) + (x - (-1.66666))*(x - 0)*f_2(-1.66666, 0, 1.66666)
I2(x) = f(1.66666) + (x - 1.66666)*f_1(1.66666, 3.33333) + (x - 1.66666)*(x - 3.33333)*f_2(1.66666, 3.33333, 5)

plot 0 lc 0, sin(x)*x, x >= -5 && x <= -1.66666 ? I0(x) : 0/0 with filledcurve y1=0 title 'I0', x >= -1.66666 && x <= 1.66666 ? I1(x) : 0/0 with filledcurve y1=0 title 'I1', x >= 1.66666 && x <= 5 ? I2(x) : 0/0 with filledcurve y1=0 title 'I2'
