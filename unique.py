class UniqueList:
  def __init__(self,elem_class):
    self.list = []
    self.elem_class = elem_class
  
  def __len__(self):
    return len(self.list)
  
  def __iter__(self):
    return iter(self.list)

  def __getitem__(self,p):
    return self.list[p]

  def indexValid(self,i):
    return i >= 0 and i < len(self.list)
  
  def add(self,elem):
    if self.search(elem) == -1 :
      self.list.append(elem)

  def search(self,elem):
    self.type_verify(elem)
    try:
      return self.list.index(elem)
    except ValueError:
      return -1 

  def type_verify(self,elem):
    if type(elem)!=self.elem_class:
      raise TypeError("Invalida Type")
  
  def order(self,key = None):
    self.list.sort(key = key)



'''
Magic Methods
'''