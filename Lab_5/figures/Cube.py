from Lab_5.figures.FigureBase import FigureBase

class Cube(FigureBase):
    def __init__(self, side_a: int):
        super().__init__(side_a)

    def get_two_d_art(self) -> str:
        result = ""
        for side_a_pixel in range(self.side_a):
            result += "# "
            for side_b_pixel in range(self.side_a - 2):
                if side_a_pixel % self.side_a == 0 or side_a_pixel + 1 == self.side_a:
                    result += "# "
                else:
                    result += "  "
            result += "#\n"

        return result

    def get_three_d_art(self) -> str:
        result = ""

        art_size = int(self.side_a + self.side_a / 2)
        side_side_size = int(self.side_a / 1.5)

        space_counter = 0
        for x in range(art_size):
            if x == 0:
                result += "# "
            elif x < side_side_size:
                result += "# " + space_counter * "  " + "# "
                space_counter += 1
            elif side_side_size <= x <= art_size - side_side_size:
                result += "# " + (side_side_size - 2) * "  " + "# "
                space_counter = 1
            elif x < art_size - 1:
                result += space_counter * "  " + "# " + (art_size - x - 2) * "  " + "# "
                space_counter += 1
            else:
                result += space_counter * "  " + "# "

            for y in range(self.side_a - 2):
                if x == 0 or x == side_side_size - 1 or x == art_size - 1:
                    result += "# "
                else:
                    result += "  "

            result += "#\n"

        return result

    def get_three_d_inverted_art(self) -> str:
        result = ""

        art_size = int(self.side_a + self.side_a / 2)
        side_side_size = int(self.side_a / 1.5)

        space_counter = 0
        for x in range(art_size):
            if x < side_side_size:
                result += (side_side_size - x - 1) * "  " + "# "
            else:
                result += "# "

            for y in range(self.side_a - 2):
                if x == 0 or x == side_side_size - 1 or x == art_size - 1:
                    result += "# "
                else:
                    result += "  "

            result += "# "

            if 0 < x < self.side_a:
                result += space_counter * "  " + "#"
                if space_counter < side_side_size - 2:
                    space_counter += 1
            elif self.side_a <= x < art_size - 1:
                space_counter -= 1
                result += space_counter * "  " + "#"

            result += "\n"

        return result