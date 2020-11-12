set style fill pattern 4 transparent
set terminal postscript
set samples 1000
set xrange[-10:10]
set output "trapezioo.eps"

f(x) = sin(x)*x
I0(x) = (x-(-5))*(f(-3.33333) - f(-5))/(-3.33333-(-5)) + f(-5)
I1(x) = (x-(-3.33333))*(f(-1.66666) - f(-3.33333))/(-1.66666-(-3.33333)) + f(-3.33333)
I2(x) = (x-(-1.66666))*(f(0) - f(-1.66666))/(0-(-1.66666)) + f(-1.66666)
I3(x) = (x-0)*(f(1.66666) - f(0))/(1.66666-0) + f(0)
I4(x) = (x-1.66666)*(f(3.33333) - f(1.66666))/(3.33333-1.66666) + f(1.66666)
I5(x) = (x-3.33333)*(f(5) - f(3.33333))/(5-3.33333) + f(3.33333)

plot 0 lc 0, sin(x)*x, x >= -5 && x <= -3.33333 ? I0(x) : 0/0 with filledcurve y1=0 title 'I0', x >= -3.33333 && x <= -1.66666 ? I1(x) : 0/0 with filledcurve y1=0 title 'I1', x >= -1.66666 && x <= 0 ? I2(x) : 0/0 with filledcurve y1=0 title 'I2', x >= 0 && x <= 1.66666 ? I3(x) : 0/0 with filledcurve y1=0 title 'I3', x >= 1.66666 && x <= 3.33333 ? I4(x) : 0/0 with filledcurve y1=0 title 'I4', x >= 3.33333 && x <= 5 ? I5(x) : 0/0 with filledcurve y1=0 title 'I5'
