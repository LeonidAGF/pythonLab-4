from src.simulation import run_simulation


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    steps: int = int(input("ведите количество шагов в симуляции"))
    seed: int = int(input("ведите seed для симуляции"))
    run_simulation(steps, seed)


if __name__ == "__main__":
    main()
