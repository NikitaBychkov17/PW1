import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def print_current_date():
    current_date = datetime.datetime.now()
    print(f"Текущая дата: {current_date.strftime('%Y-%m-%d')}")
    
if __name__ == "__main__":
    print("Запуск программы 'Бухгалтерия'")
    
    # Вывод текущей даты
    print_current_date()
    
    # Вызов функции расчета зарплаты
    calculate_salary()
    
    # Вызов функции получения сотрудников
    get_employees()