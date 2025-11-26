s3 ='10;20;30'
s3.split(';')
index = s3.find('20')
temp = s3[index+1:]
print(temp[0:index])
