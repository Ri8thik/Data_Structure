class BST:
        def __init__(self,key):
                self.key=key
                self.rchild=None
                self.lchild=None

        def insert(self,data):
                if self.key is None:
                        self.key=data
                        return
                if self.key==data:
                        return
                if self.key >data:
                        if self.lchild:
                                self.lchild.insert(data)
                        else:
                                self.lchild=BST(data)
                else:
                        if self.rchild:
                                self.rchild.insert(data)
                        else:
                                self.rchild=BST(data)


        def search(self,data):
                if self.key == data:
                        print("Node is found...!")
                        return
                if self.key>data:
                        if self.lchild:
                                self.lchild.search(data)
                        else:
                                print("ELEMENT not found...!")
                else:
                        if self.rchild:
                                self.rchild.search(data)
                        else:
                                print("ELEMENT not fouund...!")

                
        def preorder(self):
                print(self.key,end=" ")
                if self.lchild:
                        self.lchild.preorder()
                if self.rchild:
                        self.rchild.preorder()

        def inorder(self):
                if self.lchild:
                        self.lchild.inorder()
                print(self.key,end=" ")
                if self.rchild:
                        self.rchild.inorder()
                

        def postorder(self):
                if self.lchild:
                        self.lchild.postorder()
                if self.rchild:
                        self.rchild.postorder()
                print(self.key, end=" ")
                

        def delete(self,data):
                if self.key is None:
                        print("Tree is empty ...!")
                        return
                if self.key>data:
                        if self.lchild:
                                self.lchild=self.lchild.delete(data)
                        else:
                                print("Element is not found ....!")
                elif self.key<data:
                        if self.rchild:
                                self.rchild=self.rchild.delete(data)
                        else:
                                print("Element is not found ....!")
                else:
                        if self.lchild is None:
                                temp =self.rchild
                                self=None
                                return temp
                        if self.rchild is None:
                                temp =self.lchild
                                self=None
                                return temp
                        node=self.rchild
                        while node.lchild:
                                node=node.lchild
                        self.key=node.key
                        self.rchild = self.rchild.delete(node.key)
                return self
                 

        def min_node(self):
                current=self
                while current.lchild:
                        current=current.lchild
                print(f"The min node is {current.key}")

        def max_node(self):
                current=self
                while current.rchild:
                        current=current.rchild
                print(f"The max node is {current.key}")
                



root=BST(None)
root.insert(10)
lists=[6,3,1,6,98,3,7]
for i in lists:
        root.insert(i)

print("PRE-Order")
root.preorder()
print()
print("IN-Order")
root.inorder()
print()
print("POST-Order")
root.postorder()
##print()
##root.delete(6)
##print("PRE-Order after delete a node")
##root.preorder()
print()
root.min_node()
root.max_node()





                        
