import sys
from nok_game import play_nok_game
from geometric_progression import play_progression_game


def run_game(game_name):
    games = {
        "nok": play_nok_game,
        "progression": play_progression_game
    }
    game = games.get(game_name)
    if game:
        game()
    else:
        print("Ошибка: неизвестная игра. Используйте 'nok' или 'progression'.")


def show_menu():
    print("Выберите игру:")
    print("1 - Игра 'НОК' (наименьшее общее кратное)")
    print("2 - Игра 'Геометрическая прогрессия'")
    print("0 - Выйти")
    return input("Введите номер игры: ")


def main():
    if len(sys.argv) > 1:
        run_game(sys.argv[1].lower())
        return

    while True:
        choice = show_menu()
        game_choices = {"1": "nok", "2": "progression"}
        if choice in game_choices:
            run_game(game_choices[choice])
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
