import sys


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
    input_files.append('../example-input.txt')
    input_files.append('../example-input2.txt')
    input_files.append('../input.txt')
    results = [0, 0, 0]

    for file_index, filename in enumerate(input_files):
        print(f"Processing file: {filename}")
        board = Grid(parse_input(filename))
        print(f"----- Board: -----\n\n{board}\n")
        player = None
        if file_index < 2:
            player = Player(*board.starting_point, pipe="F", direction="east")
        else:
            player = Player(*board.starting_point, pipe="|", direction="north")
        print(f"----- Player: -----\n\n{player}\n\n-------------------")

        keep_going = True
        steps_in_loop = 0
        while keep_going:
            steps_in_loop += 1
            
            # Move the player
            player.move(*pipes[player.pipe][player.direction])
            print(f"{player}")
            
            # Get the next pipe and direction
            next_pipe = board.board[player.y][player.x]
            
            # Check if we are done
            if next_pipe == 'S':
                keep_going = False
                break
            
            print(f"{player.pipe=}, {next_pipe=}")
            direction = player.direction
            print(f"{direction=}")
            next_direction = pipes[next_pipe]['next'][direction]
            print(f"{next_direction=}")

            # Update pipe and direction
            player.direction = next_direction
            player.pipe = next_pipe
            print(f"{player}\n")

        results[file_index] += int(steps_in_loop / 2)

    try:
        assert results[0] == 4
    except AssertionError:
        print(f"\nAssertionError: {results[0]} != 4")
    try:    
        assert results[1] == 8
    except AssertionError:
        print(f"AssertionError: {results[1]} != 8")
        sys.exit(1)


    for result in results:
        print(f"Result: {result}")
