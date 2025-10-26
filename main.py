#from experta import *
from rules import AdditiveExpert
from facts import Additive, Warning


def get_user_input():
    raw_input = input("Введите пищевые добавки через запятую (например: E102, E250, E951): ")
    return [code.strip().upper() for code in raw_input.split(',') if code.strip()]


def main():
    additives = get_user_input()

    additive_engine = AdditiveExpert()
    additive_engine.reset()

    for additive_code in additives:
        additive_engine.declare(Additive(code=additive_code))

    additive_engine.run()

    print("\nПредупреждения:")
    for additive_fact in additive_engine.facts.values():
        if isinstance(additive_fact, Warning):
            print("-", additive_fact['message'])


if __name__ == "__main__":
    main()
