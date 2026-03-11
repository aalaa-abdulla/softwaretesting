from myenv.day1.main import add
from myenv.day1.main import mins
def test_add():
    assert add(2, 3) == 5

def test_mins():
    assert mins(4,3) == 1