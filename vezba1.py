# Funkcija print () ispisuje navedenu poruku na ekran ili neki drugi standardni izlazni uređaj.
#
# Poruka može biti niz ili bilo koji drugi objekt, objekt će se pretvoriti u niz prije nego što se upiše na ekran.

# print(object(s), separator=separator, end=end, file=file, flush=flush)

print("Hello world")

print("Hello", "how are you?")

# sep="" Navedite kako razdvojiti objekte ako ih ima više. Podrazumevano je ''

print("Hello", "how are you?", sep="---")

# end="" Na kraju odredite šta treba štampati. Podrazumevano je '\n'

print("Hello world", end="\n\n")
print("Hello", "how are you?")

#############################################################################################3

# String izrazi u pythonu okruženi su ili pojedinačnim navodnicima ili dvostrukim navodnicima.

a = "Hello"
print(a)

# Viselinijski string mozemo kreirati pomocu 3 navodnici

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Stringovi u Pithon-u su nizovi bajtova koji
# predstavljaju znakove unicode.
#
# Međutim, Pithon nema karakter tipa podataka, jedan znak je jednostavno niz dužine 1.
#
# Uglaste zagrade mogu se koristiti za pristup elementima niza.


a = "Hello World"
print(a[0])
print(a[6])

# s = ' H  e  l  l  o   W  o  r  l  d '
#      0  1  2  3  4  5  6  7  8  9 10
#   -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(a[-11])


# U toku prikazivanja mozete uporedjivati vrednosti i rezultat tog uporedjivanja ce vam se prikazati

vrednost1 = "Gryffindor"
vrednost2 = "Gryffindor"

print (vrednost1 == vrednost2)

new_vrednost1 = "Slytherin"

print (vrednost1 == new_vrednost1)

print (vrednost2 <= vrednost1)

print (vrednost2 >= vrednost1)


# Ključna reč može da se koristi za proveru da li određeni podstring postoji u drugom nizu.
# Ako se pronađe podstorija, operacija vraća true.


random_string = "This is a random string"

print ('of' in random_string)
print ('random' in random_string)