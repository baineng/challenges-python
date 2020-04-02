def without_args(func):
    return lambda: 'd1_' + func()


@without_args
def f1():
    return 'f1'


def with_args(func):
    return lambda *args: 'd2_' + ','.join(args) + '_' + func()


@with_args
def f2():
    return 'f2'


@with_args
@without_args
def f3():
    return 'f3'


def test_decorator():
    # simple decorator test
    assert f1() == 'd1_f1'

    import flask
    # decorator with args
    assert f2('x', 'y') == 'd2_x,y_f2'

    # multiple decorators
    assert f3('x', 'y') == 'd2_x,y_d1_f3'
