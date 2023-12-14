class Galaxy:
    def __init__(self, number: int, x: int, y: int):
        self.number = number
        self.x = x
        self.y = y


class Grid:
    def __init__(self, grid: list):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __str__(self):
        return "\n".join(["".join(row) for row in self.grid])

    def find_empty_columns(self) -> list:
        empty_columns = []
        for i in range(len(self.grid[0])):
            no_galaxies = True
            for row in self.grid:
                if row[i] != '.':
                    no_galaxies = False
                    break
            if no_galaxies:
                empty_columns.append(i)
        print(f"{empty_columns=}")
        return empty_columns
    
    def find_empty_rows(self) -> list:
        empty_rows = []
        for i, row in enumerate(self.grid):
            no_galaxies = True
            for char in row:
                if char != '.':
                    no_galaxies = False
                    break
            if no_galaxies:
                empty_rows.append(i)
        print(f"{empty_rows=}")
        return empty_rows

    def insert_empty_space(self):
        for col in reversed(self.find_empty_columns()):
            for i, row in enumerate(self.grid):
                self.grid[i].insert(col + 1, '.')
        for row in reversed(self.find_empty_rows()):
            self.grid.insert(row + 1, ['.'] * len(self.grid[0]))



def parse_input(filename):
    grid = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    return grid


if __name__ == '__main__':
    input_files = []
    input_files.append('../example-input.txt')
    input_files.append('../input.txt')
    results = [0, 0]
    
    for file_index, filename in enumerate(input_files):
        print(f"Input file: {filename}")
        
        grid = Grid(parse_input(filename))        
        print(f"\n{grid}")
        grid.insert_empty_space()

        galaxies = []
        counter = 1
        for i, line in enumerate(grid.grid):
            for j, char in enumerate(line):
                if char == '#':
                    #grid.grid[i][j] = str(counter)
                    galaxies.append(Galaxy(number=counter, x=j, y=i))
                    counter += 1
        print(f"\n{grid}")
        
        # Get possible galaxy pairs
        pairs = []
        for i, galaxy in enumerate(galaxies):
            for j in range(i+1, len(galaxies)):
                pairs.append((galaxy.number, galaxies[j].number))

        # Calculate distances between pairs
        print(f"{len(grid.grid)=}")
        print(f"{len(pairs)=}")
        print(f"{pairs[-1]=}")
        for pair in pairs:
            galaxy1, galaxy2 = pair
            galaxy1, galaxy2 = galaxies[galaxy1-1], galaxies[galaxy2-1]
            #print(f"Galaxy {galaxy1.number} ({galaxy1.x}, {galaxy1.y})")
            #print(f"Galaxy {galaxy2.number} ({galaxy2.x}, {galaxy2.y})")
            distance = abs(galaxy1.x - galaxy2.x) + abs(galaxy1.y - galaxy2.y)

            #print(f"Distance: {distance}")
            results[file_index] += distance

    print("")
    for result in results:
        print(f"Result: {result}")

    try:
        assert results[0] == 374
    except AssertionError:
        print(f"\nAssertionError: {results[0]} != 374")
