# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Jacob Taylor : 2117518
# Laurie Bédard-Coté : 2086165

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem:SearchProblem)->List[Direction]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = []

    while not stack.isEmpty():
        state, path = stack.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                stack.push((successor[0], path + [successor[1]]))

def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    """Search the shallowest nodes in the search tree first."""

    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    visited = []

    while not queue.isEmpty():
        state, path = queue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                queue.push((successor[0], path + [successor[1]]))


def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    """Search the node of least total cost first."""

    priorityQueue = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), [], 0), 0)
    visited = []

    while not priorityQueue.isEmpty():
        state, path, cost = priorityQueue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                priorityQueue.push((successor[0], path + [successor[1]], cost + successor[2]), cost + successor[2])



def nullHeuristic(state:GameState, problem:SearchProblem=None)->List[Direction]:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    """Search the node that has the lowest combined cost and heuristic first."""

    priorityQueue = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    visited = []

    while not priorityQueue.isEmpty():
        state, path, cost = priorityQueue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                priorityQueue.push((successor[0], path + [successor[1]], cost + successor[2]), cost + successor[2] + heuristic(successor[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
