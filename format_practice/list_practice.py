list1 = ['가위', '바위' , '보']
list2 = [37, 23 , 10, 33, 29, 40]

print (list1)
print ( list2)

print (list1[1])
print( list2[2])
print (list1[-1]) #뒤에서 첫번째! 가지고 있는 아이템 수를 넘어가면 앞이건 뒤건 오류!

list2.append(16)
print(list2)

list3 = list2 + [16]
list4 = list3 + list2

n=12
ownership = n in list3
print(ownership)

n= 10
if n in list3:
    print('{}은 있어! '.format(n))

print(list4)
del(list4[12])
print(list4)

list4.remove(40)
print(list4)