"""Розважальний чат-бот"""


import random
import emoji
import pyjokes
from googletrans import Translator
from colorama import Fore, Style
from art import text2art

welcome = text2art("chat\n bot", "tarty1")
print(Fore.LIGHTCYAN_EX + welcome)
print(Style.RESET_ALL)


movies_by_genre = {
    "Бойовик": ["Термінатор 2: Судний день", "Месники: Війна нескінченності",
                "Міцний горішок", "Погані хлопці"],
    "Комедія": ["Завжди кажи ТАК", "Шрек", "Брюс Всемогутній", "Кролик Джоджо",
                "Похмілля у Вегасі"],
    "Драма": ["Зелена книга", "Той, що біжить по лезу", "Форест Гамп", "Хрещений батько",
              "Віднесені вітром"],
    "Жахи": ["Месія зла", "Дзвінок", "Екзорцист", "Сяйво", "Воно", "Сонцестояння"]
}


music_by_genre = {
    "Рок": ["Led Zeppelin", "Qween", "Pink Floyd", "AC/DC", "Eagles",
            "The Rolling Stones", "Pink Floyd"],
    "Поп": ["Michael Jackson", "Beyonce", "Robbie Williams",
            "Prince", "ABBA", "Madonna"],
    "Блюз": ["B.B.King", "Eric Clapton", "Ray Charles",
             "John Lee Hooker", "Nina Simone"],
    "Фанк": ["James Brown", "Jamiroquai", "Vulfpeck", "Rick James",
             "Cory Wong", "Bootsy Collins"],
    "Класика": ["Johann Sebastian Bach", "Ludwig van Beethoven",
                "Wolfgang Amadeus Mozart", "Antonio Vivaldi"]
}


games_by_genre = {
    "Стратегії": ["Company of Heroes", "Civilization 6", "Starcraft II — легенда десятиліть",
                  "Warcraft III", "Crusader Kings 3", "Total War: Warhammer 2 — глобальна битва",
                  "Age of Empires III"],
    "Симулятори": ["Farming Simulator 19", "Euro Truck Simulator 2",
                   "War Thunder", "Microsoft Flight Simulator",
                   "Squadron 42", "House Flipper", "THE SIMS 4"],
    "Екшн": ["Grand Theft Auto V", "Call of Duty: Modern Warfare / Warzone",
             "Fortnite", "Red Dead Redemption 2", "The Last of Us Part II"],
    "RPG": ["The Witcher 3: Wild Hunt", "Final Fantasy XV", "Dark Souls III",
            "Persona 5", "Divinity: Original Sin 2"],
    "Спортивні": ["UFC 5", "FC 24", "Forza Motorsport", "MLB: The Show 23"]
}


stories_list = [
    "Грецький атлет Протесілай 600 року до н. е метнув диск аж на 46 м.\
    Його рекорд протримався до 1928 року.",
    "Єдиною записаною промовою Ісаака Ньютона як члена парламенту було прохання відчинити вікно.",
    "Закони щодо чаклунства в Британії скасували 1951 року.",
    "Три найбагатші родини у світі мають більше активів, ніж 48 найбідніших країн",
    "Кубик Рубика – товар, який найбільше продається у світі. На другому місці – iPhone.",
    "Щоб передивитися всі відео на YouTube, знадобиться 1000 років.",
    "Якби до Coca-Cola не додавали барвник, вона була б зеленого кольору."
]


def recomendation(new_list, message1, message2):
    """Функція рекомендації що дістає із заданих значень рандомний варіант"""
    while True:
        for i, genre in enumerate(new_list.keys(), 1):
            print(f"{i}. {genre}")
        genre_choice = input("Ваш вибір: ")

        if genre_choice.isdigit() and 1 <= int(genre_choice) <= len(new_list):
            genre_index = int(genre_choice) - 1
            selected_genre = list(new_list.keys())[genre_index]
            print(Fore.LIGHTRED_EX + message1 + f"'{selected_genre}':")
            recommended = random.choice(new_list[selected_genre])
            print("-", recommended)
            print(Style.RESET_ALL)
            break
        print(Fore.RED + message2)
        print(Fore.RESET)


