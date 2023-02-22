def hi():
    print("Morning")

hi()

def hello(name):
    print("Hello",name)

hello("Drongo")

# passing parameters with type type definef
def multiply(a:int,b:int):

    answer = a * b
    print(answer)
    return answer


result = multiply(5, 10)
print(result)


def hello(name1, name2, name3):
    print("Hello", name1, "\nHi", name2, "\nHola", name3)


hello("Ouma", "Kelvin", "Okumu")
