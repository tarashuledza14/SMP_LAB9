import os
import pyfiglet
from configs import ansi_colors


class AsciiArtGenerator:
    def __init__(self):
        self.art_text = ""
        self.font = "standard"
        self.color = "white"
        self.width_factor = 1
        self.height_factor = 1
        self.art_symbol = "#"
        self.ascii_text = ""

    def get_input(self):
        while True:
            text = input("Enter the text you want to convert to ASCII art: ").strip()
            if text:
                self.art_text = text
                break
            else:
                print("Input cannot be empty. Please try again.")

    def get_font(self):
        example_fonts = ['standard', 'slant', 'block', 'bubble', 'digital']
        print("Available fonts: ", ', '.join(example_fonts))
        while True:
            font = input("Select a font (or press Enter for 'standard'): ").strip()
            if not font:
                self.font = "standard"
                break
            elif font in example_fonts:
                self.font = font
                break
            else:
                print("Invalid font. Try again.")

    def get_color(self):
        example_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        print("Available colors: ", ', '.join(example_colors))
        while True:
            color = input("Select a color (or press Enter for 'white'): ").strip()
            if not color:
                self.color = "white"
                break
            elif color in example_colors:
                self.color = color
                break
            else:
                print("Invalid color. Try again.")

    def get_scaling_factors(self):
        while True:
            try:
                width_factor = input("Enter the width scaling factor (default is 1): ").strip()
                height_factor = input("Enter the height scaling factor (default is 1): ").strip()
                self.width_factor = int(width_factor) if width_factor else 1
                self.height_factor = int(height_factor) if height_factor else 1

                if self.width_factor > 0 and self.height_factor > 0:
                    break
                else:
                    print("Scaling factors must be positive integers. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid integers for scaling factors.")

    def get_symbol(self):
        while True:
            symbol = input("Enter the symbol you want to use in the ASCII art ('@', '#', '*',...): ").strip()
            if symbol:
                self.art_symbol = symbol
                break
            else:
                print("Using default symbol '#' for the ASCII art.")
                self.art_symbol = "#"

    def scale_ascii_art(self, ascii_art):
        scaled_lines = []
        for line in ascii_art.splitlines():
            scaled_line = "".join(char * self.width_factor for char in line)
            for _ in range(self.height_factor):
                scaled_lines.append(scaled_line)
        return "\n".join(scaled_lines)

    def generate_art(self):
        try:
            ascii_art = pyfiglet.figlet_format(self.art_text, font=self.font)
            scaled_art = self.scale_ascii_art(ascii_art)
            color_code = ansi_colors.ANSI_COLORS.get(self.color, '\033[37m')
            colored_art = f"{color_code}{scaled_art}\033[0m"
            self.ascii_text = colored_art
            return colored_art
        except Exception as e:
            print(f"Error generating ASCII art: {e}")
            return None

    def generate_art_symbol(self):
        try:
            ascii_art = pyfiglet.figlet_format(self.art_text, "banner3")
            scaled_art = self.scale_ascii_art(ascii_art)
            color_code = ansi_colors.ANSI_COLORS.get(self.color, '\033[37m')
            colored_art = f"{color_code}{scaled_art}\033[0m"
            ascii_art = colored_art.replace("#", self.art_symbol)
            self.ascii_text = ascii_art
            print(ascii_art)
            return ascii_art
        except Exception as e:
            print(f"Error generating ASCII art: {e}")
            return None

    def preview_art(self):
        art_preview = self.generate_art()
        if art_preview:
            print("Preview of your ASCII art:")
            print(art_preview)

    def save_to_file(self):
        try:
            folder_to_save = os.path.abspath(os.path.join(os.getcwd(), os.pardir, "calculator", "Sources"))
            os.makedirs(folder_to_save, exist_ok=True)
            file_name = input("Enter the file name to save the ASCII art (e.g., art): ").strip()
            formatted_file_name = os.path.join(folder_to_save, f"{file_name}.txt")
            ascii_art = self.ascii_text

            with open(formatted_file_name, 'w') as file:
                file.write(ascii_art.replace('\033[0m', ''))

            print(f"ASCII art saved to {formatted_file_name}.")
        except Exception as e:
            print(f"Error saving ASCII art to file: {e}")

    def run(self):
        while True:
            self.get_input()
            self.get_font()
            self.get_color()
            self.get_scaling_factors()
            self.preview_art()

            save_choice = input("Do you want to save the ASCII art to a file? (yes/no): ").strip().lower()
            if save_choice == 'yes':
                self.save_to_file()

            self.get_symbol()
            self.generate_art_symbol()

            save_choice = input("Do you want to save the ASCII art to a file? (yes/no): ").strip().lower()
            if save_choice == 'yes':
                self.save_to_file()

            if input('Do you want to create another ASCII art? (yes/no): ').lower() != 'yes':
                print("Thank you for using the ASCII Art Generator!")
                break
