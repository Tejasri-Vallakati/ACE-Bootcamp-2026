try:
    a=int(input("Enter First value: "))
    b=int(input("Enter Second value: "))
    print("I am try just started")
    if b%2==0:
        raise Exception
    else:
        print(a/b)
except ZeroDivisionError as zd:
    print(zd)
except Exception as e:
    print(e)
else:
    print("Hii, I am else now alive because try is executed")
finally:
    print("Hello there I am finally, I am going to close")