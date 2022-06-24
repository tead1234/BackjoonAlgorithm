def tag_func(tag, text):
    text = text
    tag = tag
    def inner_func():
        print('<{0}>{1}<{0}>'.format(tag, text))
    return inner_func
h1_func = tag_func('title', "This is Python Class")
h1_func()
