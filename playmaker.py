import re

# PLAY TYPES
RUN = 'RUN',
PASS = 'PASS',
PUNT = 'PUNT',
FG = 'FIELD_GOAL'
up\sthe\middle
# PLAY REGEX
RUN_RE = re.compile('Run\sformation|' \
    '(left|right\sguard|tackle)|' \
    'up\sthe\smiddle')
PASS_RE = re.compile('pass')
PUNT_RE = re.compile('punt')
FG_RE = re.compile('field\sgoal')

def get_play_type(play):
    """
    Takes play text and returns the type
    of play RUN,PASS, etc.
    """
    if PASS_RE.match(play):
        return PASS
    elif PUNT_RE.match(play):
        return PUNT
    elif FG_RE.match(play):
        return
    elif RUN_RE.match(play):
        return RUN
    else:
        raise Exception('COULD NOT FIND PLAY TYPE:%s' % play)
