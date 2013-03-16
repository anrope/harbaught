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
TWO_PT = 'TWO_PT_CONVERSION'

# PLAY REGEX
RUN_RE = re.compile('Run\sformation|' \
    '((left|right)\s(guard|tackle|end))|' \
    'up\sthe\smiddle|scrambles|rushed|lost\s\d+\syards', re.IGNORECASE)
PASS_RE = re.compile('pass|sacked', re.IGNORECASE)
PUNT_RE = re.compile('punt|kicks|kicked', re.IGNORECASE)
FG_RE = re.compile('field\sgoal', re.IGNORECASE)
KNEEL_RE = re.compile('kneels', re.IGNORECASE)
PAT_RE = re.compile('extra\spoint', re.IGNORECASE)
PENALTY_RE = re.compile('PENALTY|penalized', re.IGNORECASE)
SPIKE_RE = re.compile('spiked\sthe\sball', re.IGNORECASE)
FUMBLE_RE = re.compile('FUMBLES', re.IGNORECASE)
INT_RE= re.compile('intercepted', re.IGNORECASE)
REVIEW_RE = re.compile('play\s\under\sreview', re.IGNORECASE)
TWO_PT_RE = re.compile('conversion', re.IGNORECASE)

def get_play_type(play):
    """
    Takes play text and returns the type
    of play RUN,PASS, etc.
    """
    if TWO_PT_RE.search(play):
        return TWO_PT
    elif FG_RE.search(play):
        return FG
    elif INT_RE.search(play):
        return INT
    elif PUNT_RE.search(play):
        return PUNT
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
    elif PASS_RE.search(play):
        return PASS
    elif RUN_RE.search(play):
        return RUN
    else:
        raise Exception('COULD NOT FIND PLAY TYPE:%s' % play)


if __name__ == "__main__":
    play = ''
