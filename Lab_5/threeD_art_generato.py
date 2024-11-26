from Lib import FileService
from Lab_5.figures.Cube import Cube


class ThreeDArtService:
    """Service for generating and manipulating 3D art."""

    def __init__(self, height: int, color: int, direction: bool):
        """Initialize the 3D art service with a Cube and other parameters."""
        self.art = Cube(height)
        self.color = color
        self.direction = direction

    def change_size(self):
        """Change the size of the cube (side_a)."""
        try:
            size = int(input("Enter new size (no less than 3): "))
            if size >= 3:
                self.art.side_a = size
            else:
                print("Size must be at least 3. Try again.")
                self.change_size()
        except ValueError:
            print("Invalid input. Please enter a valid integer for size.")
            self.change_size()

    def change_color(self, color: int):
        """Change the color of the art."""
        self.color = color

    def change_direction(self):
        """Toggle the direction of the art."""
        self.direction = not self.direction
        print("Direction was successfully changed")

    def get_art(self) -> str:
        """Get the 3D art, either in original or inverted direction."""
        color_text = '\033[%dm%s\033[0m'
        if self.direction:
            art = self.art.get_three_d_art()
        else:
            art = self.art.get_three_d_inverted_art()

        return color_text % (self.color, art)

    def get_2d_art(self) -> str:
        """Get the 2D art."""
        color_text = '\033[%dm%s\033[0m'
        art = self.art.get_two_d_art()
        return color_text % (self.color, art)

    def print_art(self):
        """Print the 3D art."""
        print(self.get_art())

    def print_2d_art(self):
        """Print the 2D art."""
        print(self.get_2d_art())

    def save_art_into_file(self, file_name: str):
        """Save the generated art into a file."""
        try:
            FileService.write_into_file(file_name, self.get_art())
        except FileExistsError:
            print(f"File {file_name} already exists. Please choose a different name.")
            raise FileExistsError

    @staticmethod
    def get_art_archive(file_name: str):
        """Retrieve and print art from a file archive."""
        try:
            print(FileService.read_from_file(file_name))
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            raise FileNotFoundError
