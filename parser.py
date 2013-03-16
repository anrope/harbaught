import sys, os
import getopt

import csv
import playmaker
import numerify


def parse_foozball(filename):
    plays = []
    with open(filename, 'rb') as foozball:
        reader = csv.reader(foozball)
        for row in reader:

            #skip gameid row
            if row[0] == 'gameid':
                continue

            #gameid,qtr,min,sec,off,def,down,
            #togo,ydline,description,offscore,defscore,season
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

            # cleaning ints
            for x in ['down', 'to_go', 'minutes',
            'quarter', 'o_score', 'd_score', 'seconds']:
                try:
                    named[x] = int(named[x])
                except:
                    named[x] = None

            #add valid plays
            try:
                named['play_type'] = playmaker.get_play_type(named['play'])
                plays.append(named)
            except Exception, e:
                print e
                #named['play_type'] = None
                #plays.append(named)

        print 'plays logged: %s' % len(plays)

        for play in plays:
            nn_input = {
                'score': numerify.score_to_nn(play['o_score'], play['d_score']),
                'quarter': numerify.quarter_to_nn(play['quarter']),
                'time': numerify.time_to_nn(play['minutes'], play['seconds']),
                'play': numerify.play_to_nn(play['play_type'])
            }


if __name__ == "__main__":
    
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'f:', ['file=',])
    except getopt.GetoptError, e:                
        sys.exit(2) 

    for opt, arg in options:
        if opt in ('-f', '--file'):
            filename = arg
            
    parse_foozball(filename)