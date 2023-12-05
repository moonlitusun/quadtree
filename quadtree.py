class QuadTree:
  def __init__(self, bounds, max_objects=None, max_levels=None, level=None):
    self.max_objects = max_objects or 10
    self.max_levels = max_levels or 4

    self.bounds = bounds
    self.level = level or 0

    self.objects = []
    self.quadrants = []

  def split(self):
    return
  
  def insert(self, p_rect):
    indexes = []
    i = 0

    if len(self.quadrants):
      print('aaa')
      return
    
    self.objects.append(p_rect)

    print(len(self.objects), self.max_objects, len(self.objects) > self.max_objects)
    if len(self.objects) > self.max_objects and self.level < self.max_levels:
      if not len(self.quadrants):
        self.split()
        print('split')
    