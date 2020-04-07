# Funkcija je skup operacija za višekratnu upotrebu


# U Python-u se funkcija može definisati pomoću ključne reči def u sledećem formatu:
#
#       Naziv funkcije je jednostavno ime koje ćemo koristiti za identifikaciju funkcije.
#
        # Parametri funkcije su ulazi za tu funkciju. Te ulaze možemo koristiti u okviru funkcije.
        # Parametri nisu obavezni. O ovim ćemo saznati nešto kasnije.
#
#       Telo funkcije sadrži skup operacija koje će funkcija obavljati. Ovo je uvek razvedeno na desnoj strani.

def my_print_function():  # Nema parametara
    print("This")
    print("is")
    print("A")
    print("function")
    # Funkcija se zavrsava


# Pozivanje funkcije vise puta
my_print_function()
my_print_function()



# Parametri su presudni deo strukture funkcija.
#
# Oni su sredstvo prenosa podataka u funkciju. Ove podatke funkcija može koristiti za obavljanje smislenog zadatka.
#
# Prilikom kreiranja funkcije moramo definirati broj parametara i njihova imena.
# Ova imena su relevantna samo za funkciju i neće uticati na imena promenljivih na drugim mestima u kodu.
# Parametri su u zagradama i odvojeni zarezima.
#
# Stvarne vrijednosti / varijable koje su prešle u parametre poznate su kao argumenti.


def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)

# Do sada smo samo definisali funkcije koje nešto štampaju. Ne vraćaju nam ništa. Ali ako se osvrnemo,
# funkcije stalno vraćaju vrednosti. Uzmite na primer len (). Vraća ceo broj koji je dužina strukture podataka.
#
# Da bismo vratili nešto iz funkcije, moramo koristiti ključnu reč return.
# Imajte na umu da kada se izvrši izjava vraćanja, prevodilac završi funkciju.
# Preostali redovi koda nakon povratne izjave neće se izvršiti.



# Opseg funkcije znači u kojoj su mjeri varijable i ostale stavke podataka napravljene unutar funkcije dostupne u kodu.
#
# U Python-u, opseg funkcije je telo funkcije.
#
# Kad god se neka funkcija pokrene, program prelazi u opseg funkcije. Kada se funkcija završi, vraća se u spoljni opseg.


# U Python-u se podaci kreirani unutar funkcije ne mogu koristiti izvana ako se ne vrate iz funkcije.
#
# Varijable u funkciji su izolovane od ostatka programa.
# Kada se funkcija završi, oni se oslobađaju iz memorije i ne mogu ih vratiti.

name = "Ned"

def func():
    name = "Stark"

func()
print(name)

# Kada se mutable(promenljivi) podaci predaju funkciji, funkcija može da ih modifikuje ili izmeni.
# Ove modifikacije će takođe ostati na snazi i izvan opsega funkcije.
# Primer izmenljivih podataka je lista.
#
# U slučaju nepromenljivih(unmutable) podataka, funkcija može da je modifikuje,
# ali podaci će ostati nepromenjeni izvan dometa funkcije.
# Primeri nepromenljivih podataka su brojevi, nizovi itd.



# U Python-u, jedna funkcija može postati argument za drugu funkciju. Ovo je korisno u mnogim slučajevima.
#
# Napravimo funkciju kalkulatora koja zahteva funkciju dodavanja, oduzimanja, množenja ili deljenja
# zajedno sa dva broja kao argumente.

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)  # Koristimo 'operation' funkciju kao argument


result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))


# Rekurzija je proces u kojem funkcija sebe poziva tokom izvršavanja.
# Svaki rekurzivni poziv program umanjuje dublje u funkciju.
#
# Rekurzivni pozivi se zaustavljaju na osnovnom slučaju.
# Osnovni slučaj je check koji se koristi da bi pokazao da ne bi trebalo da postoji daljnja rekurzija.

def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # Rekurzivni poziv sa razlicitimo argumentom
    print(number)


rec_count(5)

# Rekurzija je koncept koji mnogi isprva teško shvate, ali ima svoje prednosti.
# Za početak, može značajno da smanji vreme izvođenja određenih algoritama, što kod čini efikasnijim.
#
# Rekurzija nam takođe omogućava da lako rešimo mnoge probleme povezane sa grafovima i drvećem,
# stvari koje biste mogli proučiti u budućnosti. Takođe je važno u algoritmima pretraživanja.
#
# Međutim, moramo biti oprezni kada koristimo rekurziju.
# Ako ne navedemo odgovarajući osnovni slučaj ili ažuriramo svoje argumente dok ponavljamo,
# program će doći do beskonačne rekurzije i rušenja.
# Argumenti prosleđeni našoj rekurzivnoj funkciji ažuriraju se u svakom rekurzivnom pozivu tako da se
# na kraju može doći do osnovnog slučaja.


# 1. Napisati funkciju koja provjerava da li je upisan broj paran ili neparan.

# 2. Napišite funkcije za sabiranje dva broja i pozovite je u glavnom dijelu programa. Omogućite
# izvršavanje te funkcije 3 puta.

# 3. Napisat program koji će korisniku nakon što unese broj provjeriti parnost i negativnost
# unesenog broja. Potrebno je izraditi dvije funkcije: jednu za provjeru parnosti broja, a drugu
# za provjeru negativnosti broja.
