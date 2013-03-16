import csv
import playmaker
import numerify

plays = []

with open('foozball_excerpt_2011.csv', 'rb') as foozball:
    reader = csv.reader(foozball)
    for row in reader:
        #gameid,qtr,min,sec,off,def,down,togo,ydline,description,offscore,defscore,season
        named = {
            'game_slug': row[0],
            'quarter': int(row[1]),
            'minutes': int(row[2]),
            'seconds': int(row[3]),
            'o_team': row[4],
            'd_team': row[5],
            'down': row[6],
            'to_go': row[7],
            'yard_line': int(row[8]),
            'play': row[9],
            'o_score': int(row[10]),
            'd_score': int(row[11]),
            'season': row[12]
        }

        if not named['down']:
            named['down'] = None

        if not named['to_go']:
            named['to_go'] = None

        try:
            named['play_type'] = playmaker.get_play_type(named['play'])
        except Exception, e:
            print e
            named['play_type'] = None
        plays.append(named)

print len(plays)
print plays[5]

for play in plays:
    nn_input = {
        'score': numerify.score_to_nn(play['o_score'], play['d_score']),
        'quarter': numerify.quarter_to_nn(play['quarter']),
        'time': numerify.time_to_nn(play['minutes'], play['seconds']),
        'play': numerify.play_to_nn(play['play'])
    }

    print nn_input
