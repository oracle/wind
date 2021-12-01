## Copyright © 2021, Oracle and/or its affiliates. 
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

import ast

from robot.api import Token


class TagCollector(ast.NodeVisitor):
    """
    Collects all tags available in the provided AST of a robot test file.

    Attributes:
        tags: a list of the tags found in the test.
    """

    def __init__(self):
        super().__init__()
        self.tags = []

    # pylint: disable=invalid-name
    def visit_File(self, node):
        self.generic_visit(node)

    # pylint: disable=invalid-name
    def visit_ForceTags(self, node):
        self.tags.extend(node.get_values(Token.ARGUMENT))

    # pylint: disable=invalid-name
    def visit_Tags(self, node):
        self.tags.extend(node.get_values(Token.ARGUMENT))

    # pylint: disable=invalid-name
    def visit_DefaultTags(self, node):
        self.tags.extend(node.get_values(Token.ARGUMENT))
