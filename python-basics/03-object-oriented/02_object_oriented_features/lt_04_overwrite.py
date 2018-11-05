class Animal:

    def eat(self):
        print("eat...")

    def drink(self):
        print("drink...")

    def run(self):
        print("run...")

    def sleep(self):
        print("sleep...")


class Dog(Animal):

    def bark(self):
        print("wang wang wang...")


class XiaoTianQuan(Dog):

    def fly(self):
        print("i can fly...")

    def bark(self):
        print("bark like a god")


xtq = XiaoTianQuan()
xtq.bark()
