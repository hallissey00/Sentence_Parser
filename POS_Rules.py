
def POS_rules(): # grows the lists to  input sentence thats on the rules.
    for word in words: # For each line in sentence
        filtered = lexiconRules[lexiconRules.word == word]
        for row in filtered[['lexicon']].values:
                list.append(row[0])
        for row in filtered[['type']].values:
                type.append(row[0])

    tree[0] = words
    tree[1] = list
    for x in range(len(words)): # Populate the first row of the treeParents with values
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
