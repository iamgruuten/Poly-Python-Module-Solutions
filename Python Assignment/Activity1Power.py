print('{:<10s}{:<10s}{:<10s}'.format('a','b','a to power of b'))
count = 1;

while count != 6:
   total = count ** (count + 1) #total value
   print('{:<10d}{:<10d}{:<10d}'.format(count,count+1,total))
   count = count + 1


         
