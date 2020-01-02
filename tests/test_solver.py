from io import StringIO
import pandas as pd

from seating_planner import solver


def test_solver():
    connection_matrix = """
    1,50,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    50,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,50,1,1,1,1,10,0,0,0,0,0,0,0,0
    1,1,50,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,1,1,50,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,1,50,1,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,1,1,1,1,50,1,0,0,0,0,0,0,0,0
    1,1,1,1,1,1,50,1,1,0,0,0,0,0,0,0,0
    1,1,10,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    0,0,0,0,0,0,0,0,0,1,50,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,50,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    """

    EXAMPLE_CONNECTIONS = [map(int, l.strip().split(" ")) for l in connection_matrix.strip().split("\n")]

    EXAMPLE_NAMES = """
    Deb
    John
    Martha
    Travis
    Allan
    Lois
    Jayne
    Brad
    Abby
    Mary
    Lee
    Annika
    Carl
    Colin
    Shirley
    DeAnn
    Lori
    """.strip().split("\n")

    planning_helper, plan = solver.solve(EXAMPLE_NAMES, EXAMPLE_CONNECTIONS, 9, 2)
    print(planning_helper.plan_to_people(plan))
