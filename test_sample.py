import pytest
def inc(x):
    return x+1
def good_answer():
    assert inc(3) == 4
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

@pytest.fixture
def cmdopt():
    return "type1"

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    if cmdopt == "type2":
        print('second')
    assert 1

def hoi():
  assert 1
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert "el" in x

def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 1

@pytest.fixture
def coolargument():
    return "hello"

def testthis(coolargument):
    print(coolargument)
    assert 1

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
