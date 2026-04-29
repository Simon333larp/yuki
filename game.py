import random


def guess_the_number():
    print("🎯 Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if guess < secret_number:
                print("📈 Больше! Загаданное число больше.")
            elif guess > secret_number:
                print("📉 Меньше! Загаданное число меньше.")
            else:
                print(
                    f"🎉 Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!"
                )
                break

        except ValueError:
            print("⚠️ Пожалуйста, введите целое число.")


if __name__ == "__main__":
    guess_the_number()
