# open the emails data
import os
files_ham = os.listdir("dataset/ham")
files_spam = os.listdir("dataset/spam")
data = []
for file_path in files_ham:
	f = open("dataset/ham/" + file_path, "r")
	text = f.read()
	data.append([text, 1])
for file_path in files_spam:
	f = open("dataset/spam/" + file_path, "r")
	text = f.read()
	data.append([text, -1])

# shuffle the data, split training and testing data
import random
random.shuffle(data)
train_data = data[0 : int(len(data)/2)]
test_data = data[int(len(data)/2) + 1 : -1]



# map tokens to number of occurences
ham_dict = {}
spam_dict = {}
for d in train_data:
	if d[-1] == 1:
		for word in d[0].split():
			if word in ham_dict:
				ham_dict[word] += 1
			else:
				ham_dict[word] = 1
	elif d[-1] == -1:
		for word in d[0].split():
			if word in spam_dict:
				spam_dict[word] += 1
			else:
				spam_dict[word] = 1
# Take first N most frequent words in ham and spam respectively,
# and merge into one word dictionary

N = 1000
ham_top_words = sorted(ham_dict, key = ham_dict.get, reverse = True)[:N]
spam_top_words = sorted(spam_dict, key = spam_dict.get, reverse = True)[:N]


# print (len(ham_top_words))
# print (len(spam_top_words))
word_dict = dict()
index = 0
for word in ham_top_words:
	if word not in word_dict:
		word_dict[word] = index
		index += 1
for word in spam_top_words:
	if word not in word_dict:
		word_dict[word] = index
		index += 1
# print(len(word_dict))


import numpy as np
from liblinearutil import *
# training
dat = []
classes = []
for d in train_data:
	vector = [0] * len(word_dict)
	for word in d[0].split():
		if word in word_dict:
			index = word_dict.get(word)
			vector[index] = 1
	dat.append(vector)
	classes.append(d[1])
y, x = classes, dat
prob  = problem(y, x)
param = parameter()
m = train(prob, param)

# testing
dat = []
classes = []
for d in test_data:
	vector = [0] * len(word_dict)
	for word in d[0].split():
		if word in word_dict:
			index = word_dict.get(word)
			vector[index] = 1
	dat.append(vector)
	classes.append(d[1])
y, x = classes, dat
pred_labels, (ACC, MSE, SCC), pred_values = predict(y,x,m)
print(ACC)

