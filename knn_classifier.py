# open the emails data
import os
files_ham = os.listdir("dataset/ham")
files_spam = os.listdir("dataset/spam")
data = []
for file_path in files_ham:
	f = open("dataset/ham/" + file_path, "r")
	text = f.read()
	data.append([text, "ham", 0.0])
for file_path in files_spam:
	f = open("dataset/spam/" + file_path, "r")
	text = f.read()
	data.append([text, "spam", 0.0])

# shuffle the data, split training and testing data
import random
random.shuffle(data)
train_data = data[0 : int(len(data)/2)]
# test_data = data[int(len(data)/2) + 1 : -1]
test_data = data[-101 : -1]


# start testing
def getSimilarity(record1, record2):
    len1 = len(record1[0].split())
    len2 = len(record2[0].split())
    num_common = 0
    d = dict()
    for word in record1[0].split():
    	if word not in d:
    		d[word] = 1
    for word in record2[0].split():
    	if word in d:
    		num_common += 1
    similarity = num_common / (len1 * len2) ** 0.5
    return similarity


def findKNN(train_data, record, k):
    # get the distance between every train_data and the record
    for i in range(0,len(train_data)):
    	sim = getSimilarity(train_data[i], record)
    	train_data[i][-1] = sim
    # sort the train_data by similarity
    # from operator import itemgetter
    # train_data.sort(key = itemgetter(-1))
    # return the k nearest neighbor
    res = []
    for i in range(k):
    	max_sim = 0
    	max_sim_index = 0
    	for i in range(0, len(train_data)):
    		if train_data[i][-1] > max_sim:
    			max_sim = train_data[i][-1]
    			max_sim_index = i
    	train_data[max_sim_index][-1] = 0
    	res.append(train_data[max_sim_index])
    return res

def judge(knn):
    num_ham = 0
    num_spam = 0
    for r in knn:
        if r[1] == 'ham':
            num_ham += 1
        else:
            num_spam += 1
    print(num_ham)
    print(num_spam)
    return "ham" if num_ham > num_spam else "spam"

correct = 0
wrong = 0    
k = 101
for d in test_data:
    knn = findKNN(train_data, d, k)   
    if judge(knn) == d[1]:
        correct += 1
    else:
        wrong += 1
        print(judge(knn))
        print(d[1])
    print("\n")

accuracy = correct / (correct + wrong)

print("\ncorrect",correct)
print("\nwrong",wrong)
print("\naccuracy",accuracy)
