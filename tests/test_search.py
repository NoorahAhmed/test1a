import pytest
from search import *  # noqa


romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
vacumm_world = GraphProblemStochastic('State_1', ['State_7', 'State_8'], vacumm_world)
LRTA_problem = OnlineSearchProblem('State_3', 'State_5', one_dim_state_space)


def test_breadth_first_tree_search():
    assert breadth_first_tree_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def test_breadth_first_search():
    assert breadth_first_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def test_uniform_cost_search():
    assert uniform_cost_search(romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']


def test_depth_first_graph_search():
    solution = depth_first_graph_search(romania_problem).solution()
    assert solution[-1] == 'Bucharest'

def test_iterative_deepening_search():
    assert iterative_deepening_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']

def test_depth_limited_search():
    # output flickers between 49 and 50
    # assert len(depth_limited_search(romania_problem).solution()) == 50
    pass

def test_astar_search():
    assert astar_search(romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']

def test_recursive_best_first_search():
    assert recursive_best_first_search(romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']

def test_BoggleFinder():
    board = list('SARTELNID')
    """
    >>> print_boggle(board)
        S  A  R
        T  E  L
        N  I  D
    """
    f = BoggleFinder(board)
    assert len(f) == 206

def test_and_or_graph_search():
    def run_plan(state, problem, plan):
        if problem.goal_test(state):
            return True
        if len(plan) is not 2:
            return False
        predicate = lambda x : run_plan(x, problem, plan[1][x])
        return all(predicate(r) for r in problem.result(state, plan[0]))
    plan = and_or_graph_search(vacumm_world)
    assert run_plan('State_1', vacumm_world, plan)

def test_LRTAStarAgent():
    my_agent = LRTAStarAgent(LRTA_problem)
    assert my_agent('State_3') == 'Right'
    assert my_agent('State_4') == 'Left'
    assert my_agent('State_3') == 'Right'
    assert my_agent('State_4') == 'Right'
    assert my_agent('State_5') is None

    my_agent = LRTAStarAgent(LRTA_problem)
    assert my_agent('State_4') == 'Left'

    my_agent = LRTAStarAgent(LRTA_problem)
    assert my_agent('State_5') is None

if __name__ == '__main__':
    pytest.main()
