"""
Playmaker
=========
Make and categorize plays.
"""
import re

# PLAY TYPES
RUN = 'RUN'
PASS = 'PASS'
PUNT = 'PUNT'
FG = 'FIELD_GOAL'
KNEEL = 'KNEEL'
PAT = 'PAT'
PENALTY = 'PENALTY'
SPIKE = 'SPIKE'
FUMBLE = 'FUMBLE'
INT = 'INT'
REVIEW = 'REVIEW'

# PLAY REGEX
RUN_RE = re.compile('Run\sformation|' \
    '((left|right)\s(guard|tackle|end))|' \
    'up\sthe\smiddle|scrambles|rushed|lost\s\d+\syards')
PASS_RE = re.compile('pass|sacked')
PUNT_RE = re.compile('punt|kicks|kicked')
FG_RE = re.compile('field\sgoal')
KNEEL_RE = re.compile('kneels')
PAT_RE = re.compile('extra\spoint')
PENALTY_RE = re.compile('PENALTY|penalized')
SPIKE_RE = re.compile('spiked\sthe\sball')
FUMBLE_RE = re.compile('FUMBLES')
INT_RE= re.compile('intercepted')
REVIEW_RE = re.compile('play\s\under\sreview')

def get_play_type(play):
    """
    Takes play text and returns the type
    of play RUN,PASS, etc.
    """
    if PASS_RE.search(play):
        return PASS
    elif FG_RE.search(play):
        return FG
    elif INT_RE.search(play):
        return INT
    elif PUNT_RE.search(play):
        return PUNT
    elif RUN_RE.search(play):
        return RUN
    elif KNEEL_RE.search(play):
        return KNEEL
    elif PAT_RE.search(play):
        return PAT
    elif SPIKE_RE.search(play):
        return SPIKE
    elif PENALTY_RE.search(play):
        return PENALTY
    elif FUMBLE_RE.search(play):
        return FUMBLE
    elif REVIEW_RE.search(play):
        return REVIEW
    else:
        raise Exception('COULD NOT FIND PLAY TYPE:%s' % play)


if __name__ == "__main__":
    play = ''