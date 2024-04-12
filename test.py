def common_prefix(a,b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]

def test_common_prefix():
    assert common_prefix('hello', 'hell') == 'hell'
    assert common_prefix('hello', 'world') == ''
    assert common_prefix('hello', 'hello') == 'hello'
    assert common_prefix('hello', 'hello world') == 'hello'
    assert common_prefix('hello world', 'hello') == 'hello'
    assert common_prefix('hello world', 'hello world') == 'hello world'
    assert common_prefix('hello world', 'hello world!') == 'hello world'
    assert common_prefix('hello world!', 'hello world') == 'hello world'
    assert common_prefix('hello world!', 'hello world!') == 'hello world!'
