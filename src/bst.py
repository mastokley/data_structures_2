

class BST(object):
    """Creates a BST class."""

    def __init__(self, node=None):
        """Instantiate a new binary sorted tree object."""
        self.head = node
        self.head.parent = None
        self._size = 0 if self.head is None else self._size == 1

    def insert(self, val):
        """Inserts a node into binary search tree."""
        try:
            float(val)
        except ValueError:
            raise ValueError('BST only accepts integers, floats.')

        new_node = BSTNode(val)
        if not self.head:
            self._size += 1
            self.head = new_node
        else:
            new_parent = self._find_parent(new_node, self.head)
            if new_parent is not None:
                self._size += 1
                if new_parent.val > new_node.val:
                    new_parent.l_child = new_node
                else:
                    new_parent.r_child = new_node

    def contains(self, val):
        if not self.head:
            return False
        dummy = BSTNode(val)
        return not self._find_parent(dummy, self.head)

    def size(self):
        return self._size

    def depth(self, start=None):
        if self.head is None:
            return 0
        last_node = None
        current_node = self.head
        current_depth = 1
        max_depth = 1
        if start is None:
            start = self.head
        while True:
            # if moving down, keep moving down and left
            if (current_node.l_child is not None and
                last_node == current_node.parent):
                current_depth += 1
                last_node = current_node
                current_node = current_node.l_child

            # if you can't move left, move down right
            elif (current_node.r_child is not None and
                  last_node != current_node.r_child):
                current_depth += 1
                last_node = current_node
                current_node = current_node.r_child

            elif (current_node.parent is not None and
                  current_node != start):
                current_depth -= 1
                last_node = current_node
                current_node = current_node.parent

            if current_depth > max_depth:
                max_depth = current_depth

#            if (current_node == start and
#                (last_node == self.head.r_child or
#             (self.head.r_child is None and )))

# TODO: rewrite using new start cursor
            if ((current_node == self.head and
                 last_node == self.head.r_child) or
                (current_node == self.head and
                 self.head.r_child is None and
                 last_node == self.head.l_child)):
                break

        return max_depth

    def balance(self):
        pass

    def _find_parent(self, new_node, old_node):
        """Helper function for insert."""
        while True:
            if new_node.val > old_node.val:
                if not old_node.r_child:
                    return old_node
                else:
                    old_node = old_node.r_child
            elif new_node.val < old_node.val:
                if not old_node.l_child:
                    return old_node
                else:
                    old_node = old_node.l_child
            else:
                print("Value already in BST.")
                return None


class BSTNode(object):
    """Create a BST Node class."""

    def __init__(self, val, parent=None, l_child=None, r_child=None):
        """Instantiate a new node object."""
        self.val = val
        self.parent = parent
        self._l_child = l_child
        self._r_child = r_child

    @property
    def l_child(self):
        return self._l_child

    @l_child.setter
    def l_child(self, node):
        self._l_child = node
        node.parent = self

    @property
    def r_child(self):
        return self._r_child

    @r_child.setter
    def r_child(self, node):
        self._r_child = node
        node.parent = self
