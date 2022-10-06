import math

a = float(input("Masukan Koefisien A : "))
b = float(input("Masukan Koefisien B : "))
c = float(input("Masukan Koefisien C : "))
print()
d = b*b-4*a*c

if d>0 :
    a1 = (-b + math.sqrt(d)) / (2 * a)
    a2 = (-b - math.sqrt(d)) / (2 * a)
    print("Akarnya Nyata Dan Tidak Sama ",a1, " Dan ",a2)
elif d==0 :
    a1 = -b/(2*a)
    print("Akarnya Nyata Dan Sama",a1)
else :
    print("Tidak Ada Akar Yang Nyata")