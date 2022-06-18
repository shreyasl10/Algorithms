#Question
#Given a string containing the infix expression. Convert it to the postfix expression
#
#Sample Input
#a+b*(c^d-e)^(f+g*h)-i
#
#Sample Output
#abcd^e-fgh*+^*+i-


def Score(op):
    if op=='^':
        return 3
    elif op=='%' or op=='/' or op=='*':
        return 2
    elif op=='+' or op=='-':
        return 1
def InToPost(s):
    s=list(s)
    stack=[]
    post=[]
    for i in range(len(s)):
        if s[i].isalpha() or s[i].isnumeric():
            post.append(s[i])
        elif s[i]!=')':
            if (not stack or (s[i]=='(' or stack[-1]=='(')) or (stack and Score(s[i])>Score(stack[-1])):
                stack.append(s[i])
            elif (stack and Score(s[i])<=Score(stack[-1])):
                while(stack and (stack[-1]!='(' and Score(stack[-1])>=Score(s[i]))):
                    post.append(stack.pop())
                stack.append(s[i])
        elif s[i]==')':
            while(stack[-1]!='('):
                post.append(stack.pop())
            stack.pop()
            
    while stack:
        post.append(stack.pop())
    return ' '.join(post)
s=input("Enter the infix notation\n")
print(InToPost(s))
