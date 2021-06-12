def add_nodes(a):
        if a in dicts :
                print(f"{a} is already present in the dicts")
        else:
                dicts[a]=[]



def add_edge(a,b):
        if a not in dicts:
                print(f"{a} is already present in the dicts ")
        elif b not in dicts:
                print(f"{b} is present in the list")
        else:
                ##list1=[b,cost]
                ##list2=[a,cost]
                dicts[a].append(b)
                dicts[b].append(a)
                
def delete_node(v):
        if v not in dicts:
                print(f"{v} is not present in the graph")
        else:
                dicts.pop(v)
                for i in dicts:
                        l=dicts[i]
                        if v in l:
                                l.remove(v)

def delete_edge(v1,v1,cost):
        if v1 not in dicts:
                print(f"{v1} is not present in the graph")
        elif v2 not in dicts:
                print(f"{v2} is not present in the graph")
        else:
                temp1=[v1,cost]
                temp2=[v2,cost]
                if temp2 in dicts[v1]:
                        dicts[v1].remove(temp2)
                        dicts[v2].remove(temp1)
                        


dicts={}
add_nodes("A")
add_nodes("B")
add_nodes("C")
add_nodes("D")
add_edge("A","B")
add_edge("A","C")
print(dicts)
delete_node("D")
delete_node("B")
print(dicts)
