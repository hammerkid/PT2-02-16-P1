import re

def correct_input (user_input):
    return  re.sub('[^a-zA-Z]+', ' ', user_input)

# x=correct_input('abc    deeet!!&*( 436__   A')
print x
