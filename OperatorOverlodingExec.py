class OrderSet:
   def __init__(self,iterable):
      self.data=set(iterable)
   def __repr__(self):
      return 'OrderSet(%r)' % list(self.data)

   def __and__(self, rhs): #位与
      return self.data & rhs.data

   def __or__(self, rhs): #位或
      return self.data | rhs.data

   def __xor__(self, rhs): #位异或
      return self.data ^ rhs.data

   def __contains__(self, item):
      for x in self.data:
         if x==item:
            return True
      return False

   def __eq__(self, rhs):
      return self.data==rhs.data

   def __ne__(self,rhs):
      return self.data!=rhs.data

s1=OrderSet([1,2,3,4])
s2=OrderSet([3,4,5])
print(s1&s2)    #OrderSet([3,4])
print(s1|s2)    #OrderSet([1,2,3,4,5])
print(s1^s2)    #OrderSet([1,2,3,4,5])
if OrderSet([1,2,3])!=OrderSet([1,2,3,4]):
    print('不相等')
if s2==OrderSet([3,4,5]):
    print('s2和OrderSet(3,4,5)相等')
if 2 in s1:
    print('2 in s1')
