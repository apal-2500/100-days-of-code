#request input for math
calc = input("calcluation  ...  ")

#convert
x, y, z = calc.split(" ")

#convert number
fl_x = float(x)
fl_z = float(z)

if  y == "+":
    print(round(fl_x + fl_z, 1))
if y == "-":
    print(round(fl_x - fl_z, 1))
if y == "*":
    print(round(fl_x * fl_z, 1))
if y == "/":
    print(round(fl_x / fl_z, 1))
