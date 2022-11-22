import csv

file = open("TitanicSurvival.csv","r")
data = list(csv.reader(file,delimiter=","))

file.close()

#for i in range(len(data)):
	#data[i][4] = '1st'

change = data[-1]
change[4] = ('1st')
change.append('good')

print(data)

#print(data)



