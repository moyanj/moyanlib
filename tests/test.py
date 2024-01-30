import unittest
import moyanlib
from moyanlib.cache import Cache
import time


# 创建一个测试类，继承自 unittest.TestCase
class TestCase(unittest.TestCase):
    # 在每个测试方法运行之前执行的操作
    def setUp(self):
        # 可以在这里进行一些初始化操作
        pass

    # 在每个测试方法运行之后执行的操作
    def tearDown(self):
        # 可以在这里进行一些清理操作
        pass

    # 测试方法需要以 "test_" 开头
    def test_genVerifiCode(self):
        result = moyanlib.generate_verifi_code()
        self.assertEqual(type(result).__name__, "str")  # 使用断言来判断结果是否符合预期
        self.assertEqual(len(result), 4)

    def test_getDeviceID(self):
        result = moyanlib.getDeviceID()
        self.assertEqual(type(result).__name__, "str")

    def test_cache1(self):
        cache = Cache()
        cache.set("114514", 4665, 2)
        result = cache.get("114514")
        self.assertEqual(result, 4665)
        cache.delete_all()

    def test_cache2(self):
        cache = Cache()
        cache.set("15", "sb", 0.15)
        time.sleep(0.18)
        result = cache.get("15")
        self.assertEqual(result, None)
        cache.delete_all()


# 运行测试
if __name__ == "__main__":
    unittest.main()
