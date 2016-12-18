from queue import PriorityQueue
from abc import ABCMeta, abstractmethod

__author__ = 'maubry'


class AStarSearch(metaclass=ABCMeta):
    search_until_and_continue = False

    @abstractmethod
    def heuristic(self, current, next):
        pass

    @abstractmethod
    def neighbors(self, current):
        pass

    @abstractmethod
    def cost(self, current, next):
        pass

    @abstractmethod
    def search_until(self, current, goal):
        pass

    def a_star_search(self, graph, start, goal, ):
        frontier = PriorityQueue()
        current = (0, start)
        frontier.put(current)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            _, current = frontier.get()

            if self.search_until(current, goal):
                if self.search_until_and_continue:
                    continue
                break

            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current

        return came_from, cost_so_far, current