class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None

class Circular_ll:

        def __init__(self):
                self.head=None

        def triversing(self):
                n=self.head
                if n is None:
                        print("SLL is empty...!")
                else:
                        while True:
                                print(n.data, end=" ")
                                n=n.ref
                                if n == self.head:
                                        break
                                        

        def add_begin(self,data):
                
                new_node=Node(data)
                
                if self.head is None:
                        self.head=new_node
                        new_node.ref=self.head
                else:
                        n=self.head
                        new_node.ref=self.head
                        
                        if self.head is not None:
                                while n.ref != n:
                                        n=n.ref
                                n.ref =new_node
                        else:
                                new_node.ref =new_node
                        self.head=new_node
                        
cc=Circular_ll()
cc.add_begin(10)
cc.add_begin(20)
cc.add_begin(300)
cc.triversing()
