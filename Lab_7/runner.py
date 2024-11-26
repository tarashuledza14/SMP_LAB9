from DAL.DataSaver import DataSaver
from Lab_7.APIClient import APIClient
from Lab_7.DataDisplay import DataDisplay
from Lab_7.ErrorHandler import ErrorHandler
from Lab_7.HistoryLogger import HistoryLogger
from UI.MenuItem import MenuItem
from UI.MenuBuilder import MenuBuilder


def show_all_posts(client, display, logger):
    """Fetch and display all posts."""
    try:
        posts = client.get_data("posts")
        display.show_table(posts)
        logger.log("показати всі пости", posts)
    except Exception as error:
        ErrorHandler.handle_error(error)


def save_data(client, saver):
    """Save data to a specified file format."""
    format_choice = input("Введіть формат збереження (json/csv/txt): ").strip().lower()
    filename = input("Введіть ім'я файлу: ").strip()
    if format_choice in ['json', 'csv', 'txt']:
        try:
            saver_method = {
                'json': saver.save_as_json,
                'csv': saver.save_as_csv,
                'txt': saver.save_as_txt
            }[format_choice]
            posts = client.get_data("posts")  # Fetch posts before saving
            saver_method(posts, filename)
            print(f"Дані збережено у {filename}.{format_choice}")
        except Exception as error:
            ErrorHandler.handle_error(error)
    else:
        print("Невідомий формат.")


def show_all_users(client, display, logger):
    """Fetch and display all users."""
    try:
        users = client.get_all_users()
        display.show_users(users)
        logger.log("показати всіх користувачів", users)
    except Exception as error:
        ErrorHandler.handle_error(error)


def show_history(logger):
    """Show the history of logs."""
    logger.show_history()


def exit_program(is_running):
    """Exit the program."""
    print("Вихід...")
    is_running[0] = False


def run():
    """Main function to run the program."""
    client = APIClient()
    display = DataDisplay()
    saver = DataSaver()
    logger = HistoryLogger()

    is_running = [True]

    menu_items = [
        MenuItem("1", "Показати всі пости", lambda: show_all_posts(client, display, logger)),
        MenuItem("3", "Зберегти дані", lambda: save_data(client, saver)),
        MenuItem("4", "Показати всіх користувачів", lambda: show_all_users(client, display, logger)),
        MenuItem("5", "Показати історію", lambda: show_history(logger)),
        MenuItem("0", "Вийти",  lambda:exit_program(is_running)),
    ]

    menu = MenuBuilder(menu_items)
    while is_running[0]:
        menu.initialize()
