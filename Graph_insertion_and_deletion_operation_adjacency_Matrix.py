def add_node(a):
        global counts
        if a in nodes:
                print("element is already present in the nodes")
        else:
                counts=counts+1
                nodes.append(a)
                for i in arrays:
                        i.append(0)
                temp=[0 for i in range(counts)]
                arrays.append(temp)


def add_edge(a,b,size):
        if a not in nodes:
                print(f"{a} is not present in the nodes ")
        elif b not in nodes :
                print(f"{b} is not present in the nodes ")
        else:
                index_1=nodes.index(a)
                index_2=nodes.index(b)
                arrays[index_1][index_2]=size
                arrays[index_2][index_1]=size
                
def delete_node(v):
        global counts
        if v not in nodes:
                print(f"{v} is not present in the graph")
        else:
                idx=nodes.index(v)
                counts-=1
                nodes.remove(v)
                arrays.pop(idx)
                for i in arrays:
                        i.pop(idx)


def delete_edge(v1,v2):
        if v1 not in nodes:
                print(f"{v1} not present in the graph")
        elif v2 not in nodes:
                print(f"{v2} not present in the graph")
        else:
                index1=nodes.index(v1)
                index2=nodes.index(v2)
                arrays[index1][index2]=0
                arrays[index1][index2]=0

                
def print_graph():
        for i in arrays :
                for j in i:
                        print(j,end=" ")
                print() 

nodes=[]
arrays=[]
counts=0
print("Before adding the node :-" )
print(nodes)

add_node("A")
add_node("B")
add_node("c")
add_node("d")
add_node("e")
add_node("f")

print("after adding nodes :-  " )
print(nodes)
add_edge("A","e",5)
add_edge("A","B",5)
add_edge("A","c",5)
print("matrix is :- ")
print_graph()
delete_node("d")
print("after deleting nodes  ")
print(nodes)
print_graph()






















