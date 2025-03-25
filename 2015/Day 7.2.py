from enum import Enum

class Operator(Enum):
    DIRECT = 0
    NOT = 1
    AND = 2
    OR = 3
    LSHIFT = 4
    RSHIFT = 5

class Wire:
    def __init__(self, 
                 operator: Operator,
                 left_name: str = None, 
                 right_name: str = None,
                 left_value: int = None, 
                 right_value: int = None,
                 value: int = None):
        
        self.operator = operator
        self.left_name = left_name
        self.right_name = right_name
        self.left_value = left_value
        self.right_value = right_value
        self.value = value

class BreadBoard:
    def __init__(self, wires: dict[str : Wire]):
        self.wires = wires
        return
    
    def add(self, name: str, wire: Wire):
        self.wires.update({name: wire})
        return

    def get(self, name: str) -> Wire:
        return self.wires[name]
    
    def change_variables(self, name: str, wire: Wire):
        if wire.left_name is not None:
            self.wires[name].left_name = wire.left_name
        if wire.right_name is not None:
            self.wires[name].right_name = wire.right_name
        if wire.left_value is not None:
            self.wires[name].left_value = wire.left_value
        if wire.right_value is not None:
            self.wires[name].right_value = wire.right_value
        if wire.value is not None:
            self.wires[name].value = wire.value
        return

def get_wire_value(board: BreadBoard, name: str) -> int:
    if name not in board.wires:
        board.add(name, Wire(Operator.DIRECT, left_value=0))
    
    wire = board.get(name)

    if wire.value is not None:
        return wire.value

    left: int = None
    right: int = None

    if wire.left_name is not None:
        left = get_wire_value(board, wire.left_name)
    elif wire.left_value is not None:
        left = wire.left_value

    if wire.right_name is not None:
        right = get_wire_value(board, wire.right_name)
    elif wire.right_value is not None:
        right = wire.right_value

    match wire.operator:
        case Operator.DIRECT:
            wire.value = left
        case Operator.NOT:
            wire.value = ~ left
        case Operator.AND:
            wire.value = left & right
        case Operator.OR:
            wire.value = left | right
        case Operator.LSHIFT:
            wire.value = left * (2**right)
        case Operator.RSHIFT:
            wire.value = left // (2**right)
    return wire.value

def main():
    print("Input:")
    
    board = BreadBoard(wires={})
    while True:
        try:
            instruction = input()
            if instruction.strip() == "":
                break
            
            words: list[str] = instruction.split(" ")

            name: str = None
            operator: Operator = None
            left: str = None
            right: str = None
            left_name: str = None
            right_name: str = None
            left_value: int = None
            right_value: int = None

            if words[1] == "->":
                operator = Operator.DIRECT
                left = str(words[0])
                name = str(words[2])
            
            elif words[0] == "NOT":
                operator = Operator.NOT
                left = str(words[1])
                name = str(words[3])

            elif words[1] == "AND":
                operator = Operator.AND
                left = str(words[0])
                right = str(words[2])
                name = str(words[4])

            elif words[1] == "OR":
                operator = Operator.OR
                left = str(words[0])
                right = str(words[2])
                name = str(words[4])

            elif words[1] == "LSHIFT":
                operator = Operator.LSHIFT
                left = str(words[0])
                right = str(words[2])
                name = str(words[4])

            elif words[1] == "RSHIFT":
                operator = Operator.RSHIFT
                left = str(words[0])
                right = str(words[2])
                name = str(words[4])
            
            if left.isnumeric():
                left_value = int(left)
            else:
                left_name = left

            if right is not None and right.isnumeric():
                right_value = int(right)
            else:
                right_name = right

            board.add(name, Wire(operator, left_name, right_name, left_value, right_value))

        except EOFError:
            break

    board.change_variables('b', Wire(operator=Operator.DIRECT, value=16076))

    print(f"Signal provided to wire 'a': {get_wire_value(board, 'a')}")

if __name__ == "__main__":
    main()
