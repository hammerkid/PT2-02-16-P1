import re
def correct_input (user_input):
    return  re.sub("[^a-zA-Z]+", "", user_input)


def autocomlete(new_input, user_array):
    new_input=correct_input(new_input)
    letters = tuple(letter or letter.upper() for letter  in new_input)
    return [word for word in user_array if word.startswith(letters or letters.upper)]

if __name__ == "__main__":
    au = autocomlete('Aaa', ['Bbb','aaa','gfghfjh'])
    print (au)