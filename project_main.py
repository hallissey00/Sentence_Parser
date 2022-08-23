import pandas as p
import time

#from POS_Rules import  POS_rules
#from Lists_Rule import  List_rule
#from Valid_Statement import  valid
#from tree import  Treesystem
#from syntax import syntaxbracket 
  

rulesSyntax = p.read_csv('Rules_Syntax.csv', delimiter=",")
lexiconRules = p.read_csv('Rules_Lexicon.csv', delimiter=",")
#words = "A boy bites white cat".lower().split()
ruleschild = rulesSyntax["child"].tolist()
rulesparents = [ [] , rulesSyntax["parent"].tolist()]
#words = "A boy likes the white cat".lower().split()
words = "A girl bites the white cat".lower().split()
# words = "A girl likes the white cat".lower().split()
# words = "The boy bites the white cat".lower().split()
# words = "The boy likes the white cat".lower().split()
# words = "The girl bites the white cat".lower().split()
# words = "The girl likes the white cat".lower().split()
# words = "The girls bite the white cat".lower().split()
# words = "The girls like the white cat".lower().split()
# words = "The boys bite the white cat".lower().split()
# words = "The boys like the white cat".lower().split()



list = []
type = []
tree = [[],[],[],[],[]]
roottree = [[],[],[],[],[]]
x=0
while(x < len(ruleschild)): 
    rulesparents[0].append(ruleschild[x].split())
    x+=1 ##split the childs and parent rules


def POS_rules(): # grows the lists to  input words.
    for word in words: #  each line in words
        create = lexiconRules[lexiconRules.word == word]
        for row in create[['lexicon']].values:
                list.append(row[0])
        for row in create[['type']].values:
                type.append(row[0])

    tree[0] = words
    tree[1] = list
    for x in range(len(words)): # Populate first row with values
        roottree[0].append(x)

    print("____________*Rules, Words, Lexicons and Types*____________") 
    print("RULES: " + str(rulesparents))
    print("")
    print("WORDS : "+ str(words))
    print("")
    print("LEXICONS : "+ str(list))
    print("")
    print("TYPES  : "+ str(type))
    print("")
    time.sleep(4)


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
        


#def valid(): 



    #if(val == True):
       # print("Acepted")
   # else:
       # print("Rejected")
  #  print("*____________________________*") 

  ##this will print all the trees to the system

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

POS_rules()
x=1
while(x <= 3): # Calls fuction list rule to create the level for the lexicon
    List_rule(tree[x], x)
    x = x+1
Treesystem()
syntaxbracket()
#end

##Julys attempt to fix the bracket 
#def syntaxbracket(words):
   # words_str= '[S1[S[NP['
    #if repr(words[0]) == "'the'":
      #   words_str += "DT the]"

    #elif repr(words[0]) == "'a'":
     #   words_str += "DT a]"
      #  words_str += "DT a]"

    #else:
     #   return

    #if repr(words[1]) in "'men'":
     #   if repr(words[0]) in ("'a'"):
      #      return
       # else:
        #    x = repr(words[1])
         #  words_str += "[NNP "+ x[1:-1] +"]"
#
 #   elif repr(words[1]) in "'man'":
   #     if repr(words[0]) in ("'a'"):
  #          return
    #    else:
     #           x = repr(sentence[1])
      #          words_str += "[NNP "+ x[1:-1]+"]"
 #       return






