stack=[]
def push():
        if len(stack)==l:
                print("stack is full")
        else:        
                a=input("enter a element :- \n")
                stack.append(a)
                print(stack)

def pop():
        if not stack:
                print("stack is empty")
        else:
                b=stack.pop()
                print(f"you remove this {b}")
                print(stack)
l=int(input("enter the length of the stack :- \n"))
while True:
        n=int(input("enter a no 1 push , 2 pop , 3 exit!:- \n"))
        if n==1:
                push()
        elif n==2:
                pop()
        elif n==3:
                break
        else:
                print("you enter a wronge input")
                
