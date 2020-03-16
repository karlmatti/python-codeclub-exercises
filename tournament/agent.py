import random
from typing import NamedTuple
from uuid import uuid4


class Action:
    SUCK = "suck"
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    NOOP = "noop"

    COST_MAP = {
        SUCK: 2,
        LEFT: 1,
        RIGHT: 1,
        UP: 1,
        DOWN: 1,
        NOOP: 0,
    }


class Point(NamedTuple):
    dirty: bool
    uuid: str  # generated from str(uuid.uuid4)


class Agent:
    AUTHOR = "karlmatti@hotmail.com"
    NAME = "Karl M"
    ACTION = Action

    def __init__(self):
        self.last_move = Action.RIGHT
        self.move_before_last = Action.LEFT
        self.last_id = 'a'
        self.next_move = Action.NOOP

    def __str__(self) -> str:

        return str(self.NAME)

    def step(self, perception: Point) -> str:

        if perception.dirty:
            self.last_id = perception.uuid
            self.move_before_last = self.last_move
            self.last_move = Action.SUCK

            self.next_move = self.move_before_last
            print(1)
            return self.last_move

        elif perception.uuid == self.last_id:
            print(2)
            self.last_id = perception.uuid
            if self.last_move == Action.LEFT:
                self.move_before_last = self.last_move
                self.last_move = Action.RIGHT
                return self.last_move
            elif self.last_move == Action.RIGHT:
                self.move_before_last = self.last_move
                self.last_move = Action.LEFT
                return self.last_move
            elif self.last_move == Action.UP:
                self.move_before_last = self.last_move
                self.last_move = Action.DOWN
                return self.last_move
            elif self.last_move == Action.DOWN:
                self.move_before_last = self.last_move
                self.last_move = Action.UP
                return self.last_move

        elif self.last_move == self.move_before_last and self.last_move != Action.SUCK:
            print(3)
            self.last_id = perception.uuid
            self.move_before_last = self.last_move
            if self.last_move == Action.LEFT:
                self.move_before_last = self.last_move
                self.last_move = random.choice([Action.LEFT, Action.UP, Action.DOWN])
                return self.last_move
            elif self.last_move == Action.RIGHT:
                self.move_before_last = self.last_move
                self.last_move = random.choice([Action.RIGHT, Action.UP, Action.DOWN])
                return self.last_move
            elif self.last_move == Action.UP:
                self.move_before_last = self.last_move
                self.last_move = random.choice([Action.RIGHT, Action.LEFT, Action.UP])
                return self.last_move
            elif self.last_move == Action.DOWN:
                self.move_before_last = self.last_move
                self.last_move = random.choice([Action.RIGHT, Action.LEFT, Action.DOWN])
                return self.last_move
        else:
            self.move_before_last = self.last_move
            self.last_move = random.choice([Action.RIGHT, Action.LEFT, Action.UP, Action.DOWN])
            return self.last_move






Robot = Agent
dusty_room_map = {}
dim = 3
for x in range(1, 1 + dim):
    for y in range(1, 1 + dim):
        dusty_room_map[(x, y)] = Point(True, str(uuid4()))

# random wall
del dusty_room_map[(2, 3)]

agent = Robot()
agent_pos = (1, 1)
agent_score = 0
agent_steps = 0

# while any rooms are dirty, run simulation
while any(room.dirty for room in dusty_room_map.values()):
    # count the iterations
    agent_steps += 1

    current_room = dusty_room_map[agent_pos]

    agent_action = agent.step(current_room)

    x, y = agent_pos
    left_pos = (x - 1, y)
    right_pos = (x + 1, y)
    up_pos = (x, y - 1)
    down_pos = (x, y + 1)

    if agent_action == Action.LEFT and left_pos in dusty_room_map:
        agent_pos = left_pos

    elif agent_action == Action.RIGHT and right_pos in dusty_room_map:
        agent_pos = right_pos

    elif agent_action == Action.UP and up_pos in dusty_room_map:
        agent_pos = up_pos

    elif agent_action == Action.DOWN and down_pos in dusty_room_map:
        agent_pos = down_pos

    elif agent_action == Action.SUCK:
        agent_score += current_room.dirty
        dusty_room_map[agent_pos] = Point(False, current_room.uuid)

    for y_pos in range(1, dim + 1):
        print("")
        for x_pos in range(1, dim + 1):
            pos = (x_pos, y_pos)
            point = dusty_room_map.get(pos)

            if pos == agent_pos:
                print("R", end=" ")
            elif not point:
                print("#", end=" ")
            elif point.dirty:
                print("o", end=" ")
            else:
                print(".", end=" ")

    print("agent is in:{} total dirt:{} last action:{}".format(
        agent_pos,
        sum(room.dirty for room in dusty_room_map.values()),
        agent_action,
    ))

print("Done")