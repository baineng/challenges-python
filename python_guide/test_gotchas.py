# -*- coding: utf-8 -*-
"""
Test some common gotchas
ref: https://docs.python-guide.org/writing/gotchas/
"""


class TestMutableArguments:
    """
    A new list is created once when the function is defined,
    and the same list is used in each successive call.
    """
    def append_to(element, to=[]):
        to.append(element)
        return to

    def immutable_append_to(element, to=None):
        if to is None:
            to = []
            to.append(element)
        return to

    def test_mutable_arguments(self):
        to1 = TestMutableArguments.append_to('ele1')
        assert to1 == ['ele1']

        to2 = TestMutableArguments.append_to('ele2')
        assert to2 == ['ele1', 'ele2']  # this should be expected as ['ele2']

    def test_immutable_append_to(self):
        to1 = TestMutableArguments.immutable_append_to('ele1')
        assert to1 == ['ele1']

        to2 = TestMutableArguments.immutable_append_to('ele2')
        assert to2 == ['ele2']


class TestLateBindingClosures:
    """
    Python’s closures are late binding.
    This means that the values of variables used in closures \
    are looked up at the time the inner function is called.

    This gotchas is not only for `lambdas` but the `def` as well.

    The most general solution is to use `default arguments` of functions,
    Alternatively, you can use the functools.partial function
    """
    def create_multipliers():
        return [lambda x: i * x for i in range(5)]

    def create_multipliers_def():
        multipliers = []
        for i in range(5):

            def multiplier(x):
                return i * x

            multipliers.append(multiplier)
        return multipliers

    def test_create_multipliers(self):
        result = [
            func(2) for func in TestLateBindingClosures.create_multipliers()
        ]

        # we expect the result should be [0, 2, 4, 6, 8]
        # but it is:
        assert result == [8, 8, 8, 8, 8]

        def_result = [
            func(2)
            for func in TestLateBindingClosures.create_multipliers_def()
        ]

        assert def_result == [8, 8, 8, 8, 8]

    def create_multipliers_by_default_argument():
        return [lambda x, i=i: i * x for i in range(5)]

    def test_create_multipliers_by_default_argument(self):
        result = [
            func(2) for func in
            TestLateBindingClosures.create_multipliers_by_default_argument()
        ]

        assert result == [0, 2, 4, 6, 8]

    def create_multipliers_by_partial():
        from functools import partial
        from operator import mul

        return [partial(mul, i) for i in range(5)]

    def test_create_multipliers_by_partial(self):
        result = [
            func(2) for func in
            TestLateBindingClosures.create_multipliers_by_partial()
        ]

        assert result == [0, 2, 4, 6, 8]
