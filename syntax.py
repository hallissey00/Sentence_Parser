
import pandas as p
import time


def syntaxbracket(): 
    
    print("")
    print("")
    time.sleep(4)  
    print("____________*Syntax Brackets*____________")
    print("")

    syntaxmatrices = []
    childsize = 3
    treesize = 4
    l = 0
    while(treesize >= 0):
        if(treesize >= 0 or tree[treesize][l] != treesize[treesize-1][l]):
            print("[", end=""),
            print(tree[treesize][l], end=""),
            syntaxmatrices.append(tree[treesize][l])
            treesize = treesize-1
            if treesize < 0:
                print("]", end=""),
                treesize = childsize 
                childsize  = childsize -1
                l = l+1
    print("]")


    print("*____________________________*")
