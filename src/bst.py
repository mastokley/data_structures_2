from collections import deque


class BST(object):
    """Creates a BST class."""

    def __init__(self, node=None):
        """Instantiate a new binary sorted tree object."""
        self.head = node
        self._size = 0 if self.head is None else self._size == 1

    def insert(self, val):
        """Insert a node into binary search tree."""
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
        """Return true if value in tree."""
        if not self.head:
            return False
        dummy = BSTNode(val)
        return not self._find_parent(dummy, self.head)

    def size(self):
        """Return count of all nodes in tree."""
        return self._size

    def depth(self, start='potato'):
        """Return number of levels in tree."""
        starting_node = self.head if start == 'potato' else start
        if starting_node is None:
            return 0
        last_node = None
        current_depth = 1
        starting_node.parent = None
        current_node = starting_node
        max_depth = 1
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
            # if you can't move left or right, move up
            elif (current_node.parent is not None and
                  current_node != start):
                current_depth -= 1
                last_node = current_node
                current_node = current_node.parent
            if current_depth > max_depth:
                max_depth = current_depth
            # if done, exit
            if ((current_node == starting_node and
                 last_node == starting_node.r_child) or
                (current_node == starting_node and
                 starting_node.r_child is None and
                 last_node == starting_node.l_child)):
                break
        return max_depth

    def balance(self):
        """Return depth of subtree on left less depth of subtree on right."""
        if self.depth() > 1:
            return self.depth(self.head.l_child) - self.depth(self.head.r_child)
        else:
            return 0

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

    def traverse_in(self):
        """Traverse tree 'in order': left, self, right."""
        def gen_in(node):
            if node is None:
                return
            try:
                for item in gen_in(node.l_child):
                    yield item
            except AttributeError:
                pass
            yield node.val
            try:
                for item in gen_in(node.r_child):
                    yield item
            except AttributeError:
                pass
        return gen_in(self.head)

    def traverse_pre(self):
        """Traverse tree in 'pre-order': self, left, right."""
        def gen_pre(node):
            if node is None:
                return
            yield node.val
            try:
                for item in gen_pre(node.l_child):
                    yield item
            except AttributeError:
                pass
            try:
                for item in gen_pre(node.r_child):
                    yield item
            except AttributeError:
                pass
        return gen_pre(self.head)

    def traverse_post(self):
        """Traverse tree in 'post-order': left, right, self."""
        def gen_post(node):
            if node is None:
                return
            try:
                for item in gen_post(node.l_child):
                    yield item
            except AttributeError:
                pass
            try:
                for item in gen_post(node.r_child):
                    yield item
            except AttributeError:
                pass
            yield node.val
        return gen_post(self.head)

    def traverse_breadth(self):
        """Traverse tree from left to right, by level."""
        q = deque()
        q.append(self.head)
        while q:
            catch = q.popleft()
            try:
                yield catch.val
            except AttributeError:
                pass
            try:
                q.append(catch.l_child)
            except AttributeError:
                pass
            try:
                q.append(catch.r_child)
            except AttributeError:
                pass


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
