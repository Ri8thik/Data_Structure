class Node:
        def __init__(self,data):
                self.data=data
                self.nref=None
                self.pref=None

class Linked_list:
        def __init__(self):
                self.head=None
                
        def print_ll(self):
                if self.head is None:
                        print("LinkedList is empty..!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data, end=" ")
                                n=n.nref

        def print_ll_reverse(self):
                print()
                if self.head is None:
                        print("Linkedlist is empty..!")
                else:
                        n=self.head
                        while n.nref is not None:
                                n=n.nref
                        while n is not None:
                                print(n.data, end=" ")
                                n=n.pref

        def insert_empty(self,data):
                if self.head is None:
                        new_node=Node(data)
                        self.head=new_node
                else:
                        print("LinkedList is not empty...!")
                        
        def add_begin(self,data):
                new_node=Node(data)
                if self.head is None:
                        self.head =new_node
                else:
                        new_node.nref=self.head
                        self.head.pref=new_node
                        self.head=new_node

        def add_end(self,data):
                new_node=Node(data)
                if self.head is None:
                        self.head=new_node
                else:
                        n=self.head
                        while n.nref is not None:
                                n=n.nref
                        n.nref=new_node
                        new_node.pref=n


        def add_after(self,data,x):
                if self.head is None:
                        print("LisnkedList is empty....!")
                else:
                        n=self.head
                        while n is not None:
                                if x==n.data:
                                        break
                                n=n.nref
                        if n is None:
                                print("Element is not found...!")
                        else:
                                new_node=Node(data)
                                new_node.pref=n
                                new_node.nref=n.nref
                                if n.nref is not None:
                                        n.nref.pref = new_node
                                n.nref=new_node
                                
                

        def add_before(self,data,x):
                if self.head is None:
                        print("LinkList is empty...!")
                else:
                        n=self.head
                        while n is not None:
                                if n.data == x:
                                        break
                                n=n.nref
                        if n is None:
                                print("element is Not present ...!")
                        else:
                                new_node=Node(data)
                                new_node.pref=n.pref
                                new_node.nref=n

                                if n.pref is not None:
                                        n.pref.nref=new_node
                                else:
                                        self.head =new_node
                                n.pref =new_node


        def delete_begin(self):
                if self.head is None:
                        print("DLL is empty...!")
                        return
                if self.head.nref is None:
                        self.head = None
                        print("DDL becomes empty after delete this node...!")
                else:
                        self.head=self.head.nref
                        self.head.pref=None
                        

        def delete_end(self):
                if self.head is None:
                        print("DDL is empty..!")
                        return
                if self.head.nref is None:
                        self.head =None
                        print("DDL becomes empty after delete this node...!")
                else:
                        n=self.head
                        while n.nref is not None:
                                n=n.nref

                        n.pref.nref=None


        def delete_by_value(self,x):
                if self.head is None:
                        print("DDL is empty...!")
                        return
                
                if self.head.nref is None:
                        if x=self.head.data:
                                self.head=None
                                print("DDL becomes empty after delete this node...!")
                        else:
                                print("element is not found ...!")
                        return
                
                if self.head.data==x:
                        self.head=self.head.nref
                        self.head.pref=None
                        return
                
                n=self.head
                while n.nref is not None:
                        if n.data == x:
                                break
                        n=n.nref
                if n.nref is not None:
                        n.nref.pref=n.pref
                        n.pref.nref=n.nref
                else:
                        if n.data==x:
                                x.pref.nref=None
                        else:
                                print("element is not found ...!")

ll=Linked_list()
ll.insert_empty(20)
##ll.insert_empty(90)
ll.add_begin(99)
ll.add_begin(89)
ll.add_end(30)
ll.add_end(40)
ll.add_after(100,40)
ll.add_before(1000,40)
ll.delete_begin()
ll.delete_end()
ll.print_ll()
ll.print_ll_reverse()
