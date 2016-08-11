
def correct_input (user_input):
    new_input=[]
    for letter in user_input:
        if letter.isalpha():
            new_input+=letter
    return new_input


def autocomlete(new_input, user_array):
    new_input=correct_input(new_input)
    for word in user_array:
        #print word
        #print new_input
        for letter in new_input:
            if word.startswith(letter[0:5]):
                return word
                #print  word
            else:
                pass


au = autocomlete('avt123', ['bbb','aaa'])
print (au)