class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'
    
obj = MyClass()
print(obj.method()) # ('instance method called', <__main__.MyClass object at 0x7f7f7f7f7f7f>)

print(MyClass.method(obj))

print(obj.class_method()) # ('class method called', <class '__main__.MyClass'>)

print(obj.static_method()) # static method called