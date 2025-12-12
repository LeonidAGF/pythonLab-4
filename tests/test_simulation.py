from src.simulation import run_simulation, get_new_isbn, get_new_year, get_new_str


def test_simulation():
    """
        Тесты для simulation
    """
    assert run_simulation(0)==0
    assert run_simulation(5)==0
    assert get_new_isbn(505)==get_new_isbn(505)
    assert get_new_year(505)==get_new_year(505)
    assert get_new_str(505)==get_new_str(505)
