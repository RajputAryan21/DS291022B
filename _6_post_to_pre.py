def isOperator(x):
 
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "/":
        return True
    if x == "*":
        return True
 
    return False  
 
def postToPre(post_exp):
 
    data = []
 
    length = len(post_exp)
 
    for i in range(length):
 
        if (isOperator(post_exp[i])):
 
            op1 = data[-1]
            data.pop()
            op2 = data[-1]
            data.pop()
 
            temp = post_exp[i] + op2 + op1
 
            data.append(temp)
 
        else:
 
            data.append(post_exp[i])
 
    
    ans = ""
    for i in data:
        ans += i
    return ans
 
 
if __name__ == "__main__":
 
    post_exp = input("Enter a postfix expression: ")
     
    print("Prefix : ", postToPre(post_exp))