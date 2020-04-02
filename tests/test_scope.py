import unittest


class ScopeTest(unittest.TestCase):

    def test_local(self):
        """local scope variables changes will not affect the parent ones"""

        data = 'default'

        def func():
            data = 'local'

        func()
        self.assertEqual(data, 'default')

    def test_nonlocal(self):
        """nonlocal variables changes will affect the parent ones, not global ones"""

        data = 'default'

        def func():
            nonlocal data
            data = 'nonlocal'

        func()
        self.assertEqual(data, 'nonlocal')

    def test_global(self):
        """only global declares can affect global variables"""

        data = 'default'

        def func():
            global data
            data = 'global'
        func()
        self.assertEqual(data, 'default')

        def func2():
            global data
            self.assertEqual(data, 'global')
        func2()


if __name__ == '__main__':
    unittest.main()