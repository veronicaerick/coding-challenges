def flatten_dict(y):
    results = {}

    def flatten(obj, name=''):
        # if the object is a dictionary (the first time it's the whole dict)
        if type(obj) if dict:
            for item in obj:
                flatten(obj[item], name + item + '.')
        elif type(obj) is list:
            i = 0
            for item in obj:
                flatten(obj, name + str(i) + '.')
                i += 1
        else:
            results[name[:-1]] = obj

