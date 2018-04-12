# Movie-Rating-Recommendation-System
The training data: a set of movie ratings by 200 users (userid: 1-200) on 1000 movies (movieid: 1-1000). 

The data is stored in a 200 row x 1000 column table. Each row represents one user. Each column represents one movie. A rating is a value in the range of 1 to 5, where 1 is "least favored" and 5 is "most favored".Please NOTE that a value of 0 means that the user has not explicitly rated the movie.

The Test Data:(test5.txt) A pool of movie ratings by 100 users (userid: 201-300). Each user has already rated 5 movies. The format of the data is as follows: the file contains 100 blocks of lines. Each block contains several triples : (U, M, R), which means that user U gives R points to movie M.Please note that in the test file, if R=0, then you are expected to predict the best possible rating which user U will give movie M.

User-Based Collaborative Filtering Algorithms
1.1 Implement the basic user-based collaborative filtering algorithmsPlease implement two versions of the basic user-based collaborative filtering algorithm as the the Cosinesimilarity methodand Pearson Correlation method.
1.2 Extensions to thebasic user-based collaborative filtering algorithmsPlease implement the following two modifications to the standard algorithm (using Pearson Correlation): 1. Inverse user frequency; 2. Case modification. 2. Item-Based Collaborative Filtering Algorithm Please implementthe item-based collaborative filtering algorithmbased on adjusted cosine similarity. 
