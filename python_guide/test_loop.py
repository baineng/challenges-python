import unittest


class LoopTest(unittest.TestCase):

    def test_loop_dict(self):
        data = {'a': 1, 'b': 2, 'c': 3}

        l = []
        for i in data:  # same as dict.keys()
            l.append(i)
        self.assertEqual(l, ['a', 'b', 'c'])

        l = []
        for i in data.values():
            l.append(i)
        self.assertEqual(l, [1, 2, 3])

        l = []
        for k, v in data.items():
            l.append(k)
            l.append(v)
        self.assertEqual(l, ['a', 1, 'b', 2, 'c', 3])

        l = []
        for i in data.items():
            l.append(i)
        self.assertEqual(l, [('a', 1), ('b', 2), ('c', 3)])

    def test_loop_list(self):
        data = ['a', 'b', 'c']

        l = []
        for i in data:
            l.append(i)
        self.assertEqual(l, ['a', 'b', 'c'])

        l = []
        for i in range(len(data)):
            l.append(i)
            l.append(data[i])
        self.assertEqual(l, [0, 'a', 1, 'b', 2, 'c'])

        l = []
        for i, v in enumerate(data):
            l.append(i)
            l.append(v)
        self.assertEqual(l, [0, 'a', 1, 'b', 2, 'c'])

    def test_zip(self):
        questions = ['name', 'quest', 'favorite color']
        answers = ['lancelot', 'the holy grail', 'blue']

        l = []
        for d in zip(questions, answers):
            l.append(d)

        self.assertEqual(l, [('name', 'lancelot'), ('quest', 'the holy grail'), ('favorite color', 'blue')])

    def test_revsered(self):
        l = []
        for i in reversed(range(1, 10)):
            l.append(i)
        self.assertEqual(l, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_sorted(self):
        data = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        l = []
        for f in sorted(set(data)):
            l.append(f)
        self.assertEqual(l, ['apple', 'banana', 'orange', 'pear'])

    def test_update_list(self):
        words = ['cat', 'window', 'defenestrate']
        for w in words[:]:
            if len(w) > 6:
                words.insert(0, w)
        self.assertEqual(words, ['defenestrate', 'cat', 'window', 'defenestrate'])


if __name__ == '__main__':
    unittest.main()