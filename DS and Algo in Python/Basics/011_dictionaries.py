my_dictionary = {'name' : 'lsawant','course':'python'}

phone_dict = {'lsawant':'555-555-5555',
'zoolander':'999-999-9999',
'jon_snow':'fail-o-so-bad'}

word_dict = {
'a':{'apple':'the round fruit of a tree of the rose farm',
'ant':'an insect which cleans up the floor'
},
'b':{'bad':'of poor quality or low standar',
'business':'season 8 of GOT'}
}

print(word_dict['b']['business'],word_dict['b']['bad'])
print(my_dictionary.get('name'))
my_dictionary['job'] = 'Python programmer'
print(my_dictionary.get('job'))
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

for k,v in my_dictionary.items():
    print(k, v)
