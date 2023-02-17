def ifelse():
    time =int(input("Enter time : "))
    if time == 9:
            print("on time")
    elif time >9 and time <=10:
        print("10 min late")

    elif time >10 and time <=12:
        print("30 min late")        

    else:
        print("Zero marks")


if __name__=='__main__':
    ifelse()