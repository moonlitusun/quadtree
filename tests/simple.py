import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from quadtree import QuadTree

my_tree = QuadTree({"x": 0, "y": 0, "width": 640, "height": 480}, 4)

print(my_tree.max_levels)
