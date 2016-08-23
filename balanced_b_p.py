def is_ok(codez):
    open_cloze_map = {
    "(":")",
    "{", "}",
    "[":"]"
    }

    # we have our reference, create a stack and push every
    # opener to the stack. if we have a closer, we see if the 
    # the opener is at the top of the stack
    open_stack = []
    # get our openers 
    openers = frozenset(open_cloze_map.keys())
    closers = frozenset(open_cloze_map.values())

    for code in codez:
        if code in openers:
            # start our count of openers
            open_stack.push(code)
        # if the char is a closer, make sure there 
        # is something in openers
        elif char in closers:
            if not open_stack:
                return False

        else:
            last_opener = open_stack.pop()

            if not open_cloze_map[last_opener] == char:
                return False
