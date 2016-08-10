import re
a='1one 2two  3three 4  fo34ur fdasfdsafa   24324sdf34'
new_str=[]
def to_wierd  ( string ):
    string = re.sub(r'\d', '', string)   #Removes digits from string
    string = re.sub('\s\s+', ' ', string)  #Removes more than one whitespace from string
    list_of_words=string.split()
    new_list = []
    for word in list_of_words:
        letter_list = list(word)
        for letter in letter_list:
            if letter_list.index(letter) % 2 == 0:
                letter_list.insert(letter_list.index(letter), letter.upper())
                letter_list.pop(letter_list.index(letter))
            else:
                letter_list.insert(letter_list.index(letter), letter.lower())
                letter_list.pop(letter_list.index(letter))

            joined = (''.join(letter_list))
        new_list.append(joined)
    #print ' '.join(nu_li)
    string = ' '.join(new_list)
    print (string)

to_wierd(a)

