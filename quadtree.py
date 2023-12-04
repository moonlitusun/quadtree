class QuadTree:
  def __init__(self, bounds, max_objects=None, max_levels=None, level=None):
    self.max_objects = max_objects or 10
    self.max_levels = max_levels or 4

    self.bounds = bounds
    self.level = level or 0

    self.objects = []
    self.quadrants = []