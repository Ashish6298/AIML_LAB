import math
import pandas as pd

def infoGain(P, N):
   
    return -P / (P + N) * math.log2(P / (P + N)) - N / (P + N) * math.log2(N / (P + N))

def insertNode(tree, addTo, Node):
  
    for k, v in tree.items():
        if isinstance(v, dict):
            tree[k] = insertNode(v, addTo, Node)
    if addTo in tree:
        if isinstance(tree[addTo], dict):
            tree[addTo][Node] = 'None'
        else:
            tree[addTo] = {Node: 'None'}
    return tree

def insertConcept(tree, addTo, Node):
   
    for k, v in tree.items():
        if isinstance(v, dict):
            tree[k] = insertConcept(v, addTo, Node)
    if addTo in tree:
        tree[addTo] = Node
    return tree

def getNextNode(data, AttributeList, concept, conceptVals, tree, addTo):
    
    Total = data.shape[0]
    if Total == 0:
        return tree
    
    countC = {}
    for cVal in conceptVals:
        dataCC = data[data[concept] == cVal]
        countC[cVal] = dataCC.shape[0]
        
    if countC[conceptVals[0]] == 0:
        tree = insertConcept(tree, addTo, conceptVals[1])
        return tree
    
    if countC[conceptVals[1]] == 0:
        tree = insertConcept(tree, addTo, conceptVals[0])
        return tree
    
    ClassEntropy = infoGain(countC[conceptVals[1]], countC[conceptVals[0]])
    
    Attr = {}
    for a in AttributeList:
        Attr[a] = list(set(data[a]))
        
    AttrCount = {}
    EntropyAttr = {}
    for att in Attr:
        for vals in Attr[att]:
            for c in conceptVals:
                iData = data[data[att] == vals]
                dataAtt = iData[iData[concept] == c]
                AttrCount[c] = dataAtt.shape[0]
            TotalInfo = AttrCount[conceptVals[1]] + AttrCount[conceptVals[0]]
            if AttrCount[conceptVals[1]] == 0 or AttrCount[conceptVals[0]] == 0:
                InfoGain = 0
            else:
                InfoGain = infoGain(AttrCount[conceptVals[1]], AttrCount[conceptVals[0]])
                
            if att not in EntropyAttr:
                EntropyAttr[att] = (TotalInfo / Total) * InfoGain
            else:
                EntropyAttr[att] = EntropyAttr[att] + (TotalInfo / Total) * InfoGain
                
    Gain = {}
    for g in EntropyAttr:
        Gain[g] = ClassEntropy - EntropyAttr[g]
        
    Node = max(Gain, key=Gain.get)
    
    tree = insertNode(tree, addTo, Node)
    for nD in Attr[Node]:
        tree = insertNode(tree, Node, nD)
        newData = data[data[Node] == nD].drop(Node, axis=1)
        AttributeList = list(newData)[:-1]
        tree = getNextNode(newData, AttributeList, concept, conceptVals, tree, nD)
    return tree

def main():
    data = pd.read_csv('PlayTennis.csv')
    print(data)
    AttributeList = list(data)[:-1]
    concept = str(list(data)[-1])
    conceptVals = list(set(data[concept]))
    tree = getNextNode(data, AttributeList, concept, conceptVals, {'root': 'None'}, 'root')
    print(tree)

if __name__ == "__main__":
    main()