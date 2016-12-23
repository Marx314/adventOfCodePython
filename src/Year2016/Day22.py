import functools
import copy
import re
from src import split_data
from src.AStarSearch import AStarSearch


class Day22(object):
    @split_data
    def build_map(self, sysout):
        sysout.pop(0)
        sysout.pop(0)
        fs = {}
        for output in sysout:
            x, y, size, used, avail, use = map(int, re.findall('(\d+)', output))
            if x not in fs:
                fs[x] = {}
            fs[x][y] = {'Used': used, 'Avail': avail, 'x': x, 'y': y}
        return fs

    def count_pairs(self, sysout):
        fs = self.build_map(sysout)
        nodes = []
        for x in range(len(fs)):
            for y in range(len(fs[x])):
                nodes.append(fs[x][y])
        nodes_by_avail = sorted(nodes, key=lambda node: -node['Avail'])
        nodes_by_used = sorted(nodes, key=lambda node: node['Used'])
        return self.count_possible_pairs(nodes_by_avail, nodes_by_used)

    @staticmethod
    def count_possible_pairs(nodes_by_avail, nodes_by_used):
        count = 0
        for node_used in nodes_by_used:
            if node_used['Used'] != 0:
                possible_pairs = []
                for node_available in nodes_by_avail:
                    if node_available['Avail'] > node_used['Used']:
                        if (node_available['x'], node_available['y']) is not (node_used['x'], node_used['y']):
                            possible_pairs.append(node_available)
                    else:
                        break
                count += len(possible_pairs)
        return count

    def shortest_path_to_wall(self, sysout):
        pf = PathFinding()
        result = self.build_map(sysout)
        file_system = FileSystem(result)
        night_watch = file_system.find_night_watch()
        came_from, cost_so_far, current = pf.a_star_search(pf, file_system, night_watch)
        return cost_so_far[current]

    def shortest_path(self, sysout):
        pf = PathFinding()
        result = self.build_map(sysout)
        file_system = FileSystem(result)
        path_length = 0
        goal = (len(result) - 2, 0)

        if file_system.has_wall():
            path_length = self.shortest_path_to_wall(sysout)

            self.move_free_node_to_night_watch(file_system)

        came_from, cost_so_far, current = pf.a_star_search(pf, file_system, goal)
        path_length += cost_so_far[current]

        path_length += 5 * goal[0] + 1  # Move from goal to top corner

        return path_length

    @staticmethod
    def move_free_node_to_night_watch(file_system):
        nx, ny = file_system.find_night_watch()
        x, y = file_system.find_empty()
        old_node = file_system.fs[nx][ny]
        file_system.fs[nx][ny] = file_system.fs[x][y]
        file_system.fs[x][y] = old_node


class PathFinding(AStarSearch):
    def neighbors(self, current):
        moves = []
        x, y = current.find_empty()
        available_space = current.fs[x][y]['Avail']
        if y >= 1 and current.fs[x][y - 1]['Used'] <= available_space:
            move = self.apply_move(current, (x, y), (x, y - 1))
            moves.append(move)
        if y < len(current.fs[0]) - 1 and x > 0 and current.fs[x - 1][y]['Used'] <= available_space:
            move = self.apply_move(current, (x, y), (x - 1, y))
            moves.append(move)
        if x < len(current.fs) - 1 and current.fs[x + 1][y]['Used'] <= available_space:
            move = self.apply_move(current, (x, y), (x + 1, y))
            moves.append(move)
        if y < len(current.fs[0]) - 1 and x > 0 and current.fs[x][y + 1]['Used'] <= available_space:
            move = self.apply_move(current, (x, y), (x, y + 1))
            moves.append(move)
        return moves

    def heuristic(self, goal, current, next):
        dist_next = self.distance_between(next.find_empty(), goal)
        dist_current = self.distance_between(current.find_empty(), goal)
        if dist_next < dist_current:
            return -100 + dist_next * 2
        return 1

    @staticmethod
    @functools.lru_cache(maxsize=0)
    def distance_between(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def cost(self, current, next):
        return 1

    def search_until(self, current, goal):
        empty = current.find_empty()
        if empty == goal:
            return True

    @staticmethod
    def apply_move(current, source, destination):
        move = current.copy()
        node_source = current.fs[source[0]][source[1]]
        move.fs[source[0]][source[1]] = current.fs[destination[0]][destination[1]]
        move.fs[destination[0]][destination[1]] = node_source

        return move


class FileSystem(object):
    fs = None

    def __init__(self, fs):
        self.fs = fs

    def find_goal(self, goal):
        for x in range(len(self.fs)):
            for y in range(len(self.fs[x])):
                if (self.fs[x][y]['x'], self.fs[x][y]['y']) == goal:
                    return x, y

    def has_wall(self):
        for x in range(len(self.fs)):
            for y in range(len(self.fs[x])):
                if self.fs[x][y]['Used'] > 400:
                    return True

    def find_night_watch(self):
        for x in range(len(self.fs)):
            for y in range(len(self.fs[x])):
                if self.fs[x][y]['Used'] > 400:
                    if self.fs[x - 1][y]['Used'] < 400:
                        return x - 1, y

    def find_empty(self):
        for x in range(len(self.fs)):
            for y in range(len(self.fs[x])):
                if self.fs[x][y]['Used'] == 0:
                    return x, y

    def __lt__(self, other):
        return self.__repr__().__lt__(repr(other))

    def __hash__(self):
        return self.__repr__().__hash__()

    def __repr__(self):
        r = ''
        for x in range(len(self.fs)):
            for y in range(len(self.fs[x])):
                r += repr(self.fs[x][y])
            r += '\n'
        return r

    def copy(self):
        return FileSystem(copy.deepcopy(self.fs))
