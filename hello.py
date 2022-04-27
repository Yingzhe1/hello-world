num=input('Give me an integer: ')
if num.lstrip('-').isdigit():#判断是否为整数，正数负数都可以使用
    print(int(num)+1)
    print(int(num)+2)
    print(int(num)+3)
else:
    print('It is not a integer.')
