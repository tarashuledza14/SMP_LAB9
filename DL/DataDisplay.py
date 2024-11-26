from tabulate import tabulate
from colorama import Fore, Style
from Lib.Log import logger


class DataDisplay:
    @staticmethod
    def show_table(data):
        logger.info("Викликається функція show_table з %d записами", len(data))
        try:
            table = [[item['id'], item['title']] for item in data]
            print(Fore.GREEN + Style.BRIGHT + "Posts" + Style.RESET_ALL)
            print(tabulate(table, headers=["ID", "Title"], tablefmt="grid"))
            logger.info("Таблиця 'Posts' успішно відображена")
        except Exception as e:
            logger.error("Помилка у show_table: %s", e)

    @staticmethod
    def show_users(users):
        logger.info("Викликається функція show_users з %d записами", len(users))
        try:
            table = []
            for user in users:
                table.append([
                    user["id"],
                    user["name"],
                    user["username"],
                    user["email"],
                    f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}",
                    user["phone"],
                    user["website"],
                    user["company"]["name"]
                ])
            print(Fore.CYAN + Style.BRIGHT + "Users" + Style.RESET_ALL)
            print(tabulate(table, headers=["ID", "Name", "Username", "Email", "Address", "Phone", "Website", "Company"], tablefmt="grid"))
            logger.info("Таблиця 'Users' успішно відображена")
        except Exception as e:
            logger.error("Помилка у show_users: %s", e)

    @staticmethod
    def show_comments(comments):
        logger.info("Викликається функція show_comments з %d записами", len(comments))
        try:
            table = []
            for comment in comments:
                # Перевірка наявності очікуваних ключів і визначення альтернативного ключа "body"
                comment_text = comment.get('comment') or comment.get('body')
                table.append([
                    comment.get('id', 'N/A'),
                    comment.get('postId', 'N/A'),
                    comment.get('userId', 'N/A'),
                    comment_text
                ])
            print(Fore.YELLOW + Style.BRIGHT + "Comments" + Style.RESET_ALL)
            print(tabulate(table, headers=["ID", "Post ID", "User ID", "Comment"], tablefmt="grid"))
            logger.info("Таблиця 'Comments' успішно відображена")
        except Exception as e:
            logger.error("Помилка у show_comments: %s", e)
