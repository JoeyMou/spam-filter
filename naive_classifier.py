# open the emails data
import os
dir_ham = "dataset/ham/"
dir_spam = "dataset/spam/"
files_ham = os.listdir(dir_ham)
files_spam = os.listdir(dir_spam)
data = []
for file_path in files_ham:
	f = open(dir_ham + file_path, "r")
	text = f.read()
	data.append([text, "ham"])
for file_path in files_spam:
	f = open(dir_spam + file_path, "r")
	text = f.read()
	data.append([text, "spam"])

# shuffle the data, split training and testing data
import random
random.shuffle(data)
train_data = data[0 : int(len(data)/2)]
test_data = data[int(len(data)/2) + 1 : -1]

# map tokens to number of occurences
ham_dict = dict()
spam_dict = dict()
for d in train_data:
	if d[-1] == "ham":
		for word in d[0].split():
			if word in ham_dict:
				ham_dict[word] += 1
			else:
				ham_dict[word] = 1
	elif d[-1] == "spam":
		for word in d[0].split():
			if word in spam_dict:
				spam_dict[word] += 1
			else:
				spam_dict[word] = 1



print(len(spam_dict))
# 	print(spam_dict.items())
print(len(ham_dict))
# 	print(spam_dict.items())


# testing
prior_ham = 0.5
prior_spam = 0.5
correct = 0
wrong = 0
wrong_when_it_is_spam = 0
wrong_when_it_is_ham = 0    
for d in test_data:
	text = d[0]
	p_ham = 1
	p_spam = 1
	for word in text.split():
		num_ham = ham_dict[word] if word in ham_dict else 0.000001
		num_spam = spam_dict[word] if word in spam_dict else 0.000001
		likily_ham = num_ham / (num_ham + num_spam)
		likily_spam = num_spam / (num_ham + num_spam)
		p_ham *= (likily_ham * prior_ham) / (likily_ham * prior_ham + likily_spam * prior_spam)
		p_spam *= (likily_spam * prior_spam) / (likily_ham * prior_ham + likily_spam * prior_spam)
	if p_spam > p_ham and d[-1] == "spam":
		correct += 1
	elif p_spam < p_ham and d[-1] == "ham":
		correct += 1
	else:
		print(d[-1])
		if d[-1] == "spam":
			wrong_when_it_is_spam += 1
		if d[-1] == "ham":
			wrong_when_it_is_ham += 1
		wrong += 1

accuracy = correct / (correct + wrong)

print("\n\n\n\n")
print(correct)
print(wrong)
print(accuracy)

when_spam = wrong_when_it_is_spam / (correct + wrong)
when_ham = wrong_when_it_is_ham / (correct + wrong)
print(when_spam)
print(when_ham)
print(wrong_when_it_is_spam)
print(wrong_when_it_is_ham)