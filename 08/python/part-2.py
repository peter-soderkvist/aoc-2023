import math

class Node():
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right
        
    def __str__(self):
        return f"name={self.name}, left={self.left}, right={self.right}"


def parse_input(filename: str) -> (str, map):
    with open(filename, 'r') as f:
        file_content = f.readlines()
        instructions = ""
        nodes = {}
        
        for i, line in enumerate(file_content):
            if i == 0:
                instructions = line.strip()
            if i > 1:
                line_split = line.split('=')
                dest_l, dest_r = line_split[1].strip().replace('(', '').replace(')', '').split(',')
                name = line_split[0].strip()
                nodes[name] = Node(name=name, left=dest_l.strip(), right=dest_r.strip())


        return instructions, nodes


if __name__ == '__main__':

    input_files = ['../input.txt']
    input_files.append('../example-input2.txt')
    input_files.append('../example-input3.txt')
    input_files.append('../input.txt')

    for filename in input_files:
        instructions, nodes = parse_input(filename=filename)
        start_nodes = [node for node in nodes.values() if node.name.endswith('A')]
        required_steps = []

        for outer_node in start_nodes:
            steps_required = 0
            keep_going = True
            next_node = outer_node.name
    
            while keep_going:
                for instruction in instructions:
                    node = nodes[next_node]
                    steps_required += 1
                    
                    match instruction:
                        case 'L':
                            next_node = node.left
                        case 'R':
                            next_node = node.right
                            
                    if next_node.endswith('Z'):
                        keep_going = False
                        print(f"Finished with {outer_node.name=} after {steps_required=} steps")
                        required_steps.append(steps_required)
                        break
    
        lcm = math.lcm(*required_steps)
        print(f"\n{filename}: {steps_required=}\n{required_steps=}\n{lcm=}")
