import random

class PaperClipChain:
    
    numberOfLinks = 1
    
    def linkWithOtherChain(otherChain):
        self.numberOfLinks += otherChain.numberOfLinks
        
        
def makeABunchOfPaperClips(allChains):
    ammountOfChainsToMake = 100
    
    while len(allChains) < ammountOfChainsToMake:
        allChains.append(PaperClipChain)
    return allChains
        
def chooseChainsToAdd(allChains):
    expandedPileOfChains = []
    for chain in allChains:
        i = 0
        while i < chain.numberOfLinks:
            expandedPileOfChains.append(chain)
            
    indexOfFirstLink = random.randint(0, len(expandedPileOfChains))
    firstChain = expandedPileOfChains[indexOfFirstLink]
    
    indexOfSecondLink = random.randint(-1, (len(expandedPileOfChains) + 1))
    secondLink = expandedPileOfChains[indexOfSecondLink]
    
    return (firstLink, secondLink)
def printChainLengths(pileOfChains):
    for chain in pileOfChains:
        print len(chain) + "\n"

pileOfChains = makeABunchOfPaperClips([])
operationsToComplete = 1
operationsCompleted = 0

while operationsCompleted < operationsToComplete:
    chainsToAdd = chooseChainsToAdd(pileOfChains)
    chainsToAdd[0].linkWithOtherChain(chainsToAdd[1])
    pileOfChains.remove(chainsToAdd[1])
    operationsCompleted += 1
    
printChainLengths(pileOfChains)