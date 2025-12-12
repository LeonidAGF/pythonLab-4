from src.simulation import run_simulation, get_new_isbn, get_new_year, get_new_str


def test_simulation():
    """
        Тесты для simulation
    """
    assert run_simulation(0)==0
    assert run_simulation(5)==0
    assert (get_new_isbn()>(10000000000-1))==1
    assert (get_new_year()>1999)==1
    assert (len(get_new_str())<26)==1
