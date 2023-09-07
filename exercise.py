"""Task 1.Write a Python program to check that a string contains
only a certain set of characters (in this case a-z, A-Z and 0-9)."""
# import re

# pattern = '[a-z]+[A-Z]+[0-9]+' #[a-zA-Z0-9]



# text = input('Please enter a text to check if the input string contains \nthe certain set of lowercase, uppersace and integers. : ')

# match = re.search(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()} ')
#     print(f'All matched sequences : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')

#--------------------------------------------------------------------------

# string1 = 'vG0'
# string2 = '[cT5]'
# print(re.match(pattern, string1))
# print(re.search(pattern, string2))
# print(re.match(pattern, string2))


"""Task 2.Write a Python program that matches a string 
that has an a followed by zero or more b's."""

# import re

# pattern = '[ab*]'

# text = input("Enter a text to match if the input string has an a followed by zero or more b's: ")

# match = re.search(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched sequences : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')

#--------------------------------------------------------------------------
# string1 = 'combbbbbbbbbbbbo'
# string2 = 'como'
# string3 = 'combo'
# string4 = 'hello'
# string5 = '123124123'

# print(re.search(pattern, string1))
# print(re.search(pattern, string2))
# print(re.search(pattern, string3))
# print(re.search(pattern, string4))
# print(re.search(pattern, string5))
# print('-------------------------')
# print(re.match(pattern, string1))
# print(re.match(pattern, string2))
# print(re.match(pattern, string3))
# print(re.match(pattern, string4))
# print(re.search(pattern, string5))

"""Task 3.Write a Python program that matches a string 
that has an a followed by one or more b's."""

# import re

# pattern = 'ab+'

# text = input("Enter a text to match if the input string has an a followed by one or more b's: ")

# match = re.search(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched sequences : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')

#--------------------------------------------------------------------------
# string1 = 'combbbbbbbbbbo'
# string2 = 'combo00'
# string3 = 'como'
# string4 = 'hello'

# print(re.search(pattern, string1))
# print(re.search(pattern, string2))
# print(re.search(pattern, string3))
# print(re.search(pattern, string4))

"""Task 4.Write a Python program that matches a string 
that has an a followed by zero or one 'b'."""

# import re

# pattern = 'ab?'

# text = input("Enter a text to match if the input string has an a followed by zero or one 'b': ")

# match = re.search(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched sequences : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')


#--------------------------------------------------------------------------
# string1 = 'combo'
# string2 = 'como'
# string3 = 'combbo'
# string4 = '123'

# print(re.search(pattern, string1))
# print(re.search(pattern, string2))
# print(re.search(pattern, string3))
# print(re.search(pattern, string4))

"""Task 5.Write a Python program that matches a string 
that has an a followed by three 'b'."""
# import re

# pattern = 'ab{3}'

# text = input("Enter a text to match if the input string has an a followed by three 'b'.: ")

# match = re.search(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched sequences : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')

#--------------------------------------------------------------------------
# string1 = 'combo'
# string2 = 'combbo'
# string3 = 'combbbo'
# string4 = 'combbbbo'
# string5 = 'combbbbbbooooo'

# print(re.search(pattern, string1))
# print(re.search(pattern, string2))
# print(re.search(pattern, string3))
# print(re.search(pattern, string4))
# print(re.search(pattern, string5))

"""Task 6.Write a Python program that matches a string 
that has an a followed by two to three 'b'."""

# import re

# pattern = 'ab{2,3}'
# text = input("Enter a text to match if the input string has an a followed by two to three 'b'.: ")

# match = re.search(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched seqeunces : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')

#--------------------------------------------------------------------------
# string1 = 'boobbbobobbbbbbb'
# string2 = 'bobobobobobobobobo'
# string3 = 'bbbbaa'

# print(re.findall(pattern, string1))
# print(re.search(pattern, string2))
# print(re.findall(pattern, string3))


"""Tesk 7.Write a Python program to find sequences of lowercase 
letters joined by an underscore."""

# import re

# pattern = '[a-z]+_[a-z]+'

# text = input("Enter a text to match if the input string has sequences of lowercase letters joined by an underscore: ")

# match = re.search(pattern, text)

# if match:
#     print(f"First matched sequence: {match.group()}")
#     print(f"All matched sequences: {re.findall(pattern, text)}")
# else:
#     print('There is no matched text.')
    

#--------------------------------------------------------------------------

# string1 = 'aASDAFDSDF123asdafs_'
# string2 = '1231254a213'
# string3 = '1231254a_213'

# print(re.search(pattern, string1))
# print(re.findall(pattern, string1))
# print(re.search(pattern, string2))
# print(re.findall(pattern, string2))
# print(re.search(pattern, string3))
# print(re.findall(pattern, string3))

"""Tesk 8.Write a Python program to find the sequences
of one upper case letter followed by lower case letters."""

# import re 

# pattern = '([A-Z]){1}([a-z]+)'   #pattern = '[A-Z][a-z]+'

# text = input("Enter a text to match if the input string has sequences of one uppercase letter followed by lowercase letters: ")

# match = re.search(pattern, text)

