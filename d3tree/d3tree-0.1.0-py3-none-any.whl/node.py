import reprlib
import sys
from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Node(list):
    name: str
    children: Union["Node", List] = field(default_factory=lambda: [])

    def insert_node(self, path: List[str]) -> None:
        if not path:
            return

        parent: str = path[0]
        child: List[str] = path[1:]

        parent_node = [x for x in self.children if x.name == parent]
        if not parent_node:
            parent_node = Node(name=parent)
            self.children.append(parent_node)

        parent_node.insert_node(path=child)  # type: ignore

    @reprlib.recursive_repr()
    def __repr__(self) -> str:
        reprlib.aRepr.maxlevel = sys.getrecursionlimit()
        return f"""{{"name":"{self.name}","children":[{','.join(map(repr, self.children))}]}}"""


if __name__ == "__main__":
    root = Node(name="/")

    with open(file="../../tests/data/filepath.txt", mode="r") as f:
        lines = filter(None, (line.strip() for line in f))
        for line in lines:
            root.insert_node(path=line.split("/"))

    res = f"treeData = {root};"
    print(f"root: {root}")
