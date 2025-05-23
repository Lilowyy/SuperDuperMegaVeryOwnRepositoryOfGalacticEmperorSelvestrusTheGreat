class Weight:
    def __init__(self, kg):
        self.kg = kg

    def get_centners(self):
        centners = int(self.kg // 100)
        return centners

if __name__ == "__main__":
    while True:
        user_input = input("Введите вес в килограммах или 'q' для выхода: ")
        if user_input.lower() == 'q':
            print("Выход")
            break

        kg = float(user_input)
        weight = Weight(kg)
        centners = weight.get_centners()
        print(f"Количество полных центнеров: {centners}")