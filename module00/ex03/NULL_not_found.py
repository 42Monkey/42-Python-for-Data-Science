from typing import Any


def NULL_not_found(object: Any) -> int:
    check = type(object)

    match object:
        case None:
            print(f'Nothing: {object} {check}')
            return 0
        case str() if not object:
            print(f'Empty: {check}')
            return 0
        case False:
            print(f'Fake: {object} {check}')
            return 0
        case int():
            print(f'Zero: {object} {check}')
            return 0
        case float():
            print(f'Cheese: {object} {check}')
            return 0
        case _:
            print("Type not Found")
            return 1

    return 42
