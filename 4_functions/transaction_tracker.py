def after_transaction(balance, transaction):
    result = balance + transaction
    if(result < 0):
        # user does not have enough to withdraw
        print('INVALID ACTION. You do not have enough money ot withdraw')
        return balance
    
    print(result)
    return result

after_transaction(500,20)
after_transaction(300,-200)
after_transaction(3,-20)
after_transaction(20,-20)
