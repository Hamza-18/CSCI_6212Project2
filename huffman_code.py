import heapq
import time
import string
import random

class Node:
    def __init__(self, freq, char, left=None, right=None, dir=None):
        """create a node with frequency and character"""
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.code = ''
        
    def __lt__(self, next):
        """compare two nodes based on frequency"""
        return self.freq < next.freq    

class Encoder:
    def __init__(self, charArray ) -> None:
        """initialize the character array"""
        self.charArray = charArray    
        
    def huffmanPrefixArray(self,):
        """this method is used to generate huffman code for each distinct character"""
        nodes = []
        heapq.heapify(nodes)
        # append each distinct character to the nodes array
        # loop over the frequency array and push each character into heap
        for index in range(len(self.charArray)):
            if self.charArray[index] is not None:
                heapq.heappush(nodes,Node(self.charArray[index], chr(index)))
        # pop from the heap until there is one node left in heap
        while len(nodes) > 1:
            # extract two minimum nodes each time and then create one node combining there frequencies
            # append new node into heap and attach the two minimum nodes as left and right child of new node
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            left.code = '0'
            right.code = '1'
            newFreq = left.freq + right.freq

            newNode = Node(newFreq, left.char+right.char,left, right)
            heapq.heappush(nodes,newNode)

        # store the root node to get huffman code later
        self.tree =  heapq.heappop(nodes)

    def getHuffmanCode(self, node,lst, code=''):
        """get huffman code for each unique character"""
        # append the code for current branch
        newCode = code + node.code

        # traverse the left and right branch recursively
        if node.right:
            self.getHuffmanCode(node.right, lst, newCode)
        if node.left:
            self.getHuffmanCode(node.left, lst, newCode)
        
        if(not node.left and not node.right):
            # if node is leaf node then append the character and code to the list
            lst.append([node.char, newCode])

    def encode(self):
        """this method is used to encode the file"""
        encodeLst = []
        self.huffmanPrefixArray()
        self.getHuffmanCode(self.tree, encodeLst)

if __name__ == '__main__':
    # define unique characters
    n = 10000000000
    # generate random frequency array for each character
    char_array = [random.randint(1,100) for i in range(n+1)]
    start = time.time()
    encoder = Encoder(char_array)
    encoder.encode()
    end = time.time()
    print("Time taken to encode the file is: ", end-start)
