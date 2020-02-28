# Celotni tip podataka sastoji se od svih pozitivnih i negativnih celih brojeva.
#
# Količina memorije koju ceo broj zauzima zavisi od njegove vrednosti.
# Na primer, 0 će zauzeti 24 bajta dok će 1 zauzeti 28 bajtova


print(10)
print(-3000)

num = 123456789
print(num)
num = -16000
print(num)

# Brojevi sa zarezom ili 'float' se odnose na pozitivne i negativne decimalne brojeve.
#
# Pithon nam omogućava da kreiramo decimale do veoma visokog decimalnog mesta.
#
# To osigurava tačne izračune za precizne vrednosti.
#
# Float zauzima 24 bajta memorije.

print(1.00000000005)
print(-85.6701)

flt_pt = 1.23456789
print(flt_pt)


# Pithon takođe podržava složene brojeve ili brojeve sačinjene od stvarnog i imaginarnog dela.
# Baš kao što se print() koristi za ispis vrednosti, tako se i complex() koristi za kreiranje složenih brojeva.
# Zahteva dve vrednosti. Prva će biti stvarni deo složenog broja, dok će druga vrednost biti zamišljeni deo.

# Složeni broj zauzima 32 bajta memorije.

print(complex(10, 20))
print(complex(2.5, -18.2))

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)


#############################################
# Aritmeticki operatori

# Ispod možemo pronaći osnovne aritmetičke operatore redosledom prioriteta.
# Operator naveden na višem nivou prvo će se izvrsiti(izracunati).

# () zagrade    Inkapsulira prethodnu operaciju
# ** exponent   Stepenovanje
# %, *, /, //  Modulo, Multiplication, Division, Floor Division
# +, -  Sabiranj i oduzimanje

# Zagrade
# Izraz koji je zatvoren u zagradama prvo će se izračunati, bez obzira na prioritet operatora

print((10 - 3) * 2)
print((18 + 2) / (10 % 8))

# Stepenovanje
# Koristeći dvostruku zvezdicu operatora eksponencijacije (**) za izračunavanje eksponenta u Pithon-u

exp1 = 4 ** 3

flt_exp2 = 3.3 ** 3

neg_exp3 = 10 ** -3


print(exp1)
print(flt_exp2)
print(neg_exp3)

# Modul
# Modul broja sa drugim brojem može se pronaći pomoću operatora %

print (10 % 2)

broj = 28
print(broj % 10)

print(-28 % 10) # Ostatak je uvek pozitivan
print(34.4 % 2.5) # Ostatak moze biti float

# Mnozenje

# Aritmetički izraz koji sadrži različite operatore izračunava se na osnovu prioriteta operatora.

print(10 - 3 * 2)

# Deljenje
# Jedan broj možemo podeliti sa drugim koristeći / operator:

print(40 / 10)
float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)


# Zaokruzivanje pri deljenju
# Za zaokruzeno delje koristimo // operator:

print(43 // 10)
float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)




# Sabiranje
# Pomoću operatora + možemo sabrati dva broja:

print (10 + 5)

float_1 = 13.65
float_2 = 3.40
print(float_1 + float_2)

num = 20
flt = 10.5
print(num + flt)

# Oduzimanje
# Možemo oduzeti jedan broj od drugog koristeći operatora -

print(10 - 5)

flt1 = -18.678
flt2 = 3.55
print(flt1 - flt2)

num = 20
flt = 10.5
print(num - flt)

#################################################
# Operatori za poređenje

# Poređenja #
# Rezultat poređenja je uvek buol.
#
# Ako je poređenje tačno, vrednost bool će biti tačna. U suprotnom, njegova vrednost će biti netacna.


num1 = 5
num2 = 10
num3 = 10
print(num2 > num1)
print(num1 > num2)

print(num2 is num3)
print(num3 is not num1)

print(3 + 10 == 5 + 5)
print(3 <= 2)


##############################################
# Operatori za dodelu
# Ovo je kategorija operatora koja se koristi za dodelu vrednosti promenljivoj.
# Operator = koji smo do sada koristili je operator dodjele, ali nije jedini.


# Varijable su promenljive, tako da njihove vrednosti možemo menjati kad god želimo!

year = 2019
print(year)

year = 2020
print(year)

year = year + 1
print(year)
#####################
num = 10
print(num)

num += 5
print(num)

num -= 5
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 2
print(num)


#################################################
# Logički izrazi
# Logički izrazi se formiraju korišćenjem Booleana i logičkih operatora.

# OR Expression
my_bool = True or False
print(my_bool)

# AND Expression
my_bool = True and False
print(my_bool)

# NOT expression
my_bool = False
print(not my_bool)