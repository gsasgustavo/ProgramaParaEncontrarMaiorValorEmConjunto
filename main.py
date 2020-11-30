import datetime

def findBiggerValue(dataset):
    start = datetime.datetime.now()
    with open(dataset+'.csv') as myfile:
        data = myfile.read().split('\n')[:-1]
    higher_number = 0
    for i in data:
        if int(i) > higher_number:
            higher_number = int(i)
    end = datetime.datetime.now()
    timedif = end - start
    higher_values.append(higher_number)
    file = open('resposta-'+dataset+'.txt','w') 
    file.write(str(higher_number)+'\n')
    file.write(str(timedif.total_seconds() * 1000)) 
    file.close() 

higher_values = []

print(findBiggerValue('dataset-2-a'))
print(findBiggerValue('dataset-2-b'))
print(findBiggerValue('dataset-2-c'))
print(findBiggerValue('dataset-2-d'))
print(findBiggerValue('dataset-2-e'))
