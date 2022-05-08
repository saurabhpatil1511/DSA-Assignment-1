# Program to find all pairs of integer array whose sum is equal to a given number
def printPairs(arr, n, sum):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)

# Program to reverse an array in place by updating orginal array
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
arr = arr[::-1]
print("Reversed array is")
print(arr)

def reverse_arr(arr):
    arr =  reversed(arr)
    return list(arr)
arr = [10, 20, 30, 40, 50]
reverse_arr(arr)

# Program to check if two strings are a rotation of each other
def rotation_check(s1, s2):
    if len(s1) == len(s2):
        temp = s1 + s1
        if temp.count(s2) > 0:
            return 1
    else:
        return 0
s1 = "ABCD"
s2 = "BCDA"
if rotation_check(s1, s2):
    print("Strings are rotation of each other")
else:
    print("Strings are not rotation!")

# Program to print the first non-repeated character from string.
def non_repeated(str1):
    for i in str1:
        count = str1.count(i)
        if count == 1:
            return i
            break
str1 = "vaibhav"
non_repeated(str1)

# Program to implement Tower of Hanoi Algorithm

def myfunc(n, A, C, B):
    if n == 0:
        return
    myfunc(n-1, A, B, C)
    print("Move disk", n, "from rod", A, "to rod", C)
    myfunc(n-1, B, C, A)

n = int(input())
myfunc(n, 'A', 'C', 'B')

# Program to convert postfix to prefix expression

def is_operator(n):
    if n == "+":
        return True
    if n == "-":
        return True
    if n == "/":
        return True
    if n == "*":
        return True
    return False

def post_pre(x):
    s = []
    length = len(x)
    for i in range(length):
        if (is_operator(x[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = x[i] + op2 + op1
            s.append(temp)
        else:
            s.append(x[i])
    ans = ""
    for i in s:
        ans += i
    return ans
x ="AB+CD-"
print("Prefix : ", post_pre(x))

# Program to convert prefix expression to infix expression

def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

str = "*-A/BC-/AKL"
print(prefixToInfix(str))

# Program to check if  all the  brackets are closed in a given snippet

def brackets_check(x):
    var = []
 
    for i in x:
        if i in ["(", "{", "["]:
            var.append(i)
            
        else:
            if not var:
                return False
            temp_char = var.pop()
            if temp_char == '(':
                if i != ")":
                    return False
            if temp_char == '{':
                if i != "}":
                    return False
            if temp_char == '[':
                if i != "]":
                    return False
 
    if var:
        return False
    return True

x = "{()}[(]"
    
if brackets_check(x):
    print("Balanced")
else:
    print("Not Balanced")

# Program to reverse stack

def reverse_stack(stack):
    stack = reversed(stack)
    return list(stack)
stack = [11,12,13,14,15]

print("Original Stack", *stack, sep='\n')
print("Reversed Stack", *reverse_stack(stack), sep='\n')

# Prpgram to find the smallest number using a stack

def min_value(stack):
    x=sorted(stack)
    return x[0]
    
stack=[50,7,4,3,-1]    
min_value(stack) 


