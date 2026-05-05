def spam():
    global eggs 
    eggs = 'spam global'
    print(eggs)

def bacon(): 
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

# 1 eggs = global
# 2 bacon() is called
# 3 bacon() local eggs variable is created
# 4 spam() is called
# 5 spam() modifies the global eggs variable to = spam global