# if match:
#     print(f'The uppercase group of first matched sequence :{match.group(1)} ')
#     print(f'The lowercase group of first matched sequence :{match.group(2)} ')
#     print(f'All matched sequences : {re.findall(pattern, text)}')
# else:
#     print('There is no matched text.')


"""Task 9.Write a Python program that matches a string 
that has an 'a' followed by anything ending in 'b'."""

# import re

# pattern = '(a).*(b$)'  # pattern = '(a.+)b$' 'or' \w(a.+)b$

# text = input("Enter a text to match if the input string has an 'a' followed by anything ending in 'b': ")

# match = re.search(pattern, text)
# All_ = re.findall(pattern, text)

# if match:
#     print(f'First matched sequence : {match}')
#     print(f'All matched sequences : {All_}')
# else:
#     print('There is no matched text.')

#--------------------------------------------------------------------------

# import re 
# pattern = '[\w*\W*\d*\D*\s*]+'

# text = input('Enter anything: ')

# print(re.search(pattern, text))




"""Task 10.
Write a Python program that matches a word at the beginning of a string."""

# import re 

# text = input('Enter any text, and the program will return the first word: ')

# # pattern = '^(\w+)'

# pattern = '^[a-z*A-z*]+'

# first = re.match(pattern, text)

# if first:
#     print(f'This is the fisrt word of {text} : {first.group()}')
# else:
#     print('There is no matched text.')


"""Task 11.
Write a Python program that matches a word at the end of a string, with optional punctuation."""

# import re

# text = input('Enter any text, and the program will return the last word: ')

# # pattern = '(\w+\W?)$'
# pattern = r'(\w+[.?!,;:\'"-=~_+<>\\|%@#\^\*&]?)$'

# last = re.search(pattern, text)

# if last:
#     print(f'The last word of {text} : {last.group()}')
# else:
#     print('There is no matched text.')

# import re

# pattern = '\W+'

# text = re.search(pattern, '.!-:;"')

# print(text.group())

"""Task 12.Write a Python program that matches a word containing 'z'.
"""

# import re

# text = input('Enter a text to match a word containing "z": ')

# pattern = r'\w*[z]\w*'

# match = re.search(pattern, text, re.IGNORECASE)

# all_ = re.findall(pattern, text, re.IGNORECASE)

# if match:
#     print(f'The word containing "z" in the input : {match.group()}')
#     print(f'The word containing "z" in the input : {all_}')
    
# else:
#     print('There is no matched text.')
    
"""Task 13.Write a Python program that matches a word 
containing 'z', not the start or end of the word."""

# import re 

# text = input('Enter a text to match a word containing "z", not the start or end of the word.: ')

# pattern = r'\w+[z]\w+' # pattern = r'[a-yA-Y]+[z]+[a-yA-Y]+'

# match = re.search(pattern, text, re.IGNORECASE )

# all_ = re.findall(pattern, text, re.IGNORECASE)

# if match:
#     print(f'The appropriate words in the input : {all_}')
    
# else:
#     print('There is no matched text.')


"""Task 14.Write a Python program to match a string that contains only upper 
and lowercase letters, numbers, and underscores."""

# import re

# text = input('Enter a text to find a string that contains only upper \nand lowercase letters, numbers, and underscores: ')

# pattern = '\w+'

# match = re.findall(pattern, text,)

# if match:
#     print(f'{match}')


"""Task 15.Write a Python program that starts each string with a specific number."""


# import re
# import random

# num = input('Enter any number: ')

# num_pattern = r'\b\d+\b'

# num_match = re.findall(num_pattern, num)

# text = input('Enter any text: ')

# pattern = r'\b\w+\b'

# match = re.findall(pattern, text)

# for i in num_match:
#     for e in match:
        
#         result = i + e
        
#         print(result, end=' ')

#--------------------------------------------------------------------------
# num_pattern = str(random.randint(0,10000))
#--------------------------------------------------------------------------

# import re
# import random

# def gen():
#     while True:
#         prompt = input('Enter any text or (e):exit to quit: ')
#         if prompt.lower() == 'e':
#             break
#         pattern = r'\b\w+\b'
        
#         match = re.findall(pattern, prompt)
        
#         ran_num = random.randint(0, 10000)
        
#         for element in match:
            
#             yield f'{ran_num}{element}'

# generator = gen()

# for value in generator:
#     print(value)


"""Task 16.
Write a Python program to remove leading zeros from an IP address.
"""

# # -192.158.1.38.
import re

ip = '01230.0247.0124.024700'

pattern = '0([\d]+\.?)'

match = re.sub(pattern, r'\1', ip)

print(match)

# pattern = r'^0*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.0*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.0*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.0*(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

# match = re.search(pattern, ip)

# if match:
#     clean = ".".join(match.groups())
#     print(clean)
        
# else:
#     print('There is no match')



# pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'


# import re


# ip = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

# email = r'^[a-zA-Z0-9\._-]*@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$'

# num = '555'

# P_num = r'^([0123]?[0-9][0-9]?)'

# p_handy = r'\+[4][9]\s[1][5-7][0-9]\s[0-9]{8}' # +49 152 07226260

# handy = '+49 176 24049637'

# match = re.search(p_handy, handy)

# print(match)