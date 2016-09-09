# The mall management is trying to figure out what was the busiest moment in the mall in the last year.
# You are given data from the door detectors: each data entry includes a timestamp (seconds in Unix Epoch format), an amount of people and whether they entered or exited.

# Example of a data entry:
# { time: 1440084737,  count: 4,  type: "enter" }

# Find what was the busiest period in the mall on the last year. Return an array with two Epoch timestamps representing the beginning and end of that period. You may assume that the data your are given is accurate and that each second with entries or exits is recorded. Implement the most efficient solution possible and analyze its time and space complexity.

# SOLUTION To find the busiest time, we need to figure out how many people were at the mall after each entry/exit. However, we are given the changes in the number of people, and not this number. We can build this data by adding/subtracting each entry/exist by ascending time order.

# Since we are not promised that the data is sorted by time, we need to sort it by time in ascending order.
# Once the data is sorted we can scan it linearly in-order and keep a variable with the amount of people in the mall. For each change in the number we compare the current number to the maximum we had so far, and make it the new maximum if it is bigger. Also, to store the end of the max period, we set it before examining the next data entry.
# 1) sort by times in asending order, then keep 
#  a variable with amount of people in the mall
# for each change, compare current to max, switch it current > max.

def find_busiest_period(data):
    if data == None:
        return None

    data.sort(time)
    n = len(data)

    count = 0
    max_count = 0
    max_period = [0,0]
    for i in range(len(n) -1):
        # change count depending on enter or exit type:
        if data[i].type == 'enter':
            count += data[i].count
        elif data[i].type == 'exit':
            count -= data[i].count
    # see if current time is same as last time
        if (i < n-1 and data[i].time == data[i+1].time):
            continue 
    # if the count is larger than max, reassign count to max
        if count > max_count:
            max_count = count
            # assign start of busiest time to current time
            max_period[0] = data[i].time
            # if current place is smaller than the length of the data up to second to las
            if (i < n-1):
                # assign end time to the next time
                max_period[1] = data[i + 1].time
            else:
                # otherwise assign end time to current times
                max_period[1] = data[i].time

    return max_period

