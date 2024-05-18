from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        difference = current_date - input_date
        return difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

print(get_days_from_today("2023-10-09"))
print(get_days_from_today("2025-10-09"))
print(get_days_from_today("wqeqwer"))

