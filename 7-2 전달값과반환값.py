def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commision = 100
    return commision, balance - money - commision

balance = 10000
commision, balance = withdraw_night(balance, 5000)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commision, balance))