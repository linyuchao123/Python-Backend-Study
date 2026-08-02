__all__ = ['test_a']   # __all__指定列表test_a


def test(a,b):
    print(a)
    print(b)

def test_a(a,b):
    print(a + b)

def test_b(a,b):
    print(a + b)

if __name__ == '__main__':
    test(1, 2)