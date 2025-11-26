times = input('Enter time taken of 2 laps separated by semi-colon (seconds):')



times_list = times.split (';')



firstlap_time = float(times_list[0])

secondlap_time = float(times_list[1])



if firstlap_time < secondlap_time :
    best = firstlap_time
else:
    best = secondlap_time



total = (firstlap_time + secondlap_time) / 2

print('Tom\'s best time is {:.1f} s and average time is {:.1f} s'.format(best, total))
