import math
from utils import calculate_hash
class Node: 
    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right
      
def compute_tree_depth(number_of_leaves: int) -> int:
    return math.ceil(math.log2(number_of_leaves))

def is_power_of_2(leaves: int) -> bool:
    return math.log2(leaves).is_integer()

def fill_set(nodes_list):
    curr_leaves = len(nodes_list)
    if is_power_of_2(curr_leaves):
        return nodes_list
    no_of_leaves = 2**compute_tree_depth(curr_leaves)
    if no_of_leaves % 2 == 0:
        nodes_list += [nodes_list[-2] + nodes_list[-1]]
    else:
        for i in range(curr_leaves, no_of_leaves):
            nodes_list.append(nodes_list[-1])
        return nodes_list

def build_merkle_tree(node_data: [str]) -> Node:
    old_set = [Node(calculate_hash(data))for data in node_data]
    tree_depth = compute_tree_depth(len(old_set))

    for i in range (0, tree_depth):
        num_nodes = 2**(tree_depth-i)
        new_set = []
        for j in range(0, num_nodes, 2):
            c0 = old_set[j]
            c1 = old_set[j+1]
            new_node = Node(value = calculate_hash(f"{c0.value}{c1.value}"), left = c0, right = c1)
            new_set.append(new_node)
        old_set = new_set
    return new_set[0]
