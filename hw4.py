# -*- coding: utf-8 -*-
"""hw4_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vmf2Uup8bW7JzH-82HnqvXahZVDmYlBI
"""

"""
CS161 | hw4.py
"""

##### Feel free to modify the classes/functions as you need #####

def largestAlligator(W):
    """
    Returns the width of the largest alligator that can travel from pond 0 to pond n-1
    Parameters
    ------------
    n : int
        The number of ponds
    W : vector<vector<int>>
        The adjacency matrix of the swamp,
        W[i][j] represents the width of the channel between ponds i and j,
        or is 0 if there is no channel between those ponds
    ------------
    """
    ans = modified_dijkstra(W,0)
    ###### TODO: YOUR CODE HERE #####
    return ans
def getNextMaxNotSure(M, sure):
  max = float('-inf')
  max_node = -1
  for i in range(n):
    if M[i] > max and sure[i]==False:
      max_node = i
      max = M[i]
  return max_node

#Dijkstra but assigns to nodes the maximum min edge weight to get to them
def modified_dijkstra(M,start):
  d = [float('-inf') for i in range(n)]
  d[start] = float('inf') #this makes it the first in search, and not assigned to the
  at_destination = []		#neighboring nodes since we don't know the threshold
  sure = [False for i in range(n)]
  
  while any(s==False for s in sure):
    curr = getNextMaxNotSure(d, sure)
    for v in range(n):
      #minimum of the current path vs other path's threshold
      d[v] = max(d[v], min(d[curr], M[curr][v]))
       
    sure[curr] = True
  return d[n-1]

n = int(input())
W = []
for i in range(n):
    W.append(list(map(int, input().split())))
print(largestAlligator(W), end="")