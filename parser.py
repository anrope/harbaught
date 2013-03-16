import csv
import playmaker

plays = []

with open('foozball_excerpt_2011.csv', 'rb') as foozball:
    reader = csv.reader(foozball)
    for row in reader:
        #gameid,qtr,min,sec,off,def,down,togo,ydline,description,offscore,defscore,season
        named = {
            'game_slug': row[0],
            'quarter': row[1],
            'minutes': row[2],
            'seconds': row[3],
            'o_team': row[4],
            'd_team': row[5],
            'down': row[6],
            'to_go': row[7],
            'yard_line': row[8],
            'play': row[9],
            'o_score': row[10],
            'd_score': row[11],
            'season': row[12]
        }
        try:
            named['play_type'] = playmaker.get_play_type(named['play'])
        except Exception, e:
            print e
            named['play_type'] = None
        plays.append(named)


print len(plays)
print plays[5]
