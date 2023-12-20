from typing import List
from collections import OrderedDict

MODULES = OrderedDict()


class FlipFlop:
    def __init__(self, children: List[str], name):
        self.children = children
        self.state = 0
        self.name = name

    def receive(self, pulse: int, *args) -> None:
        if pulse == 0:
            self.state = int(not self.state)
        else:
            pass

    def send(self) -> None:
        for child in self.children:
            print(f"{self.name} sends {self.state} to {child}")
            MODULES[child].receive(self.state, self.name)

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

    def send(self) -> None:
        state = int(not all(self.parents.values()))
        for child in self.children:
            print(f"{self.name} sends {state} to {child}")
            MODULES[child].receive(state, self.name)

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

    def send(self):
        assert self.state != None
        for child in self.children:
            print(f"{self.name} sends {self.state} to {child}")
            MODULES[child].receive(self.state, self.name)

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

    def get_state(self):
        return ""


def get_machine_state():
    out = ""
    for mod in MODULES:
        out += MODULES[mod].get_state()

    return out


def solution(inp):
    for line in inp:
        module, children = line.split(" -> ")
        module_type = module[0]
        module_name = module[1:]
        children_names = children.split(", ")
        print(children_names)

        if module_type == "%":
            module = FlipFlop

        elif module_type == "&":
            module = Conjunction

        elif module_type == "b":
            module_name = "broadcast"
            module = Broadcast

        MODULES[module_name] = module(children_names, module_name)

    for name, module in MODULES.items():
        for child in module.children:
            if child in MODULES and type(MODULES[child]) == Conjunction:
                MODULES[child].add_parent(name)

    button = Button(["broadcast"], "button")
    MODULES["button"] = button
    print(button.children)

    for _ in range(1):
        curr_state = get_machine_state()
        print(curr_state)
        queue = ["button"]
        for _ in range(20):
            print(queue)
            module = MODULES[queue.pop(0)]
            module.send()
            queue.extend(module.children)

            print(get_machine_state())


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
