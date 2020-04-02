import unittest
import collections


class ChainMapTest(unittest.TestCase):

    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    def test_accessing(self):

        m = collections.ChainMap(self.a, self.b)

        self.assertEqual(m['a'], 'A')
        self.assertEqual(m['b'], 'B')
        self.assertEqual(m['c'], 'C')

        self.assertEqual(['a', 'b', 'c'], sorted(list(m.keys())))
        self.assertEqual(['A', 'B', 'C'], sorted(list(m.values())))

        self.assertFalse('d' in m)


    def test_reordering(self):

        m = collections.ChainMap(self.a, self.b)

        self.assertEqual(m['c'], 'C')

        m.maps = list(reversed(m.maps))
        self.assertEqual(m['c'], 'D')


    def test_updating(self):

        m = collections.ChainMap(self.a, self.b)

        self.assertEqual('A', m['a'])
        self.a['a'] = 'A2'
        self.assertEqual('A2', m['a'])

        m['c'] = 'C2'
        self.assertEqual('C2', self.a['c'])

        m2 = m.new_child()
        m2['c'] = 'C3'
        self.assertEqual('C2', self.a['c'])


if __name__ == '__main__':
    unittest.main()