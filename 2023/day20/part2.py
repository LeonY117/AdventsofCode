from typing import List
from collections import OrderedDict
from math import lcm

MODULES = OrderedDict()
parents_reached = {}

PULSE_COUNT = {0: 0, 1: 0}


class FlipFlop:
    def __init__(self, children: List[str], name):
        self.children = children
        self.state = 0
        self.name = name
        self.received = []

    def receive(self, pulse: int, *args) -> None:
        self.received.append(pulse)

    def send(self) -> bool:
        pulse = self.received.pop(0)
        if pulse == 0:
            self.state = int(not self.state)
            for child in self.children:
                # print(f"{self.name}: {self.state}-> {child}")
                MODULES[child].receive(self.state, self.name)
                PULSE_COUNT[self.state] += 1
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"FlipFlop: {self.children}"

    def get_state(self) -> str:
        return str(self.state)


class Conjunction:
    def __init__(self, children: List[str], name):
        self.children = children
        self.parents = {}
        self.name = name

    def add_parent(self, parent: str):
        self.parents[parent] = 0

    def receive(self, pulse: int, parent: str) -> None:
        self.parents[parent] = pulse

        if self.name in parents_reached:
            if int(not all(self.parents.values())):
                parents_reached[self.name] = True

    def send(self) -> bool:
        state = int(not all(self.parents.values()))
        for child in self.children:
            # print(f"{self.name}: {state}-> {child}")
            MODULES[child].receive(state, self.name)
            PULSE_COUNT[state] += 1
        return True

    def __repr__(self) -> str:
        return f"Conjunct: {self.children}"

    def get_state(self):
        return "".join([str(v) for v in self.parents.values()])


class Broadcast:
    def __init__(self, children: List[str], name):
        self.children = children
        self.state = None
        self.name = name

    def receive(self, pulse, *args):
        self.state = pulse

    def send(self) -> bool:
        assert self.state != None
        for child in self.children:
            # print(f"{self.name}: {self.state}-> {child}")
            MODULES[child].receive(self.state, self.name)
            PULSE_COUNT[self.state] += 1
        return True

    def __repr__(self) -> str:
        return f"Broadcaster: {self.children}"

    def get_state(self):
        return ""


class Button:
    def __init__(self, children, name):
        self.children = children
        self.name = name

    def send(self):
        for child in self.children:
            MODULES[child].receive(0, self.name)
            PULSE_COUNT[0] += 1
        return True

    def get_state(self):
        return ""


class UnknownModule:
    def __init__(self, name):
        self.name = name

    def receive(self, pulse, *args):
        pass

    def add_parent(self, *args):
        pass

    def get_state(self):
        return ""

    def send(self):
        return False


def get_machine_state():
    out = ""
    for mod in MODULES:
        out += MODULES[mod].get_state()

    return out


def check_conjunction_state(module: Conjunction):
    return int(not all(module.parents.values()))


def solution(inp):
    global MODULES
    global parents_reached

    for line in inp:
        module, children = line.split(" -> ")
        module_type = module[0]
        module_name = module[1:]
        children_names = children.split(", ")
        if module_type == "%":
            module = FlipFlop
        elif module_type == "&":
            module = Conjunction
        elif module_type == "b":
            module_name = "broadcast"
            module = Broadcast

        MODULES[module_name] = module(children_names, module_name)

    unknown_modules = {}
    for name, module in MODULES.items():
        for child in module.children:
            if child in MODULES and type(MODULES[child]) == Conjunction:
                MODULES[child].add_parent(name)
            elif child not in MODULES and child not in unknown_modules:
                unknown_modules[child] = UnknownModule(child)

    MODULES = {**MODULES, **unknown_modules}

    parents_reached = {p: None for p in MODULES["tj"].parents.keys()}
    parent_loops = {p: None for p in MODULES["tj"].parents.keys()}

    button = Button(["broadcast"], "button")
    MODULES["button"] = button

    for i in range(10000):
        queue = ["button"]
        while queue:
            module = MODULES[queue.pop(0)]
            if module.send():
                queue.extend(module.children)

        for parent, received in parents_reached.items():
            if received and parent_loops[parent] == None:
                parent_loops[parent] = i + 1

        if all(parents_reached.values()):
            print(parents_reached)
            print(parent_loops)
            break

    return lcm(*parent_loops.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
