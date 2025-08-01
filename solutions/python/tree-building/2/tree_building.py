from __future__ import annotations

# Note: should be "its" but grammar error is required by tests.
ERR_ORDERING = "Node parent_id should be smaller than it's record_id."
ERR_PARENT_ID = "Only root should have equal record and parent id."
ERR_RECORD_ID = "Record id is invalid or out of order."


class Record:
    def __init__(self, record_id: int, parent_id: int) -> None:
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self.children: list[Node] = []


def BuildTree(records: list[Record]) -> Node | None:  # noqa: N802
    if not records:
        return None

    count = len(records)
    parents = [0] * count
    for r in records:
        if r.parent_id > r.record_id:
            raise ValueError(ERR_ORDERING)
        if r.record_id > 0 and r.parent_id == r.record_id:
            raise ValueError(ERR_PARENT_ID)
        if r.record_id >= count:
            raise ValueError(ERR_RECORD_ID)

        parents[r.record_id] = r.parent_id

    nodes = [Node(i) for i in range(count)]
    for p in sorted(set(parents)):
        nodes[p].children = [nodes[i] for i in range(p + 1, len(parents)) if parents[i] == p]

    return nodes[0]
