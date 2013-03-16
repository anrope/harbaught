import parser
import catchtwentytwo

plays_2010 = parser.parse_foozball('data/2010_nfl_pbp_data.csv')
plays_2011 = parser.parse_foozball('data/2011_nfl_pbp_data.csv')

# Skip the first play because kickofflol
in_2010, out_2010 = parser.plays_to_ml(plays_2010[1:])
in_2011, out_2011 = parser.plays_to_ml(plays_2011[1:])

pb = catchtwentytwo.get_playbook()
catchtwentytwo.train(pb, in_2010, out_2010)

same = 0
different = 0
for i in range(len(in_2011)):
    predicted = pb.predict(in_2011[i])
    actual = out_2011[i]
    if predicted == actual:
        same += 1
        print 'nailed it!', predicted, actual
    else:
        different += 1
        print 'different', predicted, actual

print 'hit {}, missed {}, total {}'.format(same, different, len(in_2011))
