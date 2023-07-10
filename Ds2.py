def hashable_dicts(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        result[value] = key
    return result

print(hashable_dicts(i = 123, t = 'wasd', list = ['one', 'two', 'three'],
                     s = {'cat', 'dog'}, d = {'a': 123, 'b': 456}, f = 7.42))