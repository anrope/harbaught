import sys, os
import getopt

import csv
import playmaker
import numerify
import catchtwentytwo


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
            for x in ['down', 'to_go', 'minutes', 'yard_line',
            'quarter', 'o_score', 'd_score', 'seconds']:
                try:
                    named[x] = int(named[x])
                except:
                    named[x] = None

            if not named['down']:
                named['down'] = 0

            if not named['to_go']:
                named['to_go'] = 0

            #add valid plays
            try:
                named['play_type'] = playmaker.get_play_type(named['play'])
                plays.append(named)
            except Exception, e:
                continue
                #print e
                #named['play_type'] = None
                #plays.append(named)

        print 'plays logged: %s' % len(plays)

        return plays


def plays_to_ml(plays):
    train_in = []
    train_out = []
    for i in range(len(plays)):
        play = plays[i]
        train_in.append({
            'score': numerify.score_to_value(play['o_score'], play['d_score']),
            'quarter': numerify.quarter_to_value(play['quarter']),
            'time': numerify.time_to_value(play['minutes'], play['seconds']),
            'to_go': play['to_go'],
            'yard_line': play['yard_line'],
            'down': play['down']
        }.values())
        train_out.append(numerify.play_to_value(play['play_type']))

    return train_in, train_out


if __name__ == "__main__":
    
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'f:', ['file=',])
    except getopt.GetoptError, e:                
        sys.exit(2) 

    for opt, arg in options:
        if opt in ('-f', '--file'):
            filename = arg
            
    parse_foozball(filename)
