from typing import List
from collections import OrderedDict

MODULES = OrderedDict()

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

    def receive(self, *args):
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


def solution(inp):
    global MODULES

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

    button = Button(["broadcast"], "button")
    MODULES["button"] = button

    state_history = {}
    curr_state = get_machine_state()
    for i in range(1000):
        queue = ["button"]
        while queue:
            module = MODULES[queue.pop(0)]
            if module.send():
                queue.extend(module.children)

        state_history[curr_state] = PULSE_COUNT.copy()
        PULSE_COUNT[0], PULSE_COUNT[1] = 0, 0

        curr_state = get_machine_state()
        if curr_state in state_history.keys():
            print(f"found loop on iteration {i}")
            break
    print(len(state_history))
    # print(state_history.values())
    TOTAL_ITER = 1000
    NUM_LOOPS = TOTAL_ITER // len(state_history)
    LEFTOVER = TOTAL_ITER % len(state_history)
    # print(state_history)
    total_highs, total_lows = 0, 0
    for counts in state_history.values():
        total_lows += counts[0]
        total_highs += counts[1]

    total_lows *= NUM_LOOPS
    total_highs *= NUM_LOOPS

    for counts in list(state_history.values())[:LEFTOVER]:
        total_lows += counts[0]
        total_highs += counts[1]
    print(total_highs, total_lows)
    return total_lows * total_highs


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
