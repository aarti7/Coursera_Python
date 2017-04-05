# PYTHON QUICK GUIDE
# http://www.codeskulptor.org/#user43_kpNkNDzdUJ_11.py


# division example
# if one value is floating, result is floating. Else integer
a = 13/2
print(a)

a= 13.0/2
print(a)

a= 13/2.0
print(a)

a= 13.0/2.0
print(a)


# Modulo Example // # Remainder is dropped. It is not 'not displayed', but dropped entirely.

a = 13//2
print(a)

a= 13.0//2
print(a)

a= 13//2.0
print(a)

a= 13.0//2.0
print(a)


##
TypecastedNumber = int("100")
print(TypecastedNumber)

addNumberafterTypecasting = TypecastedNumber + 4
print(addNumberafterTypecasting)

addTwoNumbers = 100 + 9
print(addTwoNumbers)

orderis = ord("a")
print(orderis)

typeOfNumberis = type(100)
print(typeOfNumberis)

typeOfAlphabetis = type("100")
print(typeOfAlphabetis)


typeOfAlphabetis = type("a")
print(typeOfAlphabetis)


setis = set([1,1,2,3,3,4,5])
print len(setis) # len in set = only unique values are retained.

# Priority order : not > and > or 
print( not False and False or True) 

# Add '\' to write to the next line
print( "it is a \
beautiful day today")

#escape sequences
print('Rick O\'Connelle')
print('Aarti \nSingh')
print('Aarti \xSingh') # \x is a escape sequence! means that the following 2 digits are Hexadecimal number encoding a character
print(r'Aarti \xSingh') # placing r infront of a string makes it a raw string and excape sequences are not converted.

#concatenated
print('Kilo''meters')



# Dictionary
dictionary = {1: 'Aarti', 2: 'Delhi', '1': 'India', (1,2,3): 'Florida', 'present':'Austin' }

print(dictionary.get((1,2,3))) # Keys should be immutable! Tuples can be used a key as they are immutables
print(dictionary.get('1')) # keys can be mixed between integer and string and they will be treate as different keys

dictionary[1.0] = 'Singh' # 1.0 and 1 are treated as same keys cause pyton stores floating point number as approximation
print(dictionary.get(1.0))

print(dictionary.has_key((1,2,3))) # check if key is in the dict



dict_new = dictionary # ref to the same dict thus any change in one will affect both of them
print(dict_new)
print(dictionary)
dictionary[1]='Aarti'
print(dictionary) #any change in one will affect both of them
print(dict_new) #any change in one will affect both of them



#dict_two = dictionary.copy # ref to the same dict thus any change in one will affect both of them
#print(dict_two)
#print(dictionary)
#dictionary[1]='None'
#print(dictionary) #any change in one will affect both of them
#print(dict_two) #any change in one will affect both of them

dictionary.pop(1.0)
print(dictionary)


print(dictionary.keys())




#list
print('\n\n\nLIST')
list1 = ['Florida', 1, 'Seattle', 100000, 'Austin'] # list can be of mixed types
print(list1)
print(list1[0]) # starts at index 0
print(list1[-1]) # can be traced backwards also; -1 is the first from back
print(list1[0][4]) # first index for the element, second for the character in that element


listextension = [ 'aa', 'bb', 'cc']
list2 = [2,3,4]

list3 = ([list1], [list2]) # joined by ',' # but each list is just a element here
print(list3)


list2.append(listextension) # append adds the new element as one  element .. does not merge all the elements as separate individual elelments
print(list2)


list5 = [1,2,3]
list5.extend(listextension)
list5.extend('1')
list5.extend('THIS')

print('list 5 is ', list5) #merge all the elements as separate individual elelments

list6= [1,2,3]
list7 = list6 + listextension
print(list7) # same result as extend



listis = ['Amir', 'amir', 'Barry', 'barry'] # case sensitive.. different care means differnet calues

list_ori = [100,200,300]
list_dupli = list_ori # Second list is same reference to the same list
# Any change in list_dupli will reflect in original also

list_dupli.insert(1,0.1)
print(list_dupli) 
print(list_ori) 


print(list_dupli.index(300)) # tells you what position 300 is at


list_new_duplicate = list_ori[:] #  Fully independent copy
print(list_new_duplicate)
list_new_duplicate.insert(1,0.000000001)
print(list_new_duplicate) # change only in the new list
print(list_ori) # Original unchanged


if 'Amir' in listis:
    print("Yes, Amir is here")
    
def function_list (listo):
    listo = listo + [1]
    print (listo)

function_list(list_ori) # can pass list as argument


#final = input("This is a quick reference to python and its main DS!")#
#print(final)


# global makes the Values accessible anywhere

x = 20
y = 30
print(y)
def fucntion_global():
    global y # y is accessible here cause of global in front of it
    #x = x+3 Is only present within this function locally! Either make a new local variable x or use the globally defined variable x by writing 'global x'
    y = y+2
    print(y)
    #print(x)
    
fucntion_global()
print(y)


# Lambda
#How to write =>> lambda argumentList : expression
f = lambda u,v : u+v
print(f(3,4))

# Filter
#How to write =>> filter(func, an-iterable)
# returns all the elements in the iterable which returned True when passed to the fucntion

flib = [0,1,2,3,4,5,6,7,8,9]
result = filter ( lambda x : x%2, flib)
print(result)
result = filter ( lambda x : x%2==0, flib)
print(result)


# Map Reduce
#How to write =>> map(function, values)
# calls the 'function' on all the 'values'


def function_fahrenheit(t):
    return ( float(t * 9/5) + 32)

tempinC = [23, 36, 46]
F= map(function_fahrenheit, tempinC)
print(F)


def function_celsius(t):
    return ( (t-32)*float(5)/9 )

tempinF=[73, 96, 114]
C= map(function_celsius, tempinF)
print(C)


# with

# split

# save file


