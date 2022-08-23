def List_rule(child, syntaxtree): # will use the list to pick each child in the tree to match the word
    collection = 0
    l = 0
    while(l < len(child)): # each child

#child,parent
#VP NP,S
#N DET,NP
#VP V,VP
#DET ADJ N,NP

                   
        if (child[l] == "NP") and (child[l+1] == "VP"): 
            tree[syntaxtree+1].append("S")
            for x in range(2):
                roottree[syntaxtree].append(collection)
                l+=1
        elif (child[l] == "V") and (child[l+1] == "NP"):
            tree[syntaxtree+1].append("VP")
            for x in range(2):
                roottree[syntaxtree].append(collection)
                l+=1
        elif (child[l] == "DET") and (child[l+1] == "N"):
            tree[syntaxtree+1].append("NP")
            for x in range(2):
                roottree[syntaxtree].append(collection)
                l+=1
        elif (child[l] == "DET") and (child[l+1] == "ADJ") and (child[l+2] == "N"): 
            tree[syntaxtree+1].append("NP")
            for x in range(3): # Since this rule uses 3 childs mean move on next one
                roottree[syntaxtree].append(collection)
                l+=1
            
        else:
            tree[syntaxtree+1].append(child[l]) # If none rule appear we move on         
            l+=1
        


          