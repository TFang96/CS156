from A3_Base import *
from A3_ToDo import *

#NOTE: DO NOT EDIT THIS FILE
#NOTE: ONLY USE THIS FILE TO TEST IF YOUR IMPLEMENTATION IS CORRECT
# The test cases will run individual instances of the problem and print "PASSED" if your implementation is correct.

def test_breadth_first_graph_search():
    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    assert breadth_first_graph_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']
    romania_problem = GraphProblem('Arad', 'Neamt', romania_map)
    assert breadth_first_graph_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest', 'Urziceni', 'Vaslui', 'Iasi', 'Neamt']
    romania_problem = GraphProblem('Arad', 'Giurgiu', romania_map)
    assert breadth_first_graph_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest', 'Giurgiu']


# the test cases will run individual instances of the problem and print "PASSED" if your implementation is correct.

def test_depth_first_graph_search():
    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    assert depth_first_graph_search(romania_problem).solution() == ['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
    romania_problem = GraphProblem('Arad', 'Neamt', romania_map)
    assert depth_first_graph_search(romania_problem).solution() == ['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest', 'Urziceni', 'Vaslui', 'Iasi', 'Neamt']
    romania_problem = GraphProblem('Arad', 'Giurgiu', romania_map)
    assert depth_first_graph_search(romania_problem).solution() == ['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest', 'Giurgiu']
