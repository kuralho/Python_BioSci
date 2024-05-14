a1 = {2, 3, 4, 5, 6}
a2 = {1, 2, 4, 5}
a3 = {0,1,5,7,2,4}

r1 = a1-a2-a3
r3 = a2-a1-a3
r4 = a3-a1-a2
r6 = (a1-a2).intersection(a3)
r5 = (a2-a1).intersection(a3)
r2 = (a2-a3).intersection(a2)
r7 = a1.intersection(a2).intersection(a3)


A= a1-a2
B= a2-a1
C= a2-a3

r1= A-B-C
r3= B-A-C
r4= C-A-B
r5= B.intersection(a3)
r6= A.intersection(a3)
r2= C.intersection(a2)
r7 = a1.intersection(a2).intersection(a3)

print("Oi, temos os seguintes rsultados:")
print(r1,r2,r3,r4,r5,r6,r7)

print("Região 1:", r1)
print("Região 2:", r2)
print("Região 3:", r3)
print("Região 4:", r4)
print("Região 5:", r5)
print("Região 6:", r6)
print("Região 7:", r7)
