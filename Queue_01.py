queue=[]
def enqueue():
        a =int(input("enter a no :-\n"))
        queue.append(a)
        print(queue)
def dequeue():
        if not queue:
                print("queue is empty")
        else:              
                b=queue.pop(0)
                print(f"you remove :- {b}")
def show():
        print(queue)


while True:
        n=int(input("enter a no 1 add , 2 remove, 3 show,4 exit :-\n"))
        if n==1:
                enqueue()
        elif n==2:
                dequeue()
        elif n==3:
                show()
        elif n==4:
                break
        else:
                print("enter correct input")
                
