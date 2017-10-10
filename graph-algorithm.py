# -*- coding: utf-8 -*-
"""
@author: Hiep Nguyen
"""

def shortest_list(lists):
    """
    Purpose: this function takes a list of list and return the shortest list in the
    list of list
    Argument: a list of list
    Output: the shortest list in the list of list
    """
    lengths=[]
    for sublist in lists:
        lengths.append(len(sublist))
    shortest=min(lengths)
    for sublist in lists:
        if len(sublist)==shortest:
            return sublist
        
def shortest_path(graph,start,end):#This is the intial call to the recursive function
    """
    Purpose: This function takes a graph as a dictionary, a start node and an end
    node. It will find the shortest distance between any two connected nodes
    in the graph.
    Argument: graph is a dictionary representing connected nodes, a start node,
    and an end node (keys from the dictionary).
    Output: A list that has the the shortest path between two given nodes
    """
    def shortest_recur(graph,start,end,road):
        road=road+[start]#start adding node to the path
        allpaths=[]#an empty list to store paths as lists
        if start==end:#base case
            return [road]
        else:
            for node in graph[start]:#iterating all the the nodes connected to the given node.
                if node not in road:#Start looking for node to be added in path
                    routes=shortest_recur(graph,node,end,road)#call itself recursively using the current node as a start
                    for i in routes:
                        allpaths.append(i)#Store all the paths in a list of lists
            return allpaths
    if len(shortest_recur(graph,start,end,[]))==0:#Consider the case where there is not a path between two nodes
        return None
    else:
        return shortest_list(shortest_recur(graph,start,end,[]))#Using the shortest list function above to return the shortest path


        
import copy as c
def cycle(graph,node):
    """
    Purpose: This function takes a graph and a node and detects if there is a cycle starting
    and ending with that node.
    Argument: A dictionay representing a graph and a node(key from the dictionary)
    Output: A list starting and ending with node and a statement "cycle exisits" if
    there is a cycle starts and ends with this node.Otherwise, the function will return
    an empty list and prints "no cycle"
    """
    count=0#keep counting the index of the dictionary value
    if graph[node]==[]:#Consider the case where a node stands alone
        print("no cycle")
        return []
    else:
        for i in graph[node]:#iterate the connected node
            graph_dup=c.deepcopy(graph)#make a deep copy of the dictionary
            cut=graph_dup[node].pop(count)#Cut the direct connection of the node once at a time
            path=shortest_path(graph_dup,node,cut)#Check if there is still a path from the given node to the node that has recently been cut
            count+=1
        if path is None:#If there is no other path between two nodes,there is no cycle
            print ("no cycle")
            return []
        else:#If there is still a path between two nodes, then a cycle exists
            path.append(node)
            print("cycle exists")
            return path