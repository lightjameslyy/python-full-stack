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

    # def eat(self):
    #     print("eat")
    #
    # def drink(self):
    #     print("drink")
    #
    # def run(self):
    #     print("run")
    #
    # def sleep(self):
    #     print("sleep")

    def bark(self):
        print("wang wang wang...")

wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
