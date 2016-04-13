from collections import deque
import random
import io


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
        # By returning zero, we can use this to balance one-child trees
        if starting_node is None:
            return 0
        last_node = None
        current_depth = 1
        saved = starting_node.parent
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
        starting_node.parent = saved
        return max_depth

    def balance(self):
        """Return depth of subtree on left less depth of subtree on right."""
        if self.depth() > 1:
            return (self.depth(self.head.l_child) -
                    self.depth(self.head.r_child))
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

    def _find_node(self, val):
        """Helper function to return a node based on a value"""
        try:
            current_node = self.head
            while True:
                if current_node.val == val:
                    return current_node
                elif val > current_node.val:
                    current_node = current_node.r_child
                else:
                    current_node = current_node.l_child
        except AttributeError:
            raise ValueError("value not in list")

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

    def delete_node(self, val):
        """Find and delete nodes - error handling for find in helper."""
        node = self._find_node(val)
        node_balance = self.depth(node.l_child) - self.depth(node.r_child)
        if node_balance > 0:
            leaf = node.l_child
            target_child = 'r_child'
        else:
            leaf = node.r_child
            target_child = 'l_child'

        try:
            while getattr(leaf, target_child):
                child = getattr(leaf, target_child)
                leaf = child
        except AttributeError:
            pass
        try:
            node.val = leaf.val
            if leaf.parent.l_child == leaf:
                leaf.parent.l_child = None
            else:
                leaf.parent.r_child = None
        except AttributeError:
            self.head = None

    def _rebalance(self, node):
        """Rotate local nodes and move up."""
        balance_score = self.some_balance_score_determiner(node)

        # option 1

        # if node is None:
        #     return
        # elif bad_balance_score :
        #     < do the local rotation >
        #     self._rebalance(node.parent)

        # option 2

        # if bad_balance_score:
        #     < do the local rotation >
        #     try:
        #         self._rebalance(node.parent)
        #     except AttributeError:
        #         < this means I\'m finished >

    def write_graph(self, node=None):
        file = io.open('graph.gv', 'w')
        file.write(self.get_dot(node))
        file.close()
        print("graph.gv updated")

    def get_dot(self, node=None):
        """
        Return tree with root 'self' by default as dot graph for visualization.
        """
        if (node is None) and (self.head is not None):
            node = self.head
        dots = "\t{};\n{}\n".format(node.val, "\n".join(self._get_dot(node)))
        return "digraph bst {{{}}}".format("" if node is None else dots)

    def _get_dot(self, node):
        """Recurisvely prepare a dot graph entry for this node."""
        if node.l_child is not None:
            yield "\t{} -> {};".format(node.val, node.l_child.val)
            for entry in self._get_dot(node.l_child):
                yield entry
        elif node.r_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull{} [shape=point];".format(r)
            yield "\t{} -> null{};".format(node.val, r)
        if node.r_child is not None:
            yield "\t{} -> {};".format(node.val, node.r_child.val)
            for entry in self._get_dot(node.r_child):
                yield entry
        elif node.l_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull{} [shape=point];".format(r)
            yield "\t{} -> null{};".format(node.val, r)


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
        if node is not None:
            node.parent = self

    @property
    def r_child(self):
        return self._r_child

    @r_child.setter
    def r_child(self, node):
        self._r_child = node
        if node is not None:
            node.parent = self

if __name__ == '__main__':
    bob = BST()
    bob.insert(10)
    bob.insert(15)
    bob.insert(5)
    bob.insert(20)
    bob.insert(13)
    bob.insert(12)
    bob.insert(11)
    bob.insert(12.5)
    bob.insert(2)
    bob.insert(6)
    bob.insert(5.5)
    bob.insert(1)
    bob.write_graph()
