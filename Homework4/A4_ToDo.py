from A4_Base import *

#______DO NOT EDIT ABOVE THIS LINE____________#
#use deque functions to add and remove frontier entries
#______EDITING BELOW THIS LINE IS ALLOWED, ONLY EDIT THE INTERNAL IMPLEMENTATION OF THE FUNCTIONS ____________#
#Ziheng (Tony) Fang & Ashwabh Bhatnagar
#SE/CS 156
#Homework 4

class AStarGraph(GraphProblem):
    #use this child class, Inherit from the GraphProblem class, in this class implement hueristic (h) function
    """h function is straight-line distance from a node's state to goal."""
    # in this case use the romania_map.locations attribute to compute h.
    def h(self, node):
        #YOUR CODE GOES HERE
        #obtain coordinates of current node and goal, get the straight line distance.
        goalCoordinates = romania_map.locations[self.goal]
        nodeCoordinates = romania_map.locations[node]
        return euclidean_distance(goalCoordinates, nodeCoordinates)



def astar_search(problem, h=None):
    """A* search is best-first (you may use priority queue) graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, (ALREADY ADDED in TEST CASE),
    The tests check through a call to solution() function which returns a list of expanded cities along the path"""

    # YOUR CODE GOES HERE
    h = h or problem.h
    f_value_initial = 0 + h(Node(problem.initial).state)
    frontier = [(f_value_initial, Node(problem.initial))]  # we begin with our start
    explored = set() # contains the set of nodes we explore

    while frontier:
        node = frontier.pop(0)[1] # get the first node in our priority queue
        '''Check to see if we've reached the goal.'''
        if problem.goal_test(node.state):
            return node
        explored.add(node.state) # add node to explored nodes
        '''Check every neighboring node.'''
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            '''If we have not explored the node.'''
            if child.state not in explored:
                f_value = child.path_cost + h(child.state)#f(n) = g(n) + h(n)
                frontier.append((f_value, child))#add value to our priority queue with the f value
                frontier.sort()#sort the queue
    '''If we could not find a path to the goal.'''
    return None