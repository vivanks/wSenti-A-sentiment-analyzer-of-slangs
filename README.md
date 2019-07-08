# wSenti - A sentiment analyzer of slangs used in micro-blogs



So, this project which uses power of natual level processing for and gives score of the micro-blogs in range of 0-10, where 0 for most negative and 10 for most psitive sentiment.

In this I developed a model which not only focuses on keywords which also takes into consideration of every single words and try to overcome slangs by making custom dataset and using stemmers to find its original keyword and meaning. Hence, it makes our model different in the form and capability that it can also detects and analyse informal English, which are
mostly used in microblogs.

E.g. For love one can write many variants which are not in English dictionary like “luv”, “lub”, etc. and same one word can be even used to describe sentences also.

# Dataset used

Our dataset for training contains 1,600,000 tweets extracted using Twitter API. The tweets has been marked (0 = negative, 4 = positive) and this can be used to detect sentiments.

# Conclusion

So, to overcome this we are taking more that 1 million twitter data into account and training our model over these slangs and hence predicting it. Our model is achieving accuracy on range of 70%-80% on different datasets of different microblogs. Using which, we are analysing microblogs and calculating it’s score by taking consideration of every word and relation of slang meaning with respect to the context. Which will finally compute the score of a microblog and on the scale of 0-1 up to 8 decimal places we are predicting the score of a microblog and further using scores we can classify the microblog and assign them labels. This can help a business to understand the social sentiment of their brand, product or service which monitoring online conversations.