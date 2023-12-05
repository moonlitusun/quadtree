import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from quadtree import QuadTree
from tests.common import rand_min_max

my_tree = QuadTree({"x": 0, "y": 0, "width": 640, "height": 480}, 4)

my_cursor = {
    "x": 0,
    "y": 0,
    "width": 28,
    "height": 28,
}


def handler_add_object(rect=None):
    if not rect:
        rect = {
            "x": rand_min_max(0, my_tree.bounds["width"] - 32),
            "y": rand_min_max(0, my_tree.bounds["height"] - 32),
            "width": rand_min_max(4, 32, True),
            "height": rand_min_max(4, 32, True),
        }

    my_tree.insert(rect)


handler_add_object()
handler_add_object()
handler_add_object()
handler_add_object()
handler_add_object()

list = my_tree.retrieve(
    {"x": 442.67247944659135, "y": 11.251336922147196, "width": 6, "height": 10}
)

print(list)
