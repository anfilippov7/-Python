from application.salary import calculate_salary
from application.db.people import get_employees
from pygismeteo import Gismeteo


def temperature_air(town):
    try:
        gismeteo = Gismeteo()
        search_results = gismeteo.search.by_query(town)
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
        print(f'Температура в городе {town} составляет {current.temperature.air.c} градусов цельсия')
    except:
        print('Вы ввели некорректные данные!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_employees()
    calculate_salary()
    temperature_air(town=input("Введите название города в котором вы хотите узнать температуру воздуха: "))


