"""Se citesc pe rand temperaturile medii ale fiecarei luni din an. 
Sa se scrie cu doua numere dupa virgula media temperaturii cu valoare pozitiva si negativa."""
i = 0
p = 0
n = 0
sumpoz = 0
sumneg = 0

while i < 12:
    temp = eval(input('Introduceti temperatura intr-o luna '))
    if temp >= 0:
        sumpoz += temp
        p+=1
    if temp <= 0:
        sumneg += temp
        n+=1
    i = i + 1

if p > 0:
    media_poz = float(sumpoz / p)
    print(f'Media pozitiva este {round(media_poz, 2)}')

if n > 0:
    media_neg = float(sumneg / n)
    print(f'Media neg este {round(media_neg, 2)}')