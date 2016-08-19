
class Player(object):
  def __init__(self, first_name, last_name, handle):
    self.first_name = first_name
    self.last_name = last_name
    self.handle = handle

  def print_full_name(self):
    print '%s %s' % (self.first_name, self.last_name)
