import pandas as p
import time

def Treesystem(): 
    time.sleep(5)
    print("")
    print("")
    print("____________*Lexicon tree*____________")

    l = len(tree)-1
    while l >= 0:
        print("["+str(l)+"] "+str(tree[l]))
        l=l-1
    print("")
    print("")
    time.sleep(3)    
    print("____________*Index tree*____________")
    l = len(tree)-1
    while l >= 0:
        print("["+str(l)+"] "+str(roottree[l]))
        l=l-1