def add(x, y):
    return x+y


def sub(x, y):
    answer = x - y
    return answer


def mult(x, y):
    return x*y


def div(x, y):
    return x/y


def get_numbers_from_user():
    num1 = get_integer_input('Enter the first number: ')
    num2 = get_integer_input('Enter the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)

    while not value_as_string.isnumeric:
        print('Input must be an integer')
        value_as_string = input(message)

    return int(value_as_string)


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu options are: ')
        print('\t1.Add')
        print('\t2.sub')
        print('\t3.mult')
        print('\t4.div')
        print('==========')
        user_selection = input('make a selection: ')
        if user_selection in ('1', '2', '3', '4'):
            input_ok = True
        else:
            print('Invalid selection(choose 1-4)')
    print('------------')
    return user_selection


def check_if_user_has_finished():
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('do you want to finish(yes/no): ')
        if user_input == 'yes':
            user_input_accepted = True
        elif user_input == 'no':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('input must be (yes/no)')
    return ok_to_finish


def start():
    print('simple calculator app')

    finished = False
    while not finished:
        result = 0
        menu_choice = get_operation_choice()
        n1, n2 = get_numbers_from_user()
        if menu_choice == '1':
            result = add(n1, n2)
        elif menu_choice == '2':
            result = sub(n1,n2)
        elif menu_choice == '3':
            result = mult(n1,n2)
        elif menu_choice == '4':
            result = div(n1,n2)

        print('Result', result)
        print('==========')

        finished = check_if_user_has_finished()

    print('BYE')


start()
