#Dataset
For dataset, Enron-Spam datasets is selected. There are actually six groups of Enron-spam datasets, and each of them has different spam-ham ratio. We can use them to perform sufficient experiment. In this report, we mainly used the first dataset of Enron-spam, in which there are 3672 legitimate emails and 1500 spam emails, and the ratio is around 1:3.

#Naïve Bayes Classifier
###Feature selection
For text material, the words are the features obviously. Each word corresponds to one feature. The question is which feature to select and which not. From these the current researches, there are two approaches basically. One is to select all the appearing words; the other is select part of them.

The advantage of first approach is obvious. We don’t need make efforts to select features. The disadvantage is obvious too. We need more space to store the dictionary of words.

If we select features, there will be many approaches to select. The idea is to select most weighing features of all the words, which means the word may appears most frequently or it may have the most biased possibility of constitute a spam or ham.

From experiment, the time and space it takes for the first approach is acceptable. So I took all the appearing words as features for Naïve Bayesian classifier.
###Implement
1. We scan all the emails from training data. For all the words, we create two dictionaries: “ham_dict” and “spam_dict”. The two dictionaries record the words and their occurrence from ham emails and spam emails respectively.
2. After that, we can begin testing. Firstly, we suppose the possibility of this email being spam or ham are equal, which means prior_ham = prior_spam = 0.5.
3: Given a new unknown email, we split it and get all the words.
4. For every word, we get their occurrence in ham and spam emails “num_ham” and “num_spam” respectively by the above “ham_dict” and “spam_dict”.
5. we can compute the likelihood by “num_ham” and “num_spam”.    The likelihood of the word being spam = num_spam / (num_ham + num_spam). The corresponding way for the likelihood of it being ham. 
6. Finally, we can compute the possibility of the whole email being spam or ham by multiple prior and the likelihood of all the words in it. If the possibility of it being spam is greater, we believe it’s a spam, or ham.

###Experiment
Accuracy: `91.14%`

#KNN Classifier
###Feature selection
For the KNN classifier, we also select all the words as the feature. However, I did some improvement when compute the K Nearest Neighbors.

For usual method, we create a dictionary to record all the words appeared. If the length of the dictionary is N, for every email, we create a vector of length N. Every index of the vector corresponds to one word. If the word appears in the email, we’ll set the corresponding index 1. If not, 0.

But, there is a problem. When we compute the distance later, we use the formula as following:
                     
                     Cosine Distance(i,j)=(V_i*V_j)/(|V_i |*|V_j |)
As the vector has a length of N, which can be more thousands, it will take a lot of time to compute the distance of the unknown email to all other training emails. For my experiment, the time is unacceptable. So, we can change it a little bit.

The key of KNN method is to find the neighbors which are nearest. Instead of compute the distance directly, we could compute the similarity. If two emails have greater similarity, we can say they are more near.

Here is how we define similarity:
                     
                         Cosine Similarity(i,j)=C/√(A+B)
                     
Where A is the number of terms in email I, B is the number of terms in email B, and C is the number of terms that email i and j both have.
###Implement
1. For every email in testing set, split it and get the words in it.
2. After that, compute the similarity of this email to any email in training set.
3. Sort the training set by similarity and select the K nearest neighbors.
4. For the K nearest neighbors, classify the email as the class which has the most number of neighbors.

###Experiment
Accuracy: `82.14%` (when K=11)

#SVM Classifier
###Feature selection
Support Vector is a vector of numbers, rather than text string. So, the first thing we need to do is to represent the text using numbers. As usual, we can create a dictionary to record all the words appeared. However, since the dictionary can be very large, which means the vector can be very long, we have to improve it.

So, in my experiment, we can just select the most frequent words. In detail, we can select top N most frequent words in ham email and other N most frequent words in spam email and merge them into one dictionary.
###Implement
1. Use a dictionary to store the individual words which appeared in ham emails and their occurrence from training set. Use another dictionary for ham emails too.
2. After that, select the top N frequent words in the two dictionaries respectively.
3. Merge the two dictionaries into one. For every different word, create an unique index for it.
4. For every email in testing set, represent it using the dictionary above, turn the text into numbers.
5. Use SVM to process this training email and get a model. Use this model to classify the testing emails.

###Experiment
Accuracy: `96.30%` (when N = 1000)
