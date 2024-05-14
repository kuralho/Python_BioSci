for x in new_list:
    if x%3==0:
        break
    print("parei", x) #está errado pois o print está no lugar errado

for x in new_list:  #esse é o certo
    if x%3==0:
        print("parei:",x)
    break


for x in new_list:  #esse é o certo
    if x%2==0:
        print("parei:",x)
    break

for x in new_list: 
    multiplos=[3,5,7,11]
    for j in multiplos:
        if x%j==0:

            print("parei:",x)
            break

multiplos=[11,17,19,13]
tag=False
while tag==False
    for val in range(1,10000,2):
        for m in multiplos:
            if val%m==0:
                tag=True
                print(f"encontrei{m} dividido {val}")

multiplos=[11,17,19,13]
tag=False


for val in range(1,10000,2):
    if tag==False:
        for m in multiplos:
            if val%m==0:
               tag=True
               print(f"encontrei{m} dividido {val}")

multiplos=[11,17,19,13]
tag=False


for val in range(20,10000,2):
    if tag==False:
        for m in multiplos:
            if val%m==0:
               tag=True
               print(f"encontrei{m} dividido {val}")


multiplos=[11,17,19,13]
tag=False


for val in [11*17*13, 13*19, 45*11*23]:
    if tag==False:
        for m in multiplos:
            if val%m==0:
               tag=True
               print(f"encontrei{m} dividido {val}")

multiplos=[11,17,19,13]
tag=False


for val in [11*17*13, 13*19, 45*11*23]:
    if tag==False:
        for m in multiplos:
            if val%m==0:
               tag=True
               print(f"encontrei{m} dividido {val}")
               break

multiplos=[11,17,19,13]
tag=True


for val in [11*17*13, 13*19, 45*11*23]:
    if tag==False:
        for m in multiplos:
            if val%m==0:
               tag=True
               print(f"encontrei{m} dividido {val}")
               break



counter = 0
while counter <=100:
    print(counter)
    counter + 99

counter = 0
while counter <=100:
    print(counter)
    counter += 99

J=0
while J <250:
    J+=1
    print(J)

J=0
while J <=250:
    J+=1
    print(J)

counter=0

while counter % 13 != 0:
    counter +=1
    print(counter)
else:
    counter +=2
    print(counter)

counter=1

while counter % 13 != 0:
    counter +=1
    print(counter)
else:
    counter +=2
    print(counter)

for x in range(1,11):
    for y in range(11,22,2):
        print(f'{x}*{y}={x*y}')
