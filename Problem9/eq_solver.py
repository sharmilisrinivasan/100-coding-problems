"""
File name: eq_solver.py
Author: SharmiliSrinivasan
Date created: 03/02/2018
Date last modified: 03/04/2018
Last modified by: SharmiliSrinivasan
Python Version: 2.7
"""

"""
Invocation:
python eq_solver.py <complete path to input json file>
eg: python eq_solver.py ~/Desktop/sample.json

Script that reads json file given as input and prints the following:
1. The string representation of given equation
2. The string representation of solvable equation:
   i.e. variable "x" on left and the expression to solve on the right
3. Solution to the above solvable equation, i.e. value of x.

Assumptions/Expectations:
1. There is only one "x" on the "left" side of the equation.
2. The json is valid and each component has "lhs","rhs" and "op" fields
(no missing labels).
3. The equation is solvable. i.e. If we solve for x, we get an integer as
output. Else, the output will be rounded.
4. All labels in json (operator or keys) are case-sensitive and are expected
to be in lower case.
5. If on solving for equation, divide-by-zero error is encountered, the code
throws an error.

Attributes:
    LABEL_LHS (str): Constant- Key used to represent LHS in the given JSON
    LABEL_OP (str): Constant- Key used to represent operator in the given JSON
    LABEL_RHS (str): Constant- Key used to represent RHS in the given JSON
    OP_EQUAL (str): Constant- Key used to represent equality operator in the
                    given JSON
    X_CONSTANT (str): Constant- Key used to represent variable "x" in the
                      given JSON
"""
import json
import sys

LABEL_LHS = "lhs"
LABEL_OP = "op"
LABEL_RHS = "rhs"
OP_EQUAL = "equal"
X_CONSTANT = "x"


class SIDES(object):
    """Class of constants to denote left and right sides in various contexts
    """

    LEFT_SIDE, RIGHT_SIDE = range(2)


class OpTreeNode(object):
    """Node representation of an element in binary tree along with
    related methods

    Attributes:
        left_node (opTreeNode): Instance variable- Left child of the node
        OP_SYMB_MAP (dict): Class Variable- Mapping between operator strings
                            and their symbols
        right_node (opTreeNode): Instance variable- Right child of the node
        val (str): Instance variable- Value in the node
    """

    OP_SYMB_MAP = {"add": "+",
                   "subtract": "-",
                   "multiply": "*",
                   "divide": "/",
                   "equal": "="}

    def __init__(self, root_val_=None, left_=None, right_=None):
        """Built-in function to initialise value, left and right children on
        creating current node of the tree, if given (Default values: None)

        Args:
            root_val_ (None, str): value in the node
            left_ (None, opTreeNode): left child of the node
            right_ (None, opTreeNode): right child of the node
        """
        self.val = root_val_
        self.left_node = left_
        self.right_node = right_

    def _val_is_operator(self):
        """Checks if the value in the node is an operator

        Returns:
            Bool: True, if value in the node is an operator
                  False, otherwise.
        """
        return str(self.val) in self.__class__.OP_SYMB_MAP.keys()

    def is_leaf_node(self):
        """Checks if node is leaf or not

        Returns:
            Bool: True, if node is a leaf node (has neither of the children)
                  False, otherwise.
        """
        return not (self.left_node or self.right_node)

    def has_x(self):
        """Checks value in the node or any of the children has variable "x"

        Returns:
            Bool: True, if current node or any of the children has "x" as
                  node value
                  False, otherwise.
        """
        return self.val == "x" or \
               (self.left_node and self.left_node.has_x()) or \
               (self.right_node and self.right_node.has_x())

    def _are_braces_req(self, side_):
        """Checks if string representation of node requires braces when printing
        left or right children

        Args:
            side_ (SIDES): Side of the child for which braces requirement is
                           checked

        Returns:
            Bool: True, if braces are required
                  False, otherwise.
        """
        to_return = (self._val_is_operator()
                     and self.val != OP_EQUAL)
        if side_ == SIDES.LEFT_SIDE:
            return (to_return and
                    self.left_node and
                    not self.left_node.is_leaf_node())
        return (to_return and
                self.right_node and
                not self.right_node.is_leaf_node())

    def __repr__(self):
        """Built-in function to give string representation of the node

        Returns:
            str: String representation of node
        """
        to_return = ""

        # Constructing left child
        braces_req = self._are_braces_req(SIDES.LEFT_SIDE)
        if braces_req:
            to_return += "("
        if self.left_node:
            to_return += str(self.left_node)
        if braces_req:
            to_return += ")"

        # Constructing value of current node
        to_return += str(
            self.__class__.OP_SYMB_MAP[self.val]
            if self._val_is_operator() else self.val)

        # Constructing right child
        braces_req = self._are_braces_req(SIDES.RIGHT_SIDE)
        if braces_req:
            to_return += "("
        if self.right_node:
            to_return += str(self.right_node)
        if braces_req:
            to_return += ")"

        # Final return
        return to_return


