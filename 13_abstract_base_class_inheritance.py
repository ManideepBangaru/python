class Base:
    def foo(self):
        raise NotImplementedError()
    
    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'
    
    # Oh no, we forgot to override bar()...
    # def bar(self):
    #     return 'bar() called'

b = Base()
b.foo()

c = Concrete()
c.foo()
c.bar()

# Here’s an updated implementation using an Abstract Base Class defined with the abc module:
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

assert issubclass(Concrete, Base)

c = Concrete()