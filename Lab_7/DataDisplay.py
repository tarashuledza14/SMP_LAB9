from typing import List, Dict
from tabulate import tabulate
from colorama import Fore, Style


class DataDisplay:
    """Class for displaying different types of data in tabular format."""

    @staticmethod
    def show_table(data: List[Dict]) -> None:
        """Displays a table of posts."""
        table = [[item.get('id', 'N/A'), item.get('title', 'N/A')] for item in data]
        print(Fore.GREEN + Style.BRIGHT + "Posts" + Style.RESET_ALL)
        print(tabulate(table, headers=["ID", "Title"], tablefmt="grid"))

    @staticmethod
    def show_users(users: List[Dict]) -> None:
        """Displays a table of users."""
        table = []
        for user in users:
            table.append([
                user.get("id", 'N/A'),
                user.get("name", 'N/A'),
                user.get("username", 'N/A'),
                user.get("email", 'N/A'),
                f"{user.get('address', {}).get('street', 'N/A')}, {user.get('address', {}).get('suite', 'N/A')}, "
                f"{user.get('address', {}).get('city', 'N/A')}, {user.get('address', {}).get('zipcode', 'N/A')}",
                user.get("phone", 'N/A'),
                user.get("website", 'N/A'),
                user.get("company", {}).get("name", 'N/A')
            ])
        print(Fore.CYAN + Style.BRIGHT + "Users" + Style.RESET_ALL)
        print(tabulate(table, headers=["ID", "Name", "Username", "Email", "Address", "Phone", "Website", "Company"], tablefmt="grid"))

    @staticmethod
    def show_comments(comments: List[Dict]) -> None:
        """Displays a table of comments."""
        table = []
        for comment in comments:
            # Fallback to 'body' if 'comment' key does not exist
            comment_text = comment.get('comment') or comment.get('body', 'N/A')
            table.append([
                comment.get('id', 'N/A'),
                comment.get('postId', 'N/A'),
                comment.get('userId', 'N/A'),
                comment_text
            ])
        print(Fore.YELLOW + Style.BRIGHT + "Comments" + Style.RESET_ALL)
        print(tabulate(table, headers=["ID", "Post ID", "User ID", "Comment"], tablefmt="grid"))
