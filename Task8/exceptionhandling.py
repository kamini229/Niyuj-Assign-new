def exceptionHanling():
    try:
        a = 10
        b = "kamini"
        c = 0

        d = (a + b)/c
        print(d)
    except ZeroDivisionError:
        print("Zero Division")
    except TypeError:
        print("Can't add string to integer")

exceptionHanling()