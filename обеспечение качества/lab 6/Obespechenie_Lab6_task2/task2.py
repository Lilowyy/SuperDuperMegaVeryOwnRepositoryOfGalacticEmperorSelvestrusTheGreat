def check_password(entered_password, correct_password):
    return entered_password == correct_password

def main():
    correct_password = "1111"
    max_attempts = 3
    attempts = 0

    print("ВВЕДИТЕ ПАРОЛЬ ДЛЯ ВХОДА В ПРОГРАММУ")

    while attempts < max_attempts:
        entered_password = input("Пароль: ")

        if check_password(entered_password, correct_password):
            print("ДОБРО ПОЖАЛОВАТЬ")
            return

        else:
            print("ПАРОЛЬ НЕВЕРНЫЙ, ПОПРОБУЙТЕ ЕЩЁ РАЗ!")
            attempts += 1
    print("Превышено допустимое число попыток ввода пароля. Доступ заблокирован.")
main()