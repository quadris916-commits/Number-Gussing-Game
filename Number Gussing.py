import random
def num():
    
    com=random.randint(1,20)
    while True:
        u=int(input("guess the number between 1 and 20"))
        if com==u:
            print("u got it right")
            break
        elif com>u:
            print("greater")
        if com<u:
            print("lower")
    co=print("u got it right")
    return com
result=num()
print(result)


