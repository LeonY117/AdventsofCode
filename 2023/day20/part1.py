from typing import List, Dict
from collections import OrderedDict


class FlipFlop:
    def __init__(self, children: List[str], name):
        self.children = children
        self.state = 0
        self.name = name
        self.received = []

    def receive(self, pulse: int, *args) -> None:
        self.received.append(pulse)

    def send(self) -> Dict[str, int]:
        out = {}
        pulse = self.received.pop(0)
        if pulse == 0:
            self.state = int(not self.state)
            for child in self.children:
                # print(f"{self.name}: {self.state}-> {child}")
                out[child] = self.state

        return out

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

    def send(self) -> Dict[str, int]:
        out = {}
        state = int(not all(self.parents.values()))
        for child in self.children:
            # print(f"{self.name}: {state}-> {child}")
            out[child] = state
        return out

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

    def send(self) -> Dict[str, int]:
        out = {}
        for child in self.children:
            # print(f"{self.name}: {self.state}-> {child}")
            out[child] = self.state
        return out

    def __repr__(self) -> str:
        return f"Broadcaster: {self.children}"

    def get_state(self):
        return ""


class Button:
    def __init__(self, children, name):
        self.children = children
        self.name = name

    def send(self) -> Dict[str, int]:
        out = {}
        for child in self.children:
            out[child] = 0
        return out

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
        return {}


# didn't end up being useful
def get_machine_state(modules):
    out = ""
    for mod in modules:
        out += modules[mod].get_state()

    return out


def solution(inp):
    modules = OrderedDict()

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

        modules[module_name] = module(children_names, module_name)

    # map children to parents
    # and add unknown modules (there's actually only one)
    unknown_modules = {}
    for name, module in modules.items():
        for child in module.children:
            if child in modules and type(modules[child]) == Conjunction:
                modules[child].add_parent(name)
            elif child not in modules and child not in unknown_modules:
                unknown_modules[child] = UnknownModule(child)

    modules = {**modules, **unknown_modules}

    # add the button module
    button = Button(["broadcast"], "button")
    modules["button"] = button

    pulse_count = {0: 0, 1: 0}
    for _ in range(1000):
        queue = ["button"]
        while queue:
            module = modules[queue.pop(0)]
            # a dictionary of {name: pulse} of outbound signals
            outbound = module.send()
            for receiver, pulse in outbound.items():
                modules[receiver].receive(pulse, module.name)
                pulse_count[pulse] += 1
                queue.append(receiver)

    return pulse_count[0] * pulse_count[1]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    print(solution(lines))
