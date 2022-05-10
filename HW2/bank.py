print("Deposit(d) or withdrawal(w) or balance check (c)??", end=" ")
command = input().rstrip()
balance = 0

def exception(command):
    print("There is no button like",command)
    print("Deposit(d) or withdrawal(w) or balance check (c)??", end=" ")
    command = input().rstrip()
    if command != 'q' and command != 'w' and command != 'd' and command != 'c':
        command = exception(command)
    return command

def deposit(balance):
    print("How much do you want to deposit?", end=" ")
    depositAmount = int(input())
    print("You deposited",depositAmount,"won")
    return balance + depositAmount

def withdrawal(balance):
    print("How much do you want to withdrawal?", end=" ")
    debit = int(input())
    print("You've withdrawn",debit,"won")
    if debit > balance:
        print("But you only have",balance,"won")
        return balance
    else:
        return balance - debit
        
def check(balance):
    print("Your current balance is",balance,"won")

while command != 'q':
    # Calling an exception handling function when input other than q,w,d,c is received
    if command != 'q' and command != 'w' and command != 'd' and command != 'c':
        command = exception(command)
        continue

    # When the user enters d, the deposit function is called to deposit
    if command == 'd':
        balance = deposit(balance)
    
    # When the user inputs w, the withdrawal function is called to withdraw
    elif command == 'w':
        balance = withdrawal(balance)

    # When the user inputs c, the check function is called and the balance is printed.
    elif command == 'c':
        check(balance)
    
    # When the user inputs q, the conditional expression of the while statement returns to the end of the while statement.
    else:
        continue

    print("Deposit(d) or withdrawal(w) or balance check (c)??", end=" ")
    command = input().rstrip()
    