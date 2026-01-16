# Problem Set 4A
# Name:
# Collaborators:

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(
    5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))
)
tree_test = Node(1, Node(1, (Node(1, Node(1, Node(1, Node(1)))))))

print(tree_test)


def find_tree_height(tree):
    """
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    """
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return 0

    left = tree.get_left_child()
    right = tree.get_right_child()

    left_height = find_tree_height(left) if left else 0
    right_height = find_tree_height(right) if right else 0

    return 1 + max(left_height, right_height)


print(
    find_tree_height(tree1),
    find_tree_height(tree2),
    find_tree_height(tree3),
    find_tree_height(tree_test),
)


def max_compare_func(child_value, parent_value):
    if child_value < parent_value:
        return True
    return False


def min_compare_func(child_value, parent_value):
    if child_value > parent_value:
        return True
    return False


def is_heap(tree, compare_func):
    """
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    """
    # base case
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True

    # for recursive step, start with reaching the children
    left = tree.get_left_child()
    right = tree.get_right_child()
    parent_value = tree.get_value()

    if left:  # i.e., if parent was not a leaf for the left side
        if not compare_func(left.get_value(), parent_value):
            # any False means all are False
            return False

    if right:  # same thing, on the right side
        if not compare_func(right.get_value(), parent_value):
            return False

    return (
        is_heap(tree.get_left_tree, compare_func) is True
        and is_heap(tree.get_right_tree, compare_func) is True
    )


max = is_heap(tree3, max_compare_func)
min = is_heap(tree3, min_compare_func)
print(max, min)

if __name__ == "__main__":
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
