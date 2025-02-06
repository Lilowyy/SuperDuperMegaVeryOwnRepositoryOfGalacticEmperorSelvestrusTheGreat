class Time:
    def __init__(self, days):
        self.days = days

    def get_weeks(self):
        weeks = int(self.days // 7)
        return weeks

if __name__ == "__main__":
    while True:
        user_input = input("Введите количество прошедших дней или 'q' для выхода: ")
        if user_input.lower() == 'q':
            print("Выход")
            break

        days = float(user_input)
        days = Time(days)
        weeks = days.get_weeks()
        print(f"Количество полных недель: {weeks}")