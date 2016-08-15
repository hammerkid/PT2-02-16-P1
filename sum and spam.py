def sum(*args):
    array_sum=0
    for digit in args:
        for x in digit:
            #print x
            if type(x) == int:
                array_sum = array_sum + x
        return array_sum

sum ([1,2,3,'3'])

def spam(number):
    return 'egg'*number

spam(10)