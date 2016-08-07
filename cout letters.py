from pprint import pprint

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

a = []
dict = {}
for x in text:

    if x in a:
        pass
    else:
        a.append(x)
        dict.update({x: text.count(x)})

pprint(dict)  #Prints sorted by alphabet

print('_'*10)

for w in sorted(dict, key=dict.get, reverse=True):  #Prints sort by numbers
    print (w,dict[w])

print('_'*10)

for w in sorted(dict, key=dict.get):  #Prints sort by numbers reversed
    print (w,dict[w])

