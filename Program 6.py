n = int(input('Introduceti un numar natural: '))
print(f'Ultima cifra a numarului {n} = ', n%10)
print(f'Penultima cifra a numarului {n} = ', n//10%10)
print(f'Catul si restul impartirii numarului {n} la 9 = ', n//9, 'si', n%9)
print(f'Suma cifrelor a numarului {n} = ', (n//1000) + (n//100)%10 + (n//10)%10 + n%10)
if 0<n< 10:
    print(f'Rasturnatul numarului {n} este ', n)
elif 10<=n<100:
    print(f'Rasturnatul numarului {n} este ', n //10 + n%10*10)
elif (n>=100) and (n<1000):
    print(f'Rasturnatul1 numarului {n} este ', n//100 + ((n//10)%10)*10 + (n%10)*100)
elif (n>=1000) and (n<10000):
    print(f'Rasturnatul numarului {n} este ', n//1000 + (n//100)%10 * 10 +(n//10)%10 * 100 + n%10 * 1000)
else:
    print("Ati intodus un numar >= 10000 sau <0")

"""

"""

