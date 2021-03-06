from seating_planner import solver


def test_solver():
    connection_matrix = """
    1,100,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    100,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,100,1,1,1,1,10,0,0,0,0,0,0,0,0
    1,1,100,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,1,1,100,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,1,100,1,1,1,1,0,0,0,0,0,0,0,0
    1,1,1,1,1,1,1,100,1,0,0,0,0,0,0,0,0
    1,1,1,1,1,1,100,1,1,0,0,0,0,0,0,0,0
    1,1,10,1,1,1,1,1,1,0,0,0,0,0,0,0,0
    0,0,0,0,0,0,0,0,0,1,100,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,100,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1
    """

    example_connections = [
        [int(value) for value in line.strip().split(',')]
        for line in connection_matrix.strip().split('\n')
    ]

    example_names = """
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

    planning_helper, plan = solver.solve(example_names, example_connections, 9, 2)
    print(planning_helper.plan_to_people(plan))
