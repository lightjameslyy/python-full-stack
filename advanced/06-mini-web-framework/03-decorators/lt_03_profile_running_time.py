import time

def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        end_time = time.time()
        print("running time %f" % (end_time - start_time))
    return call_func

@set_func  # 等价于 test1 = set_func(test1)
def test1():
    print("----test1----")
    for i in range(10000):
        pass

# ret = set_func(test1)
# ret()

# test1 = set_func(test1)
test1()

test1()
