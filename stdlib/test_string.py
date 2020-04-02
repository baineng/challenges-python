import unittest
import string


class FunctionsTest(unittest.TestCase):

    def test_capwords(self):
        s = 'The quick brown box jumped over the lazy dog.'

        self.assertEqual(string.capwords(s), 'The Quick Brown Box Jumped Over The Lazy Dog.')


class TemplatesTest(unittest.TestCase):

    values = {'var': 'foo'}

    def test_template(self):
        t = string.Template("$var, $$, ${var}iable")
        self.assertEqual(t.substitute(self.values), 'foo, $, fooiable')

    def test_interpolation(self):
        t = "%(var)s, %%, %(var)siable"
        self.assertEqual(t % self.values, 'foo, %, fooiable')

    def test_format(self):
        t = "{var}, {{}}, {var}iable"
        self.assertEqual(t.format(**self.values), 'foo, {}, fooiable')

    def test_safe_substitute(self):
        t = string.Template("$var is here but $missing is not provided")
        with self.assertRaises(KeyError):
            t.substitute(self.values)
        self.assertEqual(t.safe_substitute(self.values), 'foo is here but $missing is not provided')


class AdvancedTemplatesTest(unittest.TestCase):

    class MyTemplate(string.Template):
        delimiter = '%'
        idpattern = '[a-z]+_[a-z]+'

    values = {
        'with_underscore': 'replaced',
        'notunderscored': 'not replaced'
    }

    def test_mytemplate(self):
        t = self.MyTemplate('%%, %with_underscore, %notunderscore')
        self.assertEqual(t.safe_substitute(self.values), '%, replaced, %notunderscore')


if __name__ == '__main__':
    unittest.main()