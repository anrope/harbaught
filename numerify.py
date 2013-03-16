def time_to_value(minutes, second):
    if minutes < 2:
        return 0
    else:
        return 1

def score_to_value(o_score, d_score):
    margin = o_score - d_score
    if margin < 3:
        return 0
    elif margin < 7:
        return 1
    elif margin < 10:
        return 2
    elif margin < 14:
        return 3
    elif margin < 17:
        return 4
    else:
        return 5

def quarter_to_value(quarter):
    if quarter == 1:
        return 0
    elif quarter == 2:
        return 1
    elif quarter == 3:
        return 0
    elif quarter == 4:
        return 2
    else:
        return 2

PLAY_TO_VALUE = {
    'RUN': 0,
    'PASS': 1,
    'PUNT': 2,
    'FIELD_GOAL': 3,
    'KNEEL': 4,
    'PAT': 5,
    'SPIKE': 6,
    'PENALTY': 7,
    'FUMBLE': 8,
    'INT': 9,
    'REVIEW': 10
}

VALUE_TO_PLAY = {v: k for k, v in PLAY_TO_VALUE.items()}

def play_to_value(play):
    return PLAY_TO_VALUE[play]
