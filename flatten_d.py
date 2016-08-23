def flatten_d(dict_, delimiter="."):
    # open up the keys and values
    def expand(key, value):
        # if value is a dictionary
        if isinstance(value, dict):
            # return the key with the value with recursion and flatten the value,
            # add a period to seperate key additions 
            return (delimiter.join[key,k]), v
            for k, v in flatten_d(value)
        # if its not a dict, return as is
        else:
            return [(key, value)]
    #  return all items in dict 
    return dict([item for k, v in dict_.items()])