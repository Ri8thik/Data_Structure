class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None
class linklist:
        def __init__(self):
                self.head=None
        def print_ll(self):
                n=self.head
                if n is None:
                        print("linklist is empty")
                else:
                        while n is not None:
                                print(n.data, end=" ")
                                n=n.ref
                                
        def add_begin(self,data):
                new_node=Node(data)
                new_node.ref=self.head
                self.head=new_node

        def add_end(self,data):
                new_node=Node(data)
                if self.head is None:
                        self.head=new_node
                else:
                        n=self.head
                        while n.ref is not None:
                                n=n.ref
                        n.ref=new_node

        def add_after(self,data,x):
                n=self.head
                while n is not None:
                        if x==n.data:
                                break
                        n=n.ref
                        
                if n is None:
                        print("element is not found ...!")
                else:
                        new_node=Node(data)
                        new_node.ref=n.ref
                        n.ref=new_node     

        def add_before(self,data,x):
                if self.head is None:
                        print("linklist is empty..!")
                        return 
                if self.head.data==x:
                        new_node=Node(data)
                        new_node.ref=self.head
                        self.head=new_node
                        return
                n=self.head
                while n.ref is not None:
                        if n.ref.data==x:
                                break
                        n=n.ref
                if n.ref is None:
                        print("Node is not found..!")
                else:
                        new_node=Node(data)
                        new_node.ref=n.ref
                        n.ref =new_node
  
        def insert_empty(self,data):
                if self.head is None:
                        new_node=Node(data)
                        self.head=new_node
                else:
                        print("list is not empty...!")


        def delet_begin(self):
                if self.head is None:
                        print("linked list is empty...!")
                else:
                        self.head=self.head.ref

        def delet_end(self):
                if self.head is None:
                        print("linked list is empty...!")
                elif self.head.ref is None:
                        self.head=None
                else:
                        n=self.head
                        while n.ref.ref is not None:
                                n=n.ref
                        n.ref = None

        def delet_by_value(self,x):
                if self.head is None:
                        print("linked list is empty...!")
                        return
                if self.head.data == x:
                        self.head=self.head.ref
                        return
                n=self.head
                while n.ref is not None:
                        if n.ref.data==x:
                                break
                        n=n.ref
                if n.ref is None:
                        print("element is not found")
                else:
                        n.ref=n.ref.ref
                        
                                    
ll1=linklist()
ll1.add_begin(20)
ll1.add_begin(600)
ll1.add_end(2000)
ll1.add_after(69,20)
ll1.add_before(80,69)
##ll1.insert_empty(10)
##ll1.insert_empty(20)
ll1.delet_begin()
ll1.delet_end()
ll1.delet_by_value(69)
ll1.print_ll()
