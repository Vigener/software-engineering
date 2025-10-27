class RingBuffer:
  def __init__(self, n: int):
    self.__n = n
    self.__n1 = n + 1
    self.__buf = [None] * self.__n1
    self.__hd = 0
    self.__tl = 0
  def put_elem(self, x: int):
    if (self.is_full()):
      raise Exception
    self.__buf[self.__tl] = x
    self.__tl += 1
    if (self.__tl >= self.__n1):
      self.__tl = 0
  def get_elem(self):
    if (self.is_empty()):
      raise Exception
    r = self.__buf[self.__hd]
    self.__hd += 1
    if (self.__hd >= self.__n1):
      self.__hd = 0
    return r
  def bufsize(self):
    return self.__n
  def num_of_elems(self):
    if (self.__tl >= self.__hd):
      return self.__tl - self.__hd
    else:
      return self.__tl + self.__n1 - self.__hd
  def clear(self):
    self.__hd = 0
    self.__tl = 0
  def is_empty(self):
    return (self.__hd == self.__tl)
  def is_full(self):
    next_tl = self.__tl + 1
    if (next_tl >= self.__n1):
      next_tl = 0
    return (self.__hd == next_tl)
  def sum(self):
    s = 0
    i = self.__hd
    while (i != self.__tl):
      s += self.__buf[i]
      i += 1
      if (i >= self.__n1):
        i = 0
    return s