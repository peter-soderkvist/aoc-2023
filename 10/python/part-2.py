import re


class Node:
    def __init__(self, x: int, y: int, direction: str, pipe: str):
        self.x = x
        self.y = y
        self.direction = direction
        self.pipe = pipe

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.direction}, {self.pipe}"

class Grid:
    def __init__(self, board: list[str]) -> None:
        self.board = board
        self.starting_point = self.starting_point()
        
    def __str__(self) -> str:
        return "Starting point: " + str(self.starting_point) + '\n\n' + '\n'.join(self.board)
    
    def starting_point(self) -> (int, int):
        for y, row in enumerate(self.board):
            for x, char in enumerate(row):
                if char == 'S':
                    return (x, y)


class Player:
    def __init__(self, x: int, y: int, pipe: str, direction: str):
        self.x = x
        self.y = y
        self.pipe = pipe
        self.direction = direction
        self.nodes = []

    def __str__(self) -> str:
        return f"Player: {self.x=}, {self.y=} - {self.pipe=}, {self.direction=}"
    
    def move(self, y: int, x: int):
        self.x += x
        self.y += y


pipes = {
    '|': {'north': (-1, 0), 'south': (1, 0), 'next': {'north': 'north', 'south': 'south'}},
    '-': {'east': (0, 1), 'west': (0, -1), 'next': {'east': 'east', 'west': 'west'}},
    'L': {'north': (-1, 0), 'east': (0, 1),
        'next': {
            'north': 'east',
            'west': 'north',
            'east': 'north',
            'south': 'east'
            
        }
    },
    'J': {'north': (-1, 0), 'west': (0, -1),
        'next': {
            'north': 'west',
            'west': 'north',
            'east': 'north',
            'south': 'west'
        }
    },
    '7': {'south': (1, 0), 'west': (0, -1),
        'next': {
            'south': 'west',
            'west': 'south',
            'east': 'south',
            'north': 'west'
        }
    },
    'F': {'south': (1, 0), 'east': (0, 1),
        'next': {
            'north': 'east',
            'west': 'south',
            'east': 'south',
            'south': 'east'
        }
    },
}


def parse_input(filename: str) -> (str, map):
    with open(filename, 'r') as f:
        file_content = f.read().splitlines()
        return file_content


if __name__ == '__main__':

    input_files = []
    input_files.append('../example-input3.txt')
    input_files.append('../example-input4.txt')
    input_files.append('../example-input5.txt')
    input_files.append('../input.txt')
    results = [0, 0, 0, 0]

    for file_index, filename in enumerate(input_files):
        print(f"Processing file: {filename}")
        board = Grid(parse_input(filename))
        print(f"----- Board: -----\n\n{board}\n")
        player = None
        if file_index < 2:
            player = Player(*board.starting_point, pipe="F", direction="east")
        else:
            player = Player(*board.starting_point, pipe="7", direction="south")
        print(f"----- Player: -----\n\n{player}\n\n-------------------")

        keep_going = True
        steps_in_loop = 0
        while keep_going:
            player.nodes.append(Node(player.x, player.y, player.direction, player.pipe))
            steps_in_loop += 1

            # Move the player
            player.move(*pipes[player.pipe][player.direction])
            #print(f"{player}")

            # Get the next pipe and direction
            next_pipe = board.board[player.y][player.x]
            
            # Check if we are done
            if next_pipe == 'S':
                keep_going = False
                break

            direction = player.direction
            next_direction = pipes[next_pipe]['next'][direction]

            # Update pipe and direction
            player.direction = next_direction
            player.pipe = next_pipe

        print(board)
        
        new_board = []
        for row in range(len(board.board)):
            new_row = ['.' for _ in range(len(board.board[row]))]
            new_board.append(new_row)
        for node in player.nodes:
            new_board[node.y][node.x] = node.pipe
        for i, row in enumerate(new_board):
            board.board[i] = "".join(row)
        print(f"\n{board}")

        # Count ground inside the pipe loop
        counter = 0
        for i, row in enumerate(board.board):
            inside = False
            in_out = re.finditer(r'[|]|(L\-*7)|(F\-*J)', row)
            last_match = ""
            for j, this_match in enumerate(in_out, 1):
                if j == 1:
                    last_match = this_match
                    inside = not inside
                    continue
                if last_match and inside:
                    print(f"{i=}:\t{last_match=}\n\t{this_match=}")
                    matched_substring = row[last_match.end():this_match.start()]
                    counter += matched_substring.count('.')
                    print(f"{matched_substring=}")
                inside = not inside

                last_match = this_match
            
        results[file_index] = counter

    print("")
    for result in results:
        print(f"Result: {result}")

    try:
        assert results[0] == 4
    except AssertionError:
        print(f"\nAssertionError: {results[0]} != 4")
    try:
        assert results[1] == 8
    except AssertionError:
        print(f"AssertionError: {results[1]} != 8")
    try:    
        assert results[2] == 10
    except AssertionError:
        print(f"AssertionError: {results[2]} != 10")
