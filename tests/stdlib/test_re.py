import unittest
import re


class FindingPatternsTest(unittest.TestCase):

    pattern = 'this'
    text = 'Does this text match the pattern?'

    def _asserts(self, match):
        s = match.start()
        e = match.end()
        self.assertEqual(match.re.pattern, self.pattern)
        self.assertEqual(match.string, self.text)
        self.assertEqual(s, 5)
        self.assertEqual(e, 9)
        self.assertEqual(self.text[s:e], self.pattern)

    def test_search(self):
        match = re.search(self.pattern, self.text)
        self._asserts(match)

    def test_search_with_compile(self):
        regex = re.compile(self.pattern)
        match = regex.search(self.text)
        self._asserts(match)

    def test_match(self):
        match = re.match(self.pattern, self.text)
        self.assertIsNone(match)
        match = re.match('Do', self.text)
        self.assertIsNotNone(match)

    def test_fullmatch(self):
        match = re.fullmatch(self.pattern, self.text)
        self.assertIsNone(match)
        match = re.fullmatch(r'Do.*pattern\?', self.text)
        self.assertIsNotNone(match)

    def test_findall(self):
        matches = re.findall(r'\b\w*th\w*\b', self.text)
        self.assertEqual(matches, ['this', 'the'])

class GroupTest(unittest.TestCase):

    text = 'This is some text -- with punctuation.'

    def test_groups(self):
        match = re.search(r'^(\w+)', self.text)
        self.assertEqual(match.groups(), ('This',))

        match = re.search(r'(\bt\w+)\W+(\w+)', self.text)
        self.assertEqual(match.groups(), ('text', 'with'))

    def test_group(self):
        match = re.search(r'(\bt\w+)\W+(\w+)', self.text)
        self.assertEqual(match.group(0), 'text -- with')
        self.assertEqual(match.group(1), 'text')
        self.assertEqual(match.group(2), 'with')

    def test_named_groups(self):
        match = re.search(r'(?P<first>\bi\w+)\s+(?P<second>\w+)', self.text)
        self.assertEqual(match.groupdict(), { 'first': 'is', 'second': 'some' })

        self.assertEqual(match.group(0), 'is some')
        self.assertEqual(match.group(1), 'is')
        self.assertEqual(match.group('first'), 'is')
        self.assertEqual(match.groups(), ('is', 'some'))


class FlagTest(unittest.TestCase):

    def test_case_insensitive(self):
        text = 'This is some text -- with punctuation.'
        pattern = r'\bT\w+'

        self.assertEqual(re.findall(pattern, text), ['This'])
        self.assertEqual(re.findall(pattern, text, re.IGNORECASE), ['This', 'text'])

    def test_multiple_lines(self):
        text = 'This is some text -- with punctuation.\nA second line.'
        pattern = r'(^\w+)|(\w+\S*$)'

        self.assertEqual(re.findall(pattern, text), [('This', ''), ('', 'line.')])
        self.assertEqual(
            re.findall(pattern, text, re.MULTILINE),
            [('This', ''), ('', 'punctuation.'), ('A', ''), ('', 'line.')]
        )

    def test_unicode(self):
        text = u'Français złoty Österreich'
        pattern = r'\w+'

        self.assertEqual(re.findall(pattern, text, re.ASCII), ['Fran', 'ais', 'z', 'oty', 'sterreich'])
        self.assertEqual(re.findall(pattern, text), ['Français', 'złoty', 'Österreich'])

    def test_embeded_flag(self):
        text = 'This is some text -- with punctuation.'
        pattern = r'(?i)\bT\w+'

        self.assertEqual(re.findall(pattern, text), ['This', 'text'])


if __name__ == '__main__':
    unittest.main()
