#Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
n=eval(input('Introduceti numarul= '))
i=n
s=0
p=1
while i:
    s+=i
    p*=i
    i-=1
print("Suma este ",s, "produsul este ",p," iar media aritmatica este s/n ")