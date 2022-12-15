def common_words(first: str, second: str) -> str:
    lst = list( set( first.split(',') ).intersection( set( second.split(',') ) ) )
    lst.sort()
    return ','.join(lst)

if __name__ == '__main__':
    assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert common_words("one,two,three", "four,five,six") == "", "Too different"
    assert common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

