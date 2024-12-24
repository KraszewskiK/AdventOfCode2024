def solve_part1(input_data: str) -> int:
    codes = [line for line in input_data.splitlines() if line]
    result = 0
    robots = [Robot("numeric"),
              Robot("directional"),
              Robot("directional")]

    for code in codes:
        numeric_part = int(code.replace("A", ""))
        for robot in robots:
            code = "".join(robot.press_button(button) for button in code)
        sequence_length = len(code)
        result += numeric_part * sequence_length

    return result


def solve_part2(input_data: str) -> int:
    codes = [line for line in input_data.splitlines() if line]
    result = 0
    robots = [Robot("numeric")] + [Robot("directional") for _ in range(25)]
    sequence_length_memory = dict()

    for code in codes:
        numeric_part = int(code.replace("A", ""))
        sequence_length = 0
        commands = [code] + ([''] * (len(robots)))
        sequence_shelf = [None] * (len(robots) + 1)

        while any(commands):
            if commands[-1] != "":
                sequence_length += len(commands[-1])
                commands[-1] = ""

            for i in range(-2, -len(commands) - 1, -1):
                if commands[i] != "" and commands[i + 1] == "":  # command 'i' needs to be executed
                    new_command = robots[i + 1].press_button(commands[i][0])
                    commands[i] = commands[i][1:]
                    if (i + 1, new_command) in sequence_length_memory:
                        sequence_length += sequence_length_memory[(i + 1, new_command)]
                    else:
                        if sequence_shelf[i + 1] is None:
                            sequence_shelf[i + 1] = new_command, sequence_length
                        commands[i + 1] = new_command
                    break
                elif commands[i] == "" and sequence_shelf[
                    i] is not None:  # command 'i' was executed, so we count how many steps it took
                    command, old_length = sequence_shelf[i]
                    sequence_length_memory[(i, command)] = sequence_length - old_length
                    sequence_shelf[i] = None

        result += numeric_part * sequence_length

    return result


class Robot:
    keypad_numeric = ["789",
                      "456",
                      "123",
                      "#0A"]
    keypad_directional = ["#^A",
                          "<v>"]
    directions_memory = dict()

    def __init__(self, keypad: str, initial_position: str = "A") -> None:
        if keypad == "numeric":
            self.keypad = self.keypad_numeric
        elif keypad == "directional":
            self.keypad = self.keypad_directional
        else:
            raise ValueError(f"Invalid keypad: {keypad}")
        self.keypad_type = keypad
        self.position = self.get_position_in_keypad(initial_position)

    @staticmethod
    def translate_direction(direction: str) -> tuple[int, int]:
        if direction == "A":
            return 0, 0
        elif direction == "^":
            return -1, 0
        elif direction == "v":
            return 1, 0
        elif direction == "<":
            return 0, -1
        elif direction == ">":
            return 0, 1
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def get_position_in_keypad(self, button: str) -> tuple[int, int]:
        for i, line in enumerate(self.keypad):
            if button in line:
                return i, line.index(button)

    def move(self, direction: str) -> None:
        x, y = self.translate_direction(direction)
        new_x = self.position[0] + x
        new_y = self.position[1] + y

        if 0 <= new_x < len(self.keypad) and 0 <= new_y < len(self.keypad[new_x]) and self.keypad[new_x][new_y] != "#":
            self.position = new_x, new_y
        else:
            raise ValueError(f"Invalid move: {direction}, {self.position}")

    def get_directions_to_move(self, to: str) -> str:
        x, y = self.position
        to_x, to_y = self.get_position_in_keypad(to)
        if (x, y, to_x, to_y) in self.directions_memory:
            return self.directions_memory[(x, y, to_x, to_y)]
        move_sequence = ""

        if y < to_y:
            move_sequence += ">" * (to_y - y)
        if to_x < x:
            if self.keypad_type != "directional" or y != 0:
                move_sequence = "^" * (x - to_x) + move_sequence
            else:
                move_sequence += "^" * (x - to_x)
        elif x < to_x:
            if self.keypad_type != "numeric" or y != 0:
                move_sequence = "v" * (to_x - x) + move_sequence
            else:
                move_sequence += "v" * (to_x - x)
        if y > to_y:
            if (x != (0 if self.keypad_type == "directional" else len(self.keypad) - 1)) or to_y != 0:
                move_sequence = "<" * (y - to_y) + move_sequence
            else:
                move_sequence += "<" * (y - to_y)
        self.directions_memory[(x, y, to_x, to_y)] = move_sequence
        return move_sequence

    def press_button(self, button: str) -> str:
        move_sequence = self.get_directions_to_move(button)
        for direction in move_sequence:
            self.move(direction)
        return move_sequence + "A"

    def press_button_faster(self, button: str) -> str:
        move_sequence = self.get_directions_to_move(button)
        self.position = self.get_position_in_keypad(button)
        return move_sequence + "A"
