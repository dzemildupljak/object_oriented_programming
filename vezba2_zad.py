# 1. Napišite Pithon program da biste ispisali sledeći string u određenom formatu (pogledajte izlaz)
# String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high,
#           Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

# 2. Napisite program Pithon koji od korisnika prihvata radijus kruga i izračunava oblast


# LISTE

# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item. Just as strings are defined as characters
# between quotes, lists are defined by having values between square brackets [ ].
#
# Lists are great to use when you want to work with many related values.
# They enable you to keep data together that belongs together, condense your code,
# and perform the same methods and operations on multiple values at once.
#
# When thinking about Python lists and other data structures that are types of collections,
# it is useful to consider all the different collections you have on your computer:
#     your assortment of files, your song playlists, your browser bookmarks,
#     your emails, the collection of videos you can access on a streaming service, and more.
#
# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# animals list
animals = ['cat', 'dog', 'rabbit']

# 'guinea pig' is appended to the animals list
animals.append('guinea pig')

# Updated animals list
print('Updated animals list: ', animals)
#
# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
#
# language list
language = ['French', 'English', 'German']

# another list of language
language1 = ['Spanish', 'Portuguese']

language.extend(language1)

# Extended List
print('Language List: ', language)
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#
# vowel list
vowel = ['a', 'e', 'i', 'u']

# inserting element to list at 4th position
vowel.insert(3, 'o')

print('Updated List: ', vowel)
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
#
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
#
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)
# list.clear()
# Remove all items from the list. Equivalent to del a[:].
#
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e'
index = vowels.index('e')
print('The index of e:', index)

# index of the first 'i'
index = vowels.index('i')
print('The index of i:', index)
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
#
# list.count(x)
# Return the number of times x appears in the list.
#
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)
# list.reverse()
# Reverse the elements of the list in place.
#
# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)
# list.copy()

old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )



nesto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print()