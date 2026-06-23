try:
    print("I am try just started")
    print(10/2)
    print("I am try, I am done")
except ZeroDivisionError as zd:
    print(zd)
else:
    print("Hii, I am else now alive because try is executed")