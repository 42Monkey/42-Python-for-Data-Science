from typing import Any

def all_thing_is_obj(object: Any) -> int:
	check = type(object)

	match object:
		case list():
			print(f'List: {check}')
		case tuple():
			print(f'Tuple: {check}')
		case set():
			print(f'Set: {check}')
		case dict():
			print(f'Dict: {check}')
		case str():
			print(f'{object} is in the kitchen: {check}')
		case _:
			print("Type not found")
	return 42



