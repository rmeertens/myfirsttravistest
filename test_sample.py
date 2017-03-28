import pytest
def inc(x):
    return x+1
def good_answer():
    assert inc(3) == 4
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0


def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    if cmdopt == "type2":
        print('second')
    assert 0

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 0

@pytest.fixture
def coolargument():
    return "hello"

def testthis(coolargument):
    print(coolargument)
    assert 0

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()