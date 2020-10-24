







# def test(x,y,z): # x=1,y=2,z=3
#     print(x)
#     print(y)
#     print(z)
#
# # test(1,2,3) # 传入的参数位置与上面的x，y，z 一一对应
# test(2,3,z=1)

# def test(x,**kwargs):
#     print(x)
#     print(kwargs)
# # test(1,2,3,4,5)
# test(1,**{'a':4,"b":'5'})

# def test(x,*args,**kwargs):
#     print(x)
#     print(type(args))
#     print(kwargs)
# test(1,*['a',3,'c'],**{'a':2,'b':'3'})


NAME = 'python'
def test1():
    name = 'hello1'
    print(name)
    def test2():
        print('hello2')
        def test3():
            print('hello3 ')
    test2()
    print(name)

test1()

