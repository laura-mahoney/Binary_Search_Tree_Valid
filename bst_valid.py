"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False
"""

class Node(object):

    def __init__(self, data, left=None, right=None):
        
        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):

        def _ok(n, lt, gt):
            """ check this node and recurse to children"""

            if n is None:
                #base case: this is not a node 
                return True

            if lt is not None and n.data > lt:
                #base case: left node is greater than current node
                return False

            if gt is not None and n.data < gt:
                #base base: right node is less than current node
                return False 

            if not _ok(n.left, n.data, gt):
                #passing the left node in as the new node, recursively checking all lefts
                #all data on the left has to be less than n.data and greater than successive nodes
                return False 

            if not _ok(n.right, lt, n.data):
                #pass the right node in as the new node, recursively checking all rights
                #all data on the left has to be less than n.data
                return False



            return True 

        return _ok(self, None, None)


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; THAT'S VALID!\n"


