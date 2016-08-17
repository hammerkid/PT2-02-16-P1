
to_20 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 0: ''}

to_100 = {0: '', 2:'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def up_to_99(number):
    if number < 20:
        return to_20[number]
    else:
        return to_100[divmod(number, 10)[0]] + ' ' + to_20[divmod(number, 10)[1]]

# xx=up_to_99(88)
# print xx

def up_to_999(number):
    if divmod(number, 100)[1]<20:
        return to_20[divmod(number,100)[0]] + ' hundred ' + to_20[divmod(number,100)[1]]
    else:
        return (to_20[divmod(number,100)[0]] + ' hundred ' + to_100[divmod(divmod(number,100)[1],10)[0]] + ' ' +
    to_20[divmod(divmod(number, 100)[1], 10)[1]])

# a=up_to_999(999)
# print a

def up_to_999999(number):
    thsnd = ' thousand and '
    if divmod(number, 1000)[1] == 0 and divmod(number,1000)[0]<100:
        #if number 1000-99000
        return to_20[divmod(number, 1000)[0]] + ' thousand'
    elif divmod(number, 1000)[1] == 0 and divmod(number,1000)[0]>100:
        # if number 99000-999000
        return up_to_999(divmod(number, 1000)[0]) + ' thousand'
    elif divmod(number, 1000)[0] < 20 and divmod(number, 1000)[1] < 20:
        # if number 1001-19099
        return to_20[divmod(number, 1000)[0]] + thsnd + up_to_99(divmod(number, 1000)[1])
    elif 99 >= divmod(number, 1000)[0] >= 20 and divmod(number, 1000)[1] < 20:
        # if number 20001-99099
        return up_to_99(divmod(number, 1000)[0]) + thsnd + up_to_99(divmod(number, 1000)[1])
    elif 999 >= divmod(number, 1000)[0] >= 100 and divmod(number, 1000)[1] < 20:
        # if number  100001-999099
        return up_to_999(divmod(number, 1000)[0]) + thsnd + up_to_99(divmod(number, 1000)[1])
    elif divmod(number, 1000)[0] < 20:
        return to_20[divmod(number, 1000)[0]] + thsnd + up_to_999(divmod(number, 1000)[1])
    elif 99 >= divmod(number, 1000)[0] >= 20:
        return up_to_99(divmod(number, 1000)[0]) + thsnd + up_to_999(divmod(number, 1000)[1])
    elif divmod(number, 1000)[0] > 100:
        return up_to_999(divmod(number, 1000)[0]) + thsnd + up_to_999(divmod(number, 1000)[1])


# abc=up_to_1000(999999)
# print abc

def main(number):
    '''Supports numbers up to 999999'''
    if type(number) != int:
        print ('Not integer!')
    elif number > 999999:
        print ('Not supported in this version')
    elif number <= 99:
        return up_to_99(number)
    elif number <= 999:
        return up_to_999(number)
    elif number <= 999999:
        return up_to_999999(number)


xxx=main(999001)
print xxx








