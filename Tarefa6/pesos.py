arq = open("pesos.txt", 'r');

n = 0;
x_i = 0;
y_i = 0;
x2_i = 0;
xy_i = 0;

for line in arq:
	point = line.split(' ');
	x = float(point[0]);
	y = float(point[1]);
	
	n += 1;
	x_i += x;
	y_i += y;
	x2_i += x * x;
	xy_i += x * y;
arq.close();
	
print("n:", n, "xi:", x_i, "yi:", y_i, "x2:", x2_i, "xy:", xy_i);

str1 = str(n) + " " + str(x_i) + " " + str(y_i) + "\n";
str2 = str(x_i) + " " + str(x2_i) + " " + str(xy_i) + "\n";

m2 = open("m4.in", 'w');
m2.write("2\n");
m2.write(str1);
m2.write(str2);
m2.close();
