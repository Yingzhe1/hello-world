num=input('Give me an integer: ')
if num.lstrip('-').isdigit():
    print(int(num)+1)
    print(int(num)+2)
    print(int(num)+3)
else:
    print('It is not a integer.')
