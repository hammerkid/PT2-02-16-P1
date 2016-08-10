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
        for index in range(len(letter_list)):
            position = letter_list[index]
            if index % 2 == 0:
                letter_list[index] = position.upper()
            #else:
                #letter_list[index] = list_of_words[index].lower()

        joined = (''.join(letter_list))
        new_list.append(joined)
    string = ' '.join(new_list)
    print (string)

to_wierd(a)