def recommend_movies():
    """Функція рекомендації фільмів за жанром"""
    message_recom = "Рекомендований фільм жанру "
    message_error = "Невірний вибір жанру."
    print("Оберіть жанр фільмів:")
    recomendation(movies_by_genre, message_recom, message_error)


def recommend_music():
    """Функція рекомендації музики за стилем"""
    message_recom = "Рекомендований виконавець стилю "
    message_error = "Невірний вибір стилю."
    print("Оберіть стиль музики:")
    recomendation(music_by_genre, message_recom, message_error)


def recommend_games():
    """Функція рекомендації ігор за жанром"""
    message_recom = "Рекомендована гра жанру "
    message_error = "Невірний вибір жанру."
    print("Оберіть жанр гри:")
    recomendation(games_by_genre, message_recom, message_error)


def tell_joke():
    """Функція анекдотів з залученням модуля pyjokes
    та перекладу за рахунок модуля googletrans"""
    translator = Translator()
    joke = pyjokes.get_joke()
    print(Fore.LIGHTGREEN_EX + joke)
    print(Style.RESET_ALL + "Переклад:")
    print(Fore.LIGHTGREEN_EX + translator.translate(joke, dest='uk').text)
    print(Style.RESET_ALL)
    print()


def tell_interesting_story():
    """Функція розповіді історій"""
    story = random.choice(stories_list)
    print(Fore.LIGHTGREEN_EX + story)
    print(Style.RESET_ALL)
    print()


def play_game():
    """Гра 'Камінь, ножиці, парір'"""
    print(Fore.LIGHTGREEN_EX + "\t\t ГРА\n'КАМІНЬ, НОЖИЦІ, ПАПІР'!")
    print(Style.RESET_ALL)
    choices = ["камінь", "ножиці", "папір"]

    while True:
        # Вибір комп'ютера
        computer_choice = random.choice(choices)

        # Вибір користувача
        user_choice = input("Введіть 'камінь', 'ножиці' або 'папір'\n" +
                            "для повернення в меню введіть 'меню': ").lower()
        print()

        # Перевірка правильності введення користувачем
        if user_choice == "меню":
            print("Вихід до головного меню...")
            break
        if user_choice not in choices:
            print(Fore.RED + "Некоректний вибір. Спробуйте ще раз.")
            print(Fore.RESET)
            continue

        print("Ваш вибір: ", user_choice)
        print("Вибір комп'ютера: ", computer_choice)
        print()

        # Визначення переможця
        if user_choice == computer_choice:
            print(emoji.emojize(Fore.LIGHTBLUE_EX + 'Нічия! :handshake:'))
            print(Style.RESET_ALL)
        elif not (not (user_choice == "камінь" and computer_choice == "ножиці") and not (
                user_choice == "ножиці" and computer_choice == "папір")) or \
                (user_choice == "папір" and computer_choice == "камінь"):
            print(emoji.emojize(Fore.GREEN + "Ви перемогли! :party_popper:"))
            print(Style.RESET_ALL)
        else:
            print(emoji.emojize(Fore.RED + "Комп'ютер переміг! :robot:"))
            print(Style.RESET_ALL)


def display_menu():
    """Виведення пунктів основного меню"""
    print(Fore.LIGHTCYAN_EX + "Меню:")
    print("1. Рекомендації фільмів")
    print("2. Музичні рекомендації")
    print("3. Рекомендації ігор")
    print("4. Розповісти анекдот")
    print("5. Цікаві історії")
    print("6. Пограти в гру")
    print("7. Вийти")
    print(Style.RESET_ALL)


def main():
    """Основна функція"""
    while True:
        display_menu()
        choice = input("Оберіть пункт меню: ")
        print()

        if choice == "1":
            recommend_movies()
        elif choice == "2":
            recommend_music()
        elif choice == "3":
            recommend_games()
        elif choice == "4":
            tell_joke()
        elif choice == "5":
            tell_interesting_story()
        elif choice == "6":
            play_game()
        elif choice == "7":
            good_luck = text2art("good\nluck", "tarty1")
            print(Fore.LIGHTCYAN_EX + good_luck)
            break
        else:
            print(Fore.RED + "Невірний вибір. Будь ласка, виберіть знову.")
            print(Fore.RESET)


if __name__ == "__main__":
    main()
