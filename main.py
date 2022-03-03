from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from datetime import date as dt

if __name__ == '__main__':
    cs()
    ge()
    print(f'''Here is the current date:
Day - {dt.today().strftime("%d")}
Month - {dt.today().strftime("%B")}
Year - {dt.today().strftime("%Y")}''')
