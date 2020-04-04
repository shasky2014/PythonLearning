def outer_fun1():
    print('outer_fun1 running')

    def inner_fun1():
        for i in [1,2,3]:
            if i==2:
                print('ok done,现在结束循环')
                continue
            print(i,'inner_fun1 running')

    inner_fun1()
    print('outer_fun1 running')


outer_fun1()
