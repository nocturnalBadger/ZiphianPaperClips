import random
import matplotlib.pyplot as plt
import numpy

totalPaperClips = 1000
operationsToComplete = 300

class PaperClipChain:
    
    numberOfLinks = 1
    
    def linkWithOtherChain(otherChain):
        self.numberOfLinks += otherChain.numberOfLinks
        
        
def makeABunchOfPaperClips(allChains):
    global totalPaperClips
    
    while len(allChains) < totalPaperClips:
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

def makeGraph(listOfChainLengths):
    global operationsToComplete, totalPaperClips
    xSeries = numpy.linspace(0, 1, len(listOfChainLengths))
    plt.figure()
    plt.xlim(xmin = 0)
    plt.plot(xSeries, listOfChainLengths, ".")
    
    z = numpy.polyfit(xSeries, listOfChainLengths, 2)
    p = numpy.poly1d(z)
    plt.plot(xSeries, p(xSeries), "r-")
    
    # Visual
    plt.xlabel("Chain #")
    plt.ylabel("Chain Length")
    title = "Chain lengths after %i iterations over a pile of %i paperclips" % (operationsToComplete, totalPaperClips)
    plt.suptitle(title)
    plt.savefig("results.png")



# Main Stuff
pileOfChains = makeABunchOfPaperClips([])
operationsCompleted = 0

while operationsCompleted < operationsToComplete and len(pileOfChains) > 1:
    chainsToAdd = chooseChainsToAdd(pileOfChains)
    chainsToAdd[0].numberOfLinks += chainsToAdd[1].numberOfLinks
    pileOfChains.remove(chainsToAdd[1])
    operationsCompleted += 1
    
sortedListOfChainLengths = sorted([chain.numberOfLinks for chain in pileOfChains])[::-1]
makeGraph(sortedListOfChainLengths)







