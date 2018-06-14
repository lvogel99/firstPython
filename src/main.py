print("this works")

for i in range(1,11):
    if (i%2 == 0):
        print(i,"is even")
    else:
        print(i, "is odd")


message  = '{}%'

for i in range(1, 101):
    print(message.format(i))