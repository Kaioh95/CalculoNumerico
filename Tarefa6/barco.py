arq = open("barco.pts", 'r');

m = 0;
x_i = 0;
y_i = 0;
x2_i = 0;
x3_i = 0;
x4_i = 0;
yx_i = 0;
yx2_i = 0;

for line in arq:
	point = line.split(' ');
	x = float(point[0]);
	y = float(point[1]);
	
	m += 1;
	x_i += x;
	y_i += y;
	x2_i += x * x;
	x3_i += x * x * x;
	x4_i += x * x * x * x;
	yx_i += x * y;
	yx2_i += x * x * y;
arq.close();
	
print("m:", m, "xi:", x_i, "x2i:", x2_i, "x3i:", x3_i, "x4i:", x4_i, "yi:", y_i, "yx:", yx_i, "yx2:", yx2_i);

str1 = str(m) + " " + str(x_i) + " " + str(x2_i) + " " + str(y_i) + "\n";
str2 = str(x_i) + " " + str(x2_i) + " " + str(x3_i) + " " + str(yx_i) + "\n";
str3 = str(x2_i) + " " + str(x3_i) + " " + str(x4_i) + " " + str(yx2_i) + "\n";

m5 = open("m5.in", 'w');
m5.write("3\n");
m5.write(str1);
m5.write(str2);
m5.write(str3);
m5.close();