class EqSolver(object):
    """Class to restructure and solve the given equation

    Attributes:
        eq_side (opTreeNode): Instance variable- Left side of equality
                                               - Representing equation side
        OP_PAIRS (dict): Class Variable- The complementary pair of each operator
                                       - The operator to which it changes when
                                         taken to other side of equality.
        SAFE_OPS (list): Class Variable- Operators that are insensitive to
                                         order of operands
        sol_side (opTreeNode): Instance variable- Right side of equality
                                                - Representing solution side
        UNSAFE_OPS (list): Class Variable- Operators that are sensitive to
                                           order of operands
    """

    OP_PAIRS = {"add": "subtract",
                "subtract": "add",
                "multiply": "divide",
                "divide": "multiply"
                }
    SAFE_OPS = ["add", "multiply"]
    UNSAFE_OPS = ["subtract", "divide"]

    def __init__(self, parent_tree_):
        """Built-in function to initialise equation and solution side from root
        node of the tree representation of the given equation

        Args:
            parent_tree_ (opTreeNode): Root node of the tree representation of
            the given equation
        """
        self.eq_side = parent_tree_.left_node
        self.sol_side = parent_tree_.right_node

    def _get_op_pair(self, operator_):
        """Returns complementary pair of given operator

        Args:
            operator_ (str): Operator for which complement is required

        Returns:
            str: Complementary operator
        """
        return self.__class__.OP_PAIRS[operator_]

    def _get_add_side_n_op(self, operator_, x_side_):
        """Returns operator to be used and side of operator to which current
        value to be added in other side of equation

        Args:
            operator_ (str): current operator on equation side
            x_side_ (SIDES): Side of child which has variable "x"

        Returns:
            tuple: (side of child, operator) on solution side
        """
        if ((operator_ in self.__class__.SAFE_OPS) or
                (operator_ in self.__class__.UNSAFE_OPS and
                 x_side_ == SIDES.LEFT_SIDE)):
            return SIDES.RIGHT_SIDE, self._get_op_pair(operator_)
        return SIDES.LEFT_SIDE, operator_

    def _update_sol_side(self, dir_, update_val_, update_op_):
        """Updates solution side with given operator and value.
        Value is added to the given side of the given operator
        and already existing solution node is added to the other side.

        Args:
            dir_ (SIDES): Side of child of given value in solution side
            update_val_ (str): Value to be added
            update_op_ (str): Operator to be used when value added in solution
                              side
        """
        if dir_ == SIDES.LEFT_SIDE:
            self.sol_side = OpTreeNode(update_op_, update_val_, self.sol_side)
        else:
            self.sol_side = OpTreeNode(update_op_, self.sol_side, update_val_)

    def solve(self):
        """Solves the given equation by moving all elements from equation side
        to solution side , expect for the variable "x"

        Returns:
            self (eq_solver): Returns reference to self, so that this method can
                              be chained on call.
        """
        while self.eq_side:
            op = self.eq_side.val
            if op == X_CONSTANT:
                break
            if self.eq_side.left_node.has_x():
                join_val = self.eq_side.right_node
                self.eq_side = self.eq_side.left_node
                x_side = SIDES.LEFT_SIDE
            else:
                join_val = self.eq_side.left_node
                self.eq_side = self.eq_side.right_node
                x_side = SIDES.RIGHT_SIDE
            dir_, op = self._get_add_side_n_op(op, x_side)
            self._update_sol_side(dir_, join_val, op)
        return self

    def get_x_val(self):
        """Solve the solution side for value of x
        Note: The output is an integer (Assumption: The equation is solvable)

        Returns:
            int: Integer value of solution side of the eqution
        """
        return eval(str(self.sol_side))

    def __repr__(self):
        """Built-in function to give string representation of the equation

        Returns:
            str: Representation of the equation
        """
        return str(OpTreeNode(OP_EQUAL, self.eq_side, self.sol_side))


def create_tree(data_):
    """Recursively creates equation tree from given dictionary

    Args:
        data_ (dict): Dictionary form of equation to be solved

    Returns:
        opTreeNode: Root node of equation tree constructed from given dictionary
    """
    if isinstance(data_, dict):
        return OpTreeNode(data_[LABEL_OP],
                          create_tree(data_[LABEL_LHS]),
                          create_tree(data_[LABEL_RHS]))
    return OpTreeNode(data_)


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print "Full path of json file is expected as input"
            exit(1)
        json_file = sys.argv[1]
        data = json.load(open(json_file, "r"))
        eq_given = create_tree(data)

        # Outputs
        print "Given expression is: {}".format(eq_given)
        eq_solved = EqSolver(eq_given).solve()
        print "Solved expression is: {}".format(eq_solved)
        print "Value of X is: {}".format(eq_solved.get_x_val())
    except Exception, exception_:
        print "Encountered an error on execution: {}".format(exception_)
