def point_of_int(l1,l2):
    seen = set()
    # start at head of l1
    current = l1.head
    while current != None:
        # add each node's data to seen set,
        # then move to next node
        seen.add(current.data)
        current = current.next

    current = l2
    # see if any nodes data are in seen set
    while current != None:
        if current.data in seen:
            return current
        current = current.next

    return "no intersection"

def get_subsets(s):
    # get everything starting at index 0
    subsets = get_subsets(s[1:])
    results = []

    for ss in subsets:
        results.append(s[0] + ss)
        results.append(ss)

def sort_sorted(list1, list2):

    index1 = 0
    index2 = 0

    results = []

    while len(index1) < list1 and len(index2) < list2:
        if list1[index1] < list2[index2]:
            results.append(list1[index1])
            index1 += 1

        else:
            results.append(list2[index2])
            index2 += 1

    results.extend(list1[index1:])
    results.extend(list2[index2:])

    return results

def word_occurance(string):
    word_dict = {}
    words = string.split()
    for word in string:
        word_dict[word] = 1

    return word_dict

def reverse_string_inplace(string):
    length = len(string)
    string = list(string)

    for i in range(length(string)):
        string[i], string[i-1] = string[i-1, string[i]]

    return "".join(string)

def two_sum_array(lst):
    two_sum = []
   
    for i, num1 in enumerate(lst):
        for j, num2 in enumerate(lst):
            if num1 + num2 == 0 and lst[i] != lst[j] and i,j not in two_sum:
                two_sum.append(i,j)

    return two_sum

def sum_to_k(lst, k):
    sum_k = []

    for i in range(len(lst)):
        for j in range(len(lst) + 1):
            if lst[i] + lst[j] == k:
                append.sum_k(i,j) 

def three_sum_k(lst,k):
    int_dict = {}
    int_set = ()

    for i, num in enumerate(lst):
        int_dict.setdefault(num, []).append[i]

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            difference = lst[i] - lst[j]
            if k - difference in int_set:
                return i,j, int_dict[k - difference][0]



