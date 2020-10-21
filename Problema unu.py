"""Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma 
tuturor numerelor introduse."""
i=0
suma=0
nr=1
while nr!=0 :
    nr=eval(input("Introduceti un numar pozitiv:"))
    suma+=nr 
print(suma)