from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    fall_out_counter = participant_counter - completion_counter

    # print(list(fall_out_counter.keys())[0])

    return list(fall_out_counter.keys())[0]