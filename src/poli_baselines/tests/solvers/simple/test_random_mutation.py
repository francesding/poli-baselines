"""This module tests the random mutation solver"""


def test_random_mutation_instantiates_and_runs_well():
    from poli_baselines.solvers import RandomMutation
    from poli import objective_factory

    problem = objective_factory.create(
        name="aloha",
    )
    f, x0 = problem.black_box, problem.x0
    y0 = f(x0)

    solver = RandomMutation(
        black_box=f,
        x0=x0,
        y0=y0,
    )

    solver.solve(max_iter=5)


def test_random_mutation_in_docs():
    import numpy as np

    from poli.objective_repository import AlohaProblemFactory
    from poli_baselines.solvers import RandomMutation

    problem_factory = AlohaProblemFactory()

    problem = problem_factory.create()
    f, x0 = problem.black_box, problem.x0
    y0 = f(x0)

    solver = RandomMutation(
        black_box=f,
        x0=x0,
        y0=y0,
    )

    solver.solve(max_iter=100)

    print(solver.get_best_solution())


if __name__ == "__main__":
    test_random_mutation_in_docs()
