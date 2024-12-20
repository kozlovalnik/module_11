from pprint import pprint


class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            pass

    def __is_valid_vin(self, vin_number: int) -> bool:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер', vin_number)
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера', vin_number)
        return True

    def __is_valid_numbers(self, numbers: str) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров', numbers, {0: 1})
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера', numbers, {0: 1})
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.vin = args[1]


class IncorrectCarNumbers(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0]
        self.num = args[1]
        self.kw = kwargs


def introspection_info(obj: object)-> list:
    result = []
    result.append(type(obj))
    result.append(obj.__module__)
    for dir_item in dir(obj):
        result.append(dir_item)
    return result

pprint(introspection_info(Car))
pprint(introspection_info(IncorrectVinNumber))

