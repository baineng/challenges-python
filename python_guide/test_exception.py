import unittest

class ErrorA(Exception):
    pass


class ErrorB(ErrorA):
    pass


class ErrorC(ErrorB):
    pass


class ExceptionTest(unittest.TestCase):

    def test_try_catch(self):

        d = False
        try:
            raise ErrorA()
        except:
            d = True
        self.assertEqual(d, True)

        d = False
        try:
            raise ErrorC()
        except ErrorC as ex:
            d = True
        self.assertEqual(d, True)

        d = False
        try:
            raise ErrorC()
        except ErrorB:
            d = True
        self.assertEqual(d, True)

        d = False
        try:
            pass
        except ErrorA:
            pass
        else:
            d = True
        self.assertEqual(d, True)


        d = False
        try:
            raise ErrorC()
        except ErrorA:
            pass
        finally:
            d = True
        self.assertEqual(d, True)


if __name__ == '__main__':
    unittest.main()
