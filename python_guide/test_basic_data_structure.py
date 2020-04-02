import unittest


class ComprehensionTest(unittest.TestCase):

    def test_list(self):
        squares = list(map(lambda x: x*2, range(10)))
        self.assertEqual(squares, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

        squares = [x*2 for x in range(10)]
        self.assertEqual(squares, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

        squares = [x*2 for x in range(10) if x % 2 == 0]
        self.assertEqual(squares, [0, 4, 8, 12, 16])

    def test_set(self):
        a = {x for x in 'abracadabra' if x not in 'abc'}
        self.assertEqual(a, {'r', 'd'})

    def test_dict(self):
        a = {x: x*2 for x in (2, 4, 6)}
        self.assertEqual(a,
                         {
                             2: 4,
                             4: 8,
                             6: 12
                         })


class ListTest(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def test_append(self):
        self.data.append(4)
        self.assertEqual(self.data, [1, 2, 3, 4])

    def test_extend(self):
        newData = [3, 5, 6]
        self.data.extend(newData)
        self.assertEqual(self.data, [1, 2, 3, 3, 5, 6])

    def test_insert(self):
        self.data.insert(2, 4)
        self.assertEqual(self.data, [1, 2, 4, 3])

    def test_remove(self):
        self.data.remove(2)
        self.assertEqual(self.data, [1, 3])

    def test_pop(self):
        # pop last item
        p = self.data.pop()
        self.assertEqual(self.data, [1, 2])
        self.assertEqual(p, 3)

        # pop specific index
        h = self.data.pop(0)
        self.assertEqual(self.data, [2])
        self.assertEqual(h, 1)

    def test_clear(self):
        self.data.clear()
        self.assertEqual(self.data, [])

    def test_count(self):
        c = self.data.count(2)
        self.assertEqual(c, 1)

    def test_sort(self):
        self.data.reverse()
        self.assertEqual(self.data, [3, 2, 1])

        self.data.sort()
        self.assertEqual(self.data, [1, 2, 3])

    def test_copy(self):
        self.assertEqual(self.data.copy(), self.data[:])

    def test_stack(self):
        stack = self.data
        stack.append(5)
        stack.append(6)
        self.assertEqual(stack, [1, 2, 3, 5, 6])
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack, [1, 2])

    def test_del(self):
        del self.data[1]
        self.assertEqual(self.data, [1, 3])


class DictTest(unittest.TestCase):

    def setUp(self):
        self.data = { 'sape': 4139, 'guido': 4127, 'jack': 4098 }

    def test_basic(self):
        self.assertEqual(self.data['guido'], 4127)

        self.assertEqual(list(self.data.keys()), ['sape', 'guido', 'jack'])

        # different ways to assign a dict
        del self.data['guido']
        self.assertEqual(self.data, { 'sape': 4139, 'jack': 4098 })
        self.assertEqual(self.data, dict([('sape', 4139), ('jack', 4098)]))
        self.assertEqual(self.data, dict(sape=4139, jack=4098))


class TupleTest(unittest.TestCase):

    def test_assign(self):
        empty = ()
        self.assertEqual(empty, ())

        singleton = 'hello',
        self.assertEqual(singleton, ('hello',))

        t = 1, 2, 3
        self.assertEqual(t, (1, 2, 3))
        self.assertEqual(t[1], 2)


class SetTest(unittest.TestCase):

    def test_assign(self):
        d1 = set()  # instead of {}, {} is for dict

        d1.add('a')
        d1.add('b')
        self.assertEqual(d1, {'a', 'b'})

        d2 = {'a', 'b', 'c', 'd', 'e', 'f'}

        self.assertEqual(d2 - d1, {'c', 'd', 'e', 'f'})  # in d2, but not d1
        self.assertEqual(d2 | d1, {'a', 'b', 'c', 'd', 'e', 'f'})  # in either d2 or d1
        self.assertEqual(d2 & d1, {'a', 'b'})  # in both d2 and d1
        self.assertEqual(d2 ^ d1, {'c', 'd', 'e', 'f'})  # in d2 or d1, but not both


if __name__ == '__main__':
    unittest.main()