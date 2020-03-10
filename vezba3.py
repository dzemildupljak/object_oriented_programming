# Gravitational force is the attractive force that exists between
# two masses.
# It can be calculated by using the following formula:
#
# G M m
# _______
#  r^2
# where G is the gravitational constant, M and m are the two masses,
# and r is the distance between them.
#
# You must implement this equation in Python to calculate the gravitational force
# between Earth and the moon.
# Sample Input #
# G = 6.67 * 10^-11
# MEarth = 6.0 * 10^24
# mMoon = 7.34 * 10^22
# r = 3.84 * 10^8
# Sample Output #
# FG = 1.99 * 10^2



# USLOVNE IZJAVE
# Uslovna izjava je boolov izraz koji, ako je istina, izvršava deo koda.


# if condtional statement is True:
#     # execute expression1
#     pass
# else:
#     # execute expression2
#     pass

# Postoje tri vrste uslovnih izjava u Pithon-u:

num = 5

if (num == 5): # The condition is true
  print ("The number is equal to 5") # The code is executed

if num > 5: # The condtion is false
  print ("The number is greater than 5") # The code is not executed


# Možemo koristiti logičke operatore za stvaranje složenijih uslova u izjavi if.
# Na primer, možda ćemo želeti da udovoljimo više klauzula da bi izraz bio tačan.

variable1 = 12

if variable1 % 2 == 0 and variable1 % 3 == 0 and variable1 % 4 == 0 :
  # Only works when variable1 is a multiple of 2, 3, and 4
  print ("The variable1ber is a multiple of 2, 3, and 4")

if (variable1 % 5 == 0 or variable1 % 6 == 0):
  # Only works when variable1 is either a multiple of 5 or 6
  print ("The number is a multiple of 5 and/or 6")

# Karakteristika uvjetnih izjava je da ih možemo ugnijezditi. To znači da može postojati if izjava unutar drugog!

variable2 = 63

if variable2 >= 0 and variable2 <= 100:
    if variable2 >= 50 and variable2 <= 75:
        if variable2 >= 60 and variable2 <= 70:
            print ("The number is in the 60-70 range")


# U uslovnoj izjavi možemo da izmenimo vrednosti naših promenljivih.

variable3 = 10
if variable3 > 5:
  variable3 = 20 # Assigning a new value to variable3
  new_variable3 = variable3 * 5 # Creating a new value called newvariable3

# The if condition ends, but the changes made inside it remain
print (variable3)
print (new_variable3)



# ELSE IF

variable4 = 60

if variable4 <= 50:
    print ("The number is less than or equal to 50")
else:
    print ("The number is greater than 50")


# output_value1 if condition else output_value2

# Ako je ispunjen uslov, izlaz će biti output_value1. U suprotnom, to bi bilo output_value2.


output = 60

output = "The number is less than or equal to 50" if output <= 50 else \
                                            "The number is greater than 50"

print (output)

# Izjava if-else obrađuje dve strane istog stanja: True i False. Ovo vrlo dobro funkcioniše ako radimo sa
# problemom koji ima samo dva ishoda.
#
# Međutim, u programiranju to nije uvek istinit ili lažan scenario i problem može imati više ishoda.
#
# Ovde pojavljuje izjava if-elif-else. To je najopsežnija uslovna izjava jer nam omogućava da
# lako stvorimo više uslova.

light = "Red"

if light == "Green":
    print ("Go")
elif light == "Yellow":
    print ("Caution")
elif light == "Red":
    print ("Stop")
else:
    print ("Incorrect light signal")



# ElIF uslovljavanje mozemo ponavljati koliko je potrebno puta

broj = 5

if broj == 0:
  print ("Zero")
elif broj == 1:
  print ("One")
elif broj == 2:
  print ("Two")
elif broj == 3:
  print ("Three")
elif broj == 4:
  print ("Four")
elif broj == 5:
  print ("Five")
elif broj == 6:
  print ("Six")
elif broj == 7:
  print ("Seven")
elif broj == 8:
  print ("Eight")
elif broj == 9:
  print ("Nine")

# Važna stvar koju morate imati na umu je da if-elif-else ili if-elif
# izjava nije isto što i više if.
# ako izjave deluju nezavisno.
#
# Ako su uslovi dve uzastopne tačke tačni, obe izjave će se izvršiti.
#
# S druge strane, u slučaju if-elif-else, kada se uslov procenjuje na True,
# ostali uslovi izjave se ne procenjuju.

# IF statement

varable6 = 10

if varable6 > 5 :
  print ("The number is greater than 5")

if varable6 % 2 == 0 :
  print ("The number is even")

if not varable6 % 2 == 0 :
  print ("The number is odd")

# ELFI statement

varable7 = 10

if varable7 > 5 :
  print ("The number is greater than 5")
elif varable7 % 2 == 0 :
  print ("The number is even")
else:
  print ("The number is odd and less than or equal to 5")

#########################################################################################################


