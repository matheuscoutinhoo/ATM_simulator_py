
opt= int(input('Hello. How can we help you?\n[1] - Deposit\n[2] - Check balance\n[3] - Withdraw\n[4] - exit '))
balance = 0

while True:
    if opt == 1:
        dep = float(input('How many do you want to deposit: '))
        balance = balance + dep
        print(f'Your balance now is R$ {balance:.2f}')
        repeater = (input('Do you want to continue? (y/n) ')).lower()
        repeater.strip()
        if repeater == 'y':
            opt = int(input('Hello. How can we help you?\n[1] - Deposit\n[2] - Check balance\n[3] - Withdraw\n[4] - exit '))
        else:
            print('Ok. Thanks.')
            break

    elif opt == 2:
        print(f'Your balance right now is R$ {balance}')
        if balance == 0:
            print('You do not have any balance. Please make a deposit.')
        repeater = (input('Do you want to continue? (y/n) ')).lower()
        repeater.strip()
        if repeater == 'y':
            opt = int(input('Hello. How can we help you?\n[1] - Deposit\n[2] - Check balance\n[3] - Withdraw\n[4] - exit '))
        else:
            print('Ok. Thanks.')
            break

    elif opt == 3:
        if balance == 0:
            print('You do not have any balance. Please make a deposit.')
            repeater = (input('Do you want to continue? (y/n) ')).lower()
            repeater.strip()
            if repeater == 'y':
                opt = int(input('Hello. How can we help you?\n[1] - Deposit\n[2] - Check balance\n[3] - Withdraw\n[4] - exit '))
            else:
                print('Ok. Thanks.')
                break
        else:
            withdraw = int(input('How many do you want to withdraw: '))
            balance = balance - withdraw
            print(f'You have withdrawed R$ {withdraw}.\nYour balance now is R$ {balance}')
            repeater = (input('Do you want to continue? (y/n) ')).lower()
            repeater.strip()
            if repeater == 'y':
                opt = int(input('Hello. How can we help you?\n[1] - Deposit\n[2] - Check balance\n[3] - Withdraw\n[4] - exit '))
            else:
                print('Ok. Thanks.')
                break

    elif opt == 4:
        print('Thank you')
        break


