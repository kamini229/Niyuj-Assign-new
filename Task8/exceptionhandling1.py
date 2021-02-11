def exceptionHanling1():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b)/c
        print(d)
    except:
        print("In the except block")
    else:
        print("because there is no exception, else is execute")
    finally:
        print("finally always executed")

exceptionHanling1()