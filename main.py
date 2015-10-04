import random
import matplotlib.pyplot as plt

class PaperClipChain:
    
    numberOfLinks = 1
    
    def linkWithOtherChain(otherChain):
        self.numberOfLinks += otherChain.numberOfLinks
        
        
def makeABunchOfPaperClips(allChains):
    ammountOfChainsToMake = 1000
    
    while len(allChains) < ammountOfChainsToMake:
        allChains.append(PaperClipChain())
    return allChains
        
def chooseChainsToAdd(allChains):
    expandedPileOfChains = []
    for chain in allChains:
        i = 0
        while i < chain.numberOfLinks:
            expandedPileOfChains.append(chain)
            i += 1
            
    #print "There are %i paperclips." % len(expandedPileOfChains)
    indexOfFirstChain = random.randint(0, len(expandedPileOfChains) - 1)
    firstChain = expandedPileOfChains[indexOfFirstChain]
    
    secondChain = firstChain
    while firstChain == secondChain:
        indexOfSecondChain = random.randint(0, len(expandedPileOfChains) - 1)
        secondChain = expandedPileOfChains[indexOfSecondChain]
    
    return (firstChain, secondChain)

def printChainLengths(pileOfChains):
    #print "There are a total of %i chains" % len(pileOfChains)
    for chain in pileOfChains:
        print chain.numberOfLinks

def makeGraph(listOfChainLengths):
    xSeries = [1]
    while len(xSeries) < len(listOfChainLengths):
        xSeries.append(len(xSeries))
    plt.figure()
    #plt.xlim(xmax = len(listOfChainLengths) / 4)
    plt.plot(xSeries, listOfChainLengths, ".")
    plt.savefig("results.png")



# Main Stuff
pileOfChains = makeABunchOfPaperClips([])
operationsToComplete = 500
operationsCompleted = 0

while operationsCompleted < operationsToComplete and len(pileOfChains) > 1:
    chainsToAdd = chooseChainsToAdd(pileOfChains)
    chainsToAdd[0].numberOfLinks += chainsToAdd[1].numberOfLinks
    pileOfChains.remove(chainsToAdd[1])
    operationsCompleted += 1
    
sortedListOfChainLengths = sorted([chain.numberOfLinks for chain in pileOfChains])[::-1]
makeGraph(sortedListOfChainLengths)


#print "Preformed %i operations" % operationsCompleted
#printChainLengths(pileOfChains)







