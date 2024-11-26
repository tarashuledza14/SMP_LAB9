import os
from Source.ABC123asterism import draw_char_asterism
from Source.ABC123dog import draw_char_dog
from Source.ABC123hash import draw_char_hash
from configs import ansi_colors


class MyAsciiArtGenerator:

    def __init__(self):

        self.art_text = ""
        self.color = "white"
        self.width_factor = 1
        self.height_factor = 1
        self.art_symbol = ""
        self.ascii_text = ""
        self.max_width = 140
        self.max_height = 28
        self.alignment = "center"

    def get_input(self):
        """Prompt the user for the text to convert to ASCII art."""
        while True:
            text = input("Enter the text you want to convert to ASCII art: ").strip()
            if text:
                self.art_text = text.upper()
                break
            else:
                print("Input cannot be empty. Please try again.")

    def get_color(self):
        """Prompt the user to select a color."""
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
        """Prompt the user to enter the scaling factors for width and height."""
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
        """Prompt the user to enter the symbol for the ASCII art."""
        while True:
            symbol = input("Enter the symbol you want to use in the ASCII art ('@', '#', '*'): ").strip()
            if symbol:
                self.art_symbol = symbol
                break
            else:
                print("Using default symbol '#' for the ASCII art.")
                self.art_symbol = "#"

    def get_alignment(self):
        """Prompt the user to select the alignment for the text."""
        while True:
            alignment = input("Choose text alignment (left, center, right): ").strip().lower()
            if alignment in ['left', 'center', 'right']:
                self.alignment = alignment
                break
            else:
                print("Invalid input. Please choose 'left', 'center', or 'right'.")

    def scale_ascii_art(self, ascii_art):
        """Scale the ASCII art based on width and height factors."""
        scaled_lines = []
        for line in ascii_art.splitlines():
            scaled_line = "".join(char * self.width_factor for char in line)
            for _ in range(self.height_factor):
                scaled_lines.append(scaled_line)
        return "\n".join(scaled_lines)

    def figlet_format(self, art_text, font):
        """Format the input text into ASCII art using the selected font symbol."""
        result = [""] * 7

        for letter in art_text:
            if font == "#":
                letter_art = draw_char_hash(letter)
            elif font == "@":
                letter_art = draw_char_dog(letter)
            elif font == "*":
                letter_art = draw_char_asterism(letter)
            else:
                raise ValueError("Invalid font symbol. Choose '#', '@', or '*'.")

            for i in range(7):
                result[i] += letter_art[i]

        return "\n".join(result)

    def generate_art_symbol(self):
        """Generate the ASCII art based on the user input and apply color and scaling."""
        try:
            ascii_art = self.figlet_format(self.art_text, self.art_symbol)
            scaled_art = self.scale_ascii_art(ascii_art)

            art_lines = scaled_art.splitlines()
            aligned_art_lines = []
            for line in art_lines:
                if self.alignment == 'center':
                    aligned_line = line.center(self.max_width)
                elif self.alignment == 'right':
                    aligned_line = line.rjust(self.max_width)
                else:  # self.alignment == 'left'
                    aligned_line = line.ljust(self.max_width)
                aligned_art_lines.append(aligned_line)

            aligned_art = "\n".join(aligned_art_lines)
            color_code = ansi_colors.ANSI_COLORS.get(self.color, '\033[37m')
            colored_art = f"{color_code}{aligned_art}\033[0m"
            ascii_art = colored_art.replace("#", self.art_symbol)
            self.ascii_text = ascii_art

            canvas_width, canvas_height = self.get_canvas_size()
            canvas = self.create_canvas(canvas_width, canvas_height)

            art_lines = ascii_art.splitlines()
            for i in range(min(canvas_height, len(art_lines))):
                for j in range(min(canvas_width, len(art_lines[i]))):
                    canvas[i][j] = art_lines[i][j]

            # Display the result
            for line in canvas:
                print(''.join(line))

            return canvas

        except Exception as e:
            print(f"Error generating ASCII art: {e}")
            return None

    def save_to_file(self):
        """Save the generated ASCII art to a file."""
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

    def get_canvas_size(self):
        """Prompt the user to input the canvas size."""
        while True:
            try:
                width = int(input("Enter the width of the canvas (max 140): ").strip())
                height = int(input("Enter the height of the canvas (max 28): ").strip())

                if 1 <= width <= 140 and 1 <= height <= 28:
                    return width, height
                else:
                    print("Width must be between 1 and 140, height must be between 1 and 28. Please try again.")
            except ValueError:
                print("Invalid input. Please enter valid integers for width and height.")

    def create_canvas(self, width, height):
        """Create a canvas for the ASCII art."""
        return [[' ' for _ in range(width)] for _ in range(height)]

    def run(self):
        """Run the ASCII art generator."""
        while True:
            self.get_input()
            self.get_symbol()
            self.get_color()
            self.get_scaling_factors()
            self.get_alignment()
            self.generate_art_symbol()

            save_choice = input("Do you want to save the ASCII art to a file? (yes/no): ").strip().lower()
            if save_choice == 'yes':
                self.save_to_file()

            if input('Do you want to create another ASCII art? (yes/no): ').lower() != 'yes':
                print("Thank you for using the ASCII Art Generator!")
                break