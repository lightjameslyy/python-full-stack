def set_func(func):
    def call_func():
        print("---权限验证1---")
        print("---权限验证2---")
        func()
    return call_func

@set_func  # 等价于 test1 = set_func(test1)
def test1():
    print("----test1----")

# ret = set_func(test1)
# ret()

# test1 = set_func(test1)
test1()

test1()
