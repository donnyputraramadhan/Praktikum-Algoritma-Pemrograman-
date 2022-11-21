#operasi logika atau boolean
#not, or, and, xor
#not
print('====not====')
a = false
c = not a
print('data a=',a)
print('---------------not')
print('data c +',c)
#or(jika salah satu true, maka hasilnya adalah true)
print('====or====')
a = false
b = false
c = a or b
print(a,'or',b'=',c)
a = false
b = true
c = a or b
print(a,'or',b'=',c)
a = true
b = false
c = a or b
print(a,'or',b,'=',c)
a = true
b = true
c = a or b
print(a,'or',b,'=',c)
#and (jika dua buah nilai true, maka hasil true)
print('====and====')
a = false
b = false
c = a and b 
print(a,'and',b,'=',c)
a = false
b = true
c = a and b
print(a,'and',b,'=',c)
a = true
b = false
c = a and b
print(a,'and',b,'=',c)
a = true
b = true
c = a and b
print(a,'and',b,'=',c)
#xor (akan true jika salah satu true, sisanya false)
print('====xor====')
a = false
b = false
c = a ^ b
print(a,'xor',b,'=',c)
a = false 
b = true
c = a ^ b
print(a,'xor',b,'=',c)
a = true
b = false
c = a ^ b
print(a,'xor',b,'=',c)
a = true
b = true
c = a ^ b
print(a,'xor',b,'=',c)
