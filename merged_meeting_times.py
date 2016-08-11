def merge_time_ranges(meetings):
    sorted_meetings = sorted(meetings)

    # start merged_meetings list with the first meetings
    merged_meetings = sorted_meetings[0]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current meetings and last meetings overlap, merge them
        if (current_meeting_start<= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            merged_meetings.append(current_meeting_start,current_meeting_end)

    return merged_meetings