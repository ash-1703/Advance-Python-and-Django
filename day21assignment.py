from collections import Counter
class MyCounter(Counter):
  def __call__(self,Counter):
    self.Counter=Counter
    print(Counter)
        
co1 = MyCounter()
co1("intel")
