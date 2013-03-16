def time_to_nn(minutes, second):
    if minutes < 2:
        return 0
    else:
        return 1

def score_to_nn(o_score, d_score):
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

def quarter_to_nn(quarter):
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

def play_to_nn(play):
    if play == 'RUN':
        return 0
    elif play == 'PASS':
        return 1
    elif play == 'PUNT':
        return 2
    elif play == 'FIELD_GOAL':
        return 3
    elif play == 'KNEEL':
        return 4
    elif play == 'PAT':
        return 5
    elif play == 'SPIKE':
        return 6
    elif play == 'PENALTY':
        return 7
    elif play == 'FUMBLE':
        return 8