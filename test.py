#!/usr/bin/python3
arg = 'name=philip'
args = arg.split(' ')
print(args)
my_class = args[0]
del args[0]
my_dict = {}
for instance in args:
    key, value = instance.split('=')
    print(f'key: {key}, value: {value}')
    if value[-1:] == '"' and value[:1] == '"':
        value = value[1:-1].replace('_', ' ')
    elif '.' in value:
        value = float(value)
    else:
        try:
            value = int(value)
        except ValueError:
            pass
    new_dict = {key: value}
    my_dict.update(new_dict)
print(my_dict)