# PETLJE
#
# Petlja je kontrolna struktura koja se koristi za obavljanje skupa uputstava za
# određeni broj puta
#
# Petlja je kontrolna struktura koja se koristi za izvođenje skupa uputstava za
# određeni broj puta.
# Prekidači za rešavanje problema moraju pisati isti skup uputstava iznova i iznova.
# Možemo odrediti koliko puta želimo da se kod izvrši.

# The for loop
# The while loop


# A for petlja koristi iterator za kretanje u nizu, npr. raspon brojeva, elementi liste itd.
# Jednostavno rečeno, iterator je varijabla koja prolazi kroz listu.
# Iterator počinje od početka sekvence. U svakoj iteraciji iterator ažurira na sledeću vrednost u nizu.
# Petlja se završava kada iterator dođe do kraja.

# Ime iteratora
# Niz koji treba proći
# Skup operacija koje treba izvesti
# Petlja uvek počinje sa ključnom rečju for. Telo petlje je razvedeno desno:



# U Pithon-u se ugrađena funkcija range () može koristiti za kreiranje niza celih brojeva.
# Taj niz se može ponoviti kroz petlju. Opseg je naveden u sledećem formatu:
# range(start, end, step)

for i in range(1,11): # A sequence from 1 to 10
    if i % 2 == 0:
        print (i, " is even")
    else:
        print (i, " is odd")


# Kao što vidimo gore, umesto da pojedinačno proveravamo da li je svaki celi broj od 1 do 10 paran ili neparan,
# možemo proći kroz sekvencu i izračunati i% 2 == 0 za svaki element.
# Iterator, i, počinje od 1 i postaje svaka sledeća vrednost u nizu.
# Da vidimo kako se petlja menja kada je određena komponenta koraka raspona:

for i in range(1,11,3): # A sequence from 1 to 10 with a step of 3
    print (i)

# Udvostrucimo vrednosti liste kroz for petlju

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print (float_list)

for i in range(0, len(float_list)): # Iterator goes traverses to the last index of the list
  float_list[i] = float_list[i] * 2

print (float_list)


# Takođe bismo mogli da pređemo elemente liste / niza direktno kroz iterator.
# U gornjoj listi float_list, da proverimo koliko je elemenata veće od 10:

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list: # Iterator goes traverses to the last index of the list
  if num > 10:
    count_greater += 1

print (count_greater)



# Pithon nam omogućava lako stvaranje petlje unutar petlji. Postoji samo jedan ulov:
# unutrašnja petlja će se uvek završiti pre spoljne petlje.
# Za svaku iteraciju spoljne petlje iterator u unutrašnjoj petlji dovršiće iteracije za dati opseg,
# nakon čega će spoljna petlja preći na sledeću iteraciju.

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list: # Now we have two iterators
        if(n1 + n2 == n):
            print(n1, n2)

# Ponekad moramo izaći iz petlje pre nego što dođe do kraja.
# To se može dogoditi ako smo pronašli ono što smo tražili i ne treba više da pravimo račune u petlji.

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
result = ()
found = False # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            result = (n1, n2)
            found = True # Set found to True
            break # Break inner loop if a pair is found
    if found == True:
        break # Break outer loop if a pair is found

print (result)


# Kada se koristi ključna reč Continu, preskače se ostatak te određene iteracije. Petlja se nastavlja na sledeću ponavljanje.
# Možemo reći da ne prekida petlju, već preskače sav kod u trenutnoj iteraciji i prelazi na sledeću

num_list = list(range(0, 10)) # 0123456789

for num in num_list:
  if num == 3 or num == 6 or num == 8:
    continue
  print (num)



#############################################################################################
# WHILE LOOP


# Petlja dok se ponavlja i ponavlja tokom određenog skupa operacija sve dok određeni uslov bude istinit.

# U petlji for je fiksiran broj ponavljanja jer znamo veličinu sekvence.
# S druge strane, petlja za vreme nije uvek ograničena na fiksni raspon.
# Izvršavanje se zasniva isključivo na stanju koji je s njom povezan.


# Evo petlje koja otkriva maksimalnu snagu od n pre nego što vrednost pređe 1000:

n = 2 # Could be any number
stepen = 0
vrednost = n
while vrednost < 1000:
  stepen += 1
  vrednost *= n
print (stepen)

# Takođe možemo koristiti petlje sa strukturama podataka,
# posebno u slučajevima kada se dužina strukture podataka menja tokom iteracija.

# Sledeća petlja izračunava zbir prvih i poslednjih cifara bilo kog celog broja:
n = 249
last = n % 10 # Finding the last number is easy

first = n # Set it to `n` initially
while first >= 10:
  first = first // 10 # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print (result)


# U odnosu na petlje, trebali bismo biti pažljiviji prilikom stvaranja petlji.
# To je zato što neko vreme petlja ima potencijal da se nikad ne završi. Ovo bi moglo srušiti program!


# while(True):
#   print ("Hello World")
#
# x = 1
# while(x > 0):
#   x += 5
#
# Pauza, nastavak i prolaženje ključnih reči rade i za petlje.
#
# Kao i za petlje, tako i mi možemo gnijezditi dok se petlje. Dalje, dve vrste petlji možemo

