from allSourcesPaths import *
from singleSourcePaths import *
from graph import *
from msts import *
from basicGraphAlgorithms import *
from encodeGraph import *
import sys
from test import *

def testsssp():
    
    w = {
    ('v1', 'v2'): 2,
    ('v1', 'v4'): 1,
    ('v2', 'v4'): 3,
    ('v2', 'v5'): 10,
    ('v3', 'v1'): 4,
    ('v3', 'v6'): 5,
    ('v4', 'v3'): 2,
    ('v4', 'v5'): 2,
    ('v4', 'v6'): 8,
    ('v4', 'v7'): 4,
    ('v5', 'v7'): 6,
    ('v7', 'v6'): 1,
}
G = {
    'v1': {'v2', 'v4'},
    'v2': {'v4', 'v5'},
    'v3': {'v1', 'v6'},
    'v4': {'v3', 'v5', 'v6', 'v7'},
    'v5': {'v7'},
    'v7': {'v6'}
}

s = 'v1'

distances = dijkstra_shortest_path(G, w, s)
print(distances)


'''def testccDP():
    

def testMCM():
    

def testprint():
    

def testobst():
    '''
    
def main():
    #testcounting()
    #testccDP()
    #testMCM()
    #testprint()
    testsssp()

if __name__ == '__main__':
    main()