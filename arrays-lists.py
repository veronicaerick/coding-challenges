a# Given a list of words, return a list of words that are anagrams of eachother

def anagram_lists(words):
    word_dict = {}
    # sort the word
    sorted_word = "".join(sorted(word))
    # iterate through and see if the sorted word is in our dict,
    # if so, append word. if not, add word as value.
    for word in words:
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]
    # look at our results and return them as lists within a list
    results = []
    for s_w, w in word_dict.iteritems():
        results.append(w)

# given a list of ints, determine whether a pair sums up to S

def sum_to_S(lst, S):
    int_dict = {}
    pairs = set()
    # iterate through list starting at lst[0], lst[1] and see if they sum to S
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == S and not in pairs and lst[i] != lst[j]:
                pairs.add(i,j)

    return list(pairs)

# given a list, see if any three items sum to S
def three_sum_to_S(lst, S):
    int_dict = {}
    int_set = set(lst)

    # set keys and vals for dict, int_dict[num] = [i]
    for i, num in enumerate(lst):
        int_dict.setdefault(num, []).append(i)
    #  iterate through, keep track of two, compare two items to
    # see if S-diff is in the set. If it is, there are 3 items that
    # sum to S, return those
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            diff = lst[i] + lst[j]
            if S - diff in int_set:
                return i, j, int_dict[S-diff][0]
    # found nothing, so return None
    return None


# check if a tree is balanced
def is_balanced(self):
    if not node:
        return 0

    left = _num_descendants(node.left)
    if left in None:
        return None

    right = _num_descendants(node.right)
    if right is None:
        return None

    # if heights vary by more than one, its imbalanced
    if abs(left-right) > 1:
        return None
    # height of this node is the highest of our deepest descendant + us
    return max(left,right) + 1
        return None
return _num_descendants(self) is not None

def binary_search(val):
    higher_than = 0
    lower_than = 0
    guesses = 0
    guessed = None

    while guesses != val:
        guesses += 1
        guessed = (lower_than - higher_than) / 2 + higher_than
        if val < guessed:
            lower_than = guess

        elif val > guessed:
            higher_than = guess


    return guesses

def lowest_common_ancestor(root, node1, node2):
    if root is None:
        return None

    if node1 < root.data < node2:
        return root
    # if both nodes are less than, LCA is on the left
    elif if root.data > node1 and root.data > node2:
        return lowest_common_ancestor(root.left, node1, node2)

    else:
        return lowest_common_ancestor(root.right, node1, node2)

# given 2 sorted arrays, find the kth element after the merge
def find_kth_2_sorted_arrays(lst1, lst2):
    sorted_list = []
    indexA = 0
    indexB = 0

    while indexA < len(lst1) and indexB < len(lst2):
        if lst1[indexA] < lst2[indexB]:
            sorted_list.append(lst1[indexA])
        else:
            sorted_list.append(lst1[indexB])

    extend.sorted_list(lst1[indexA:])
    extend.sorted_list(lst2[indexB:])



def find_permutations(string):
    if len(string) == 1:
        return [string]

    # recursivly call, start at second index, grab first char
    permutations = find_permutations(string[1:])
    first_letter = string[0]
    results = []
    # iterate thru, moving the place we are inserting each char around
    # per iteration
    for perm in permutations:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + first_letter + perm[i:])

    return result

