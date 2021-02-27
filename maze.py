size = 8
start_sign = '👤'
end_sign = '🚩'
right = '→'
left = '←'
up = '↑'
down = '↓'

moves = [
    {'x':0, 'y':1, 'dir': right}, # move right
    {'x': 0,'y': -1, 'dir': left}, # move left
    {'x': 1, 'y': 0, 'dir': down}, # move down 
    {'x': -1, 'y': 0, 'dir': up} # move up
]

def printMaze(lab, start, end):
    global size
    space = ' '
    for i in range(8):
        for j in range(8):
            if i == mstart.x and j == mstart.y:
                print(start_sign,  end=space)
            elif i == end.x and j == end.y:
                print(end_sign)
            else:
                print(lab[i][j],  end=space)
        print('')

class Position:
    def __init__(self, x, y):
        self. x = x
        self.y = y
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

def isValidMove(start, move):
    return start.x + move['x']>=0 and start.x + move['x']<size \
        and start.y + move['y']>=0 and start.y + move['y']<size

def findSolutions(lab, start, end):
    for move in moves:
        if isValidMove(start, move):
            if lab[start.x + move['x']][start.y + move['y']] == '_':
                lab[start.x][start.y ] = move['dir']
                
                start = Position(start.x + move['x'], start.y + move['y'])
                if start == end:
                    printMaze(lab, start, end)
                    input("Press Enter to continue...")
                findSolutions(lab, start, end)
                start = Position(start.x - move['x'], start.y - move['y'])
                lab[start.x][start.y ] = '_'

if __name__ == "__main__":
    lab = [['_', '_','_', '_', '_', '_', '_', '_'],
        ['_', '_','_', '🀫', '_', '_', '_', '_'],
        ['_', '🀫','_', '_', '🀫', '_', '_', '_'],
        ['_', '_','_', '_', '_', '_', '_', '_'],
        ['_', '_','_', '_', '_', '_', '_', '_'],
        ['_', '_','_', '🀫', '_', '_', '_', '_'],
        ['_', '_','_', '_', '_', '_', '🀫', '_'],
        ['_', '_','_', '_', '_', '_', '_', '_']]
        
    mstart = Position(0,0)
    end = Position(7,7)

    findSolutions(lab, mstart, end)