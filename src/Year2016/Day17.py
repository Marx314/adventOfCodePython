import hashlib
from src.AStarSearch import AStarSearch
from src.AStarSearch import AStarSearchGraph

DOOR_OPEN = 'bcdef'
OPEN = '1'
CLOSED = '0'


class Day17(AStarSearch, AStarSearchGraph):
    @staticmethod
    def first_four_from_md5(key):
        return hashlib.md5(key.encode('utf-8')).hexdigest()[0:4]

    @staticmethod
    def generate_move(door_status):
        return {
            'UP': OPEN if door_status[0] in DOOR_OPEN else CLOSED,
            'DOWN': OPEN if door_status[1] in DOOR_OPEN else CLOSED,
            'LEFT': OPEN if door_status[2] in DOOR_OPEN else CLOSED,
            'RIGHT': OPEN if door_status[3] in DOOR_OPEN else CLOSED
        }

    def calculate_path(self, start):
        initial_hash = start[1]
        goal = ((3, 3), '')
        came_from, cost_so_far, current = self.a_star_search(self, start, goal)
        path = current[1].replace(initial_hash, '')
        return path

    def calculate_longest_path(self, start):
        self.search_until_and_continue = True
        goal = ((3, 3), '')
        came_from, cost_so_far, current = self.a_star_search(self, start, goal)
        solutions = [v[1] for k, v in came_from.items() if k[0] == (3, 3)]
        s = sorted(solutions, key=len)
        return len(s[-1]) - len(start[1]) + 1

    def heuristic(self, goal, current, next):
        return 0

    def cost(self, current, next):
        return 1

    def search_until(self, current, goal):
        return current[0] == goal[0]

    def neighbors(self, current):
        moves = self.generate_move(self.first_four_from_md5(current[1]))
        allowed_next = []
        for move, door in moves.items():
            if door is OPEN:
                if current[0][0] < 3 and move == 'DOWN':
                    allowed_next.append(((current[0][0] + 1, current[0][1]), current[1] + 'D'))
                elif current[0][0] > 0 and move == 'UP':
                    allowed_next.append(((current[0][0] - 1, current[0][1]), current[1] + 'U'))
                elif current[0][1] > 0 and move == 'LEFT':
                    allowed_next.append(((current[0][0], current[0][1] - 1), current[1] + 'L'))
                elif current[0][1] < 3 and move == 'RIGHT':
                    allowed_next.append(((current[0][0], current[0][1] + 1), current[1] + 'R'))
        return allowed_next