def is_permutation(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    for i in range(len(s1_sorted)):
        if s1_sorted[i] != s2_sorted:
            return False

    return True

def unique_chars(string):
    unique = set()

    for letters in string:
        if char in unique:
            return False
        else:
            unqiue.add(char)
        return True

def second_largest(lst):
    if len(lst) < 2:
        return None

    max_num = lst[0]
    second_max = min(lst)

    for num in lst:
        if num > max_num:
            max_num = num
            second_max = max_num
        elif num > second_max and num != max_num:
            second_max = num

def get_subsets(elements):

    if len(elements) > 0:
        result = []
        head = elements[0]
        for tail in get_subsets(elements[1:]):
            result.append(head + tail)
            result.append(tail)
        return result

def powerset(seq):
    result = []
    if len(seq) <=1:
        return None
    else:
        for i in powerset(seq[1:]):
            result.append(seq[0] + item)
            result.append(item)
    return result

def two_sum(lst, S):
    result = []

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == S:
                result.append(i,j)

def two_sum_v2(lst, S):
    result = []
    int_dict = {}

    for i in range(0,len(lst)):
        sumMinItem = S - arr[i]
        if sumMinItem in int_dict:
            sums.append(lst[i], sumMinItem)
        int_dict[lst[i]] = lst[i]

def find_dupes(lst):
    int_dict = {}
    int_dupes = ()
    for i in range(len(lst)):
        if lst[i] not in int_dict:
            int_dict[arr[i]] = True
        elif lst[i] in int_dict:
            int_dupes.append(lst[i])

# You will be given a list of stock prices for a given day and your goal is to return the maximum profit that could have been made by buying a stock at the given price and then selling the stock later on. For example if the input is: [45, 24, 35, 31, 40, 38, 11] then your program should return 16 because if you bought the stock at $24 and sold it at $40, a profit of $16 was made and this is the largest profit that could be made. If no profit could have been made, return -1.
def stock_picker(lst):
    max_profit = -1
    buy_price = 0
    sell_price = 0

    change_index = True

    for i in range(0, len(lst) -1):
        sell_price = lst[i + 1]
        if change_index:
            buy_price = lst[i]
        if sell_price < buy_price:
            change_index = True
            continue
        else:
            temp_profit = sell_price - buy_price
            if temp_profit > max_profit:
                max_profit = temp_profit
            change_index = False

    return max_profit

def count_anagrams(string):
    char_dict = {}
    for word in string.split(" "):
        sorted_word = ''.join(sorted(word))
        char_dict.setdefault(sorted_word,[]).append(word)

    return char_dict.itervalues()

def anagram_of_palindrome(string):

    char_dict = {}
    seen_odd = False

    for char in string:
        count = char_dict.get(char, 0)
        char_dict[char] = count + 1

    for count in char_dict.values():
        if count %2 != 0:
            if seen_odd:
                return False
            seen_odd = True

    return True

def count_recursively(lst):
    if not lst:
        return 0

    return count_recursively([1:]) + 1

def binary_search(val):
    higher_than = 0
    lower_than = 101
    num_guesses = 0

    guess = None

    while val != guess:
        num_guesses += 1
        guess = (lower_than-higher_than) / 2 + higher_than
        if guess > val:
            higher_than = guess
        elif guess < val:
            lower_than = guess

    return num_guesses

def remove_node(node):
    if not node.next:
        return

    node.data = node.next.data
    node.next = node.next.next

def decode_string(string):
    word = ""
    i = 0
    while i < len(s):
        num_skip = int(s[i])
        i += num_skip + 1

        word += s[i]

        i+=1

    return word

def reverse_list_inplace(lst):
    for i in range(len(lst)/2):
        lst[i], lst[i-1] = lst[i-1], lst[i]

def reverse_string(string):
    out = ""

    for i in range(len(string), 0, -1):
        out += string[i-1]

    return out

def reverse_ll(head):
    out_head = None
    n = head

    while n is not None:
        out_head = Node(n.data, out_head)
        n = n.next

    return out_head

def reverse_lL_in_place(lst):
    prev = None
    current = lst.head

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    lst.head = prev

def make_anagram_dict(words):
    out = {}

    for w in words:
        sorted_word = "".join(sorted(word))
        out.setdefault(sorted_word, []).append(w)

    return out

def most_common_anagrams(wordlist):
    all_anas_dict = make_anagram_dict(wordlist)
    highest_num_anagrams = 0
    most_anagrams = None

    for w in wordlist:
        sorted_word = "".join(sorted(w))
        number_amagrams = len(all_anas_dict[sorted_word])
        if number_amagrams > highest_num_anagrams:
            highest_num_anagrams = number_amagrams
            most_anagrams = w
        return most anagrams

def reverse(s):
    current_token = ''
    tokens= []

    in_space = None

    for letter in s:
        if letter == " ":
            if not in_space:
                tokens.append(current_token)
                current_token = ''
                in_space = True
        else:
            if in_space:
                tokens.append(current_token)
                current_token = ''
                in_space = False
            current_token += letter

        tokens.append(current_token)

    return ''.join(reversed(tokens))

def substring_within_string(string,substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i] == substring[0]:
            start = 0
            while start < len(substring) and string[i + start] == substring[start]:
                start += 1
            if start == len(substring):
                return i

#
def stock_picker(lst):
    max_profit = 0

    for purchase_time in range(0, len(lst) - 1):
        for sell_time in range(purchase_time, len(lst)):
            profit = lst[sell_time] - lst[purchase_time]
            if profit > max_profit:
                max_profit = profit

    return max_profit

def is_perm(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    for i in range(len(sorted_s1)):
        if (sorted_s1[0] != sorted_s2[0]:
