vowels = ['a', 'e', 'i', 'o', 'u',]
s= input('enter the word')
snew= list(s)
vowels_list =[]
for x in snew:
    if x.lower() in vowels:
        vowels_list.append(x)
vowels_string = ''.join(vowels_list)
print(vowels_string)
