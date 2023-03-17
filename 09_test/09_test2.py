def convert():
    num=int(input("enter number of seconds : "))
    hours=num//3600
    munites=(num%3600)//60
    seconds=(num%3600)%60

    print('number of hours',hours)
    print('number of munites',munites)
    print('number of seconds',seconds)

convert()