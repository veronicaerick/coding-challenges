# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

#each closer corresponds to the most recently seen, unclosed opener
#every opener and closer is in a pair

# helper function first 
def is_valid(code):
    open_to_close_map = {
    '(':')',
    '{':'}',
    '[':']'
    }
    #  grab the keys and values and set keys as open
    openers = frozenset(openers_to_closers_map.keys())
    closers = frozenset(openers_to_closers_map.values())

    open-stack = []

    for char in code:
        if char in openers:
            open-stack.append(char)
        elif char in closers:
            return False
        else: 
            last_unclosed_opener = open-stack.pop()

            if not openers_to_closers_map[last_unclosed_opener] == char:
                return False

    return open-stack