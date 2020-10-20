"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
def valid_parentheses(string):
    x=0
    for s in string:
        if s=='(':
            x+=1
        if s==')':
            x-=1
            if x==-1:
                return False
    if x==0:
        return True
    else:
        return False

a="hi())("
print(valid_parentheses(a))
