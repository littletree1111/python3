class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        seen = {head: Node(head.val)}

        node = head

        while node:
            copy = seen[node]
            if node.random:
                # if the node has a non-None random node

                if node.random not in seen:
                    # create the random node
                    rannode = Node(node.random.val)
                    seen[node.random] = rannode
                copy.random = seen[node.random]

            if node.next:
                if node.next not in seen:
                    # create the next node and append the newly created node
                    # if next exists and hasn't already been created
                    newnode = Node(node.next.val)
                    seen[node.next] = newnode
                copy.next = seen[node.next]

            node = node.next
        return seen[head]
