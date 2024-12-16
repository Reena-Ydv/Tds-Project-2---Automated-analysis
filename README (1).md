
    # Automated Data Analysis Report

    ## Dataset Overview
    The dataset comprises **10000 rows** and **23 columns**, containing a mix of:
    - **Numerical Features**: 23
    - **Categorical Features**: 0

    The goal of this analysis is to uncover meaningful patterns, address data quality issues, and prepare the dataset for predictive modeling.

    ## Missing Values Analysis
    Missing data can distort analysis results. Below is a summary of missing values:
    ```
    book_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0
dtype: int64
    ```

    **Approach to Handling Missing Values**:
    - For numerical columns: Imputed with the column mean to preserve overall trends.
    - For categorical columns: Replaced with the most frequently occurring category (mode), ensuring minimal bias.

    ## Summary Statistics
    Here are the descriptive statistics for numerical features:
               book_id  goodreads_book_id  best_book_id  ...      ratings_3     ratings_4     ratings_5
count  10000.00000       1.000000e+04  1.000000e+04  ...   10000.000000  1.000000e+04  1.000000e+04
mean    5000.50000       5.264697e+06  5.471214e+06  ...   11475.893800  1.996570e+04  2.378981e+04
std     2886.89568       7.575462e+06  7.827330e+06  ...   28546.449183  5.144736e+04  7.976889e+04
min        1.00000       1.000000e+00  1.000000e+00  ...     323.000000  7.500000e+02  7.540000e+02
25%     2500.75000       4.627575e+04  4.791175e+04  ...    3112.000000  5.405750e+03  5.334000e+03
50%     5000.50000       3.949655e+05  4.251235e+05  ...    4894.000000  8.269500e+03  8.836000e+03
75%     7500.25000       9.382225e+06  9.636112e+06  ...    9287.000000  1.602350e+04  1.730450e+04
max    10000.00000       3.328864e+07  3.553423e+07  ...  793319.000000  1.481305e+06  3.011543e+06

[8 rows x 16 columns]

    **Key Observations**:
    - Columns with high variance indicate potential outliers or skewed distributions.
    - Columns with low variance may not significantly contribute to model predictions.

    ## Outlier Analysis
    Outliers were identified using Z-scores (threshold = 3):
    - **Impact**: Extreme outliers were replaced with the column mean to avoid distortion while preserving data completeness.
    - This step improves model robustness and prevents undue influence from anomalous values.

    ## Correlation Analysis
    Correlation analysis helps identify relationships between numerical features:
    |                           |     book_id |   goodreads_book_id |   best_book_id |     work_id |   books_count |        isbn |      isbn13 |      authors |   original_publication_year |   original_title |        title |   language_code |   average_rating |   ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |    ratings_3 |   ratings_4 |    ratings_5 |    image_url |   small_image_url |
|:--------------------------|------------:|--------------------:|---------------:|------------:|--------------:|------------:|------------:|-------------:|----------------------------:|-----------------:|-------------:|----------------:|-----------------:|----------------:|---------------------:|--------------------------:|------------:|------------:|-------------:|------------:|-------------:|-------------:|------------------:|
| book_id                   |  1          |          0.110904   |     0.104931   |  0.0922825  |    -0.291646  | -0.0394886  | -0.0783744  | -0.0223316   |                  0.0858572  |      -0.0476214  | -0.00524522  |     0.0115018   |      -0.0360037  |     -0.599881   |         -0.607623    |               -0.546607   | -0.486362   | -0.567637   | -0.61597     | -0.620964   | -0.572266    |  0.0285986   |       0.0285986   |
| goodreads_book_id         |  0.110904   |          1          |     0.961018   |  0.854551   |    -0.241743  | -0.252035   | -0.325474   | -0.0204595   |                  0.336822   |      -0.0811645  |  0.00646675  |    -0.0098262   |      -0.0214029  |     -0.0861138  |         -0.0688252   |                0.206745   | -0.0492176  | -0.0625952  | -0.0822616   | -0.0596144  | -0.061704    | -0.0485227   |      -0.0485227   |
| best_book_id              |  0.104931   |          0.961018   |     1          |  0.821945   |    -0.233421  | -0.251169   | -0.31855    | -0.0174578   |                  0.330176   |      -0.0753495  |  0.0122714   |    -0.00208414  |      -0.0206901  |     -0.0829251  |         -0.0625584   |                0.208773   | -0.0475171  | -0.0590802  | -0.0774123   | -0.0528654  | -0.0551533   | -0.0413664   |      -0.0413664   |
| work_id                   |  0.0922825  |          0.854551   |     0.821945   |  1          |    -0.18462   | -0.217618   | -0.278842   | -0.016209    |                  0.266152   |      -0.0806205  |  0.00165886  |     0.0015754   |      -0.00433824 |     -0.0768153  |         -0.0619912   |                0.177581   | -0.0449463  | -0.0596612  | -0.0775199   | -0.0534363  | -0.0522307   | -0.0608614   |      -0.0608614   |
| books_count               | -0.291646   |         -0.241743   |    -0.233421   | -0.18462    |     1         |  0.0430326  |  0.11033    | -0.0139273   |                 -0.454994   |       0.0462319  |  0.0200303   |     0.0923679   |      -0.102144   |      0.267978   |          0.270882    |                0.1714     |  0.247405   |  0.277762   |  0.293396    |  0.283337   |  0.23492     |  0.0159082   |       0.0159082   |
| isbn                      | -0.0394886  |         -0.252035   |    -0.251169   | -0.217618   |     0.0430326 |  1          |  0.36067    |  0.0147961   |                 -0.0626154  |       0.014948   | -0.00359582  |     0.0541756   |      -0.0193711  |      0.019146   |          0.0156277   |               -0.0447731  |  0.00681505 |  0.0188728  |  0.0322939   |  0.0235814  |  0.0015732   |  0.0222938   |       0.0222938   |
| isbn13                    | -0.0783744  |         -0.325474   |    -0.31855    | -0.278842   |     0.11033   |  0.36067    |  1          |  0.00254912  |                 -0.0917883  |       0.0533591  | -0.0218636   |     0.0655871   |      -0.0690621  |      0.0341961  |          0.0319599   |               -0.0211928  |  0.0246734  |  0.0439463  |  0.0583067   |  0.0380212  |  0.0135543   |  0.00167828  |       0.00167828  |
| authors                   | -0.0223316  |         -0.0204595  |    -0.0174578  | -0.016209   |    -0.0139273 |  0.0147961  |  0.00254912 |  1           |                 -0.00600362 |       0.0393505  |  0.0350577   |    -0.0540365   |       0.00295806 |      0.0119685  |          0.0131113   |                0.00531805 |  0.0127527  |  0.0153666  |  0.0176952   |  0.0146659  |  0.0184655   | -0.000605178 |      -0.000605178 |
| original_publication_year |  0.0858572  |          0.336822   |     0.330176   |  0.266152   |    -0.454994  | -0.0626154  | -0.0917883  | -0.00600362  |                  1          |      -0.044429   | -0.0167486   |    -0.06694     |       0.0215784  |     -0.0901646  |         -0.0846204   |                0.0670629  | -0.0674884  | -0.0876498  | -0.098187    | -0.0739464  | -0.0806321   | -0.0371185   |      -0.0371185   |
| original_title            | -0.0476214  |         -0.0811645  |    -0.0753495  | -0.0806205  |     0.0462319 |  0.014948   |  0.0533591  |  0.0393505   |                 -0.044429   |       1          |  0.796394    |    -0.0353753   |      -0.025526   |      0.0232492  |          0.0270347   |                0.0278253  |  0.0182769  |  0.0273761  |  0.0304473   |  0.0308105  |  0.0114161   | -0.00801772  |      -0.00801772  |
| title                     | -0.00524522 |          0.00646675 |     0.0122714  |  0.00165886 |     0.0200303 | -0.00359582 | -0.0218636  |  0.0350577   |                 -0.0167486  |       0.796394   |  1           |    -0.0493291   |      -0.0384488  |     -0.0061585  |         -0.000137352 |                0.0110166  |  0.00259348 |  0.00176962 | -0.000105047 |  0.00123311 | -0.0145198   | -0.0225237   |      -0.0225237   |
| language_code             |  0.0115018  |         -0.0098262  |    -0.00208414 |  0.0015754  |     0.0923679 |  0.0541756  |  0.0655871  | -0.0540365   |                 -0.06694    |      -0.0353753  | -0.0493291   |     1           |       0.0310041  |     -0.00575687 |         -0.00924886  |               -0.0113353  | -0.00520134 | -0.00870691 | -0.0104708   | -0.00780162 | -0.000447764 |  0.0140639   |       0.0140639   |
| average_rating            | -0.0360037  |         -0.0214029  |    -0.0206901  | -0.00433824 |    -0.102144  | -0.0193711  | -0.0690621  |  0.00295806  |                  0.0215784  |      -0.025526   | -0.0384488   |     0.0310041   |       1          |      0.0385753  |          0.0386793   |               -0.0476351  | -0.12226    | -0.199327   | -0.129423    |  0.0190353  |  0.165441    | -0.00345457  |      -0.00345457  |
| ratings_count             | -0.599881   |         -0.0861138  |    -0.0829251  | -0.0768153  |     0.267978  |  0.019146   |  0.0341961  |  0.0119685   |                 -0.0901646  |       0.0232492  | -0.0061585   |    -0.00575687  |       0.0385753  |      1          |          0.946537    |                0.583935   |  0.685051   |  0.738778   |  0.813547    |  0.882114   |  0.84838     | -0.0419701   |      -0.0419701   |
| work_ratings_count        | -0.607623   |         -0.0688252  |    -0.0625584  | -0.0619912  |     0.270882  |  0.0156277  |  0.0319599  |  0.0131113   |                 -0.0846204  |       0.0270347  | -0.000137352 |    -0.00924886  |       0.0386793  |      0.946537   |          1           |                0.617041   |  0.664537   |  0.750207   |  0.836965    |  0.916951   |  0.847453    | -0.0393832   |      -0.0393832   |
| work_text_reviews_count   | -0.546607   |          0.206745   |     0.208773   |  0.177581   |     0.1714    | -0.0447731  | -0.0211928  |  0.00531805  |                  0.0670629  |       0.0278253  |  0.0110166   |    -0.0113353   |      -0.0476351  |      0.583935   |          0.617041    |                1          |  0.513894   |  0.57474    |  0.586196    |  0.619666   |  0.582712    | -0.0637657   |      -0.0637657   |
| ratings_1                 | -0.486362   |         -0.0492176  |    -0.0475171  | -0.0449463  |     0.247405  |  0.00681505 |  0.0246734  |  0.0127527   |                 -0.0674884  |       0.0182769  |  0.00259348  |    -0.00520134  |      -0.12226    |      0.685051   |          0.664537    |                0.513894   |  1          |  0.770763   |  0.653045    |  0.612061   |  0.639039    | -0.03699     |      -0.03699     |
| ratings_2                 | -0.567637   |         -0.0625952  |    -0.0590802  | -0.0596612  |     0.277762  |  0.0188728  |  0.0439463  |  0.0153666   |                 -0.0876498  |       0.0273761  |  0.00176962  |    -0.00870691  |      -0.199327   |      0.738778   |          0.750207    |                0.57474    |  0.770763   |  1          |  0.867285    |  0.728502   |  0.634639    | -0.0519799   |      -0.0519799   |
| ratings_3                 | -0.61597    |         -0.0822616  |    -0.0774123  | -0.0775199  |     0.293396  |  0.0322939  |  0.0583067  |  0.0176952   |                 -0.098187   |       0.0304473  | -0.000105047 |    -0.0104708   |      -0.129423   |      0.813547   |          0.836965    |                0.586196   |  0.653045   |  0.867285   |  1           |  0.863316   |  0.699578    | -0.0430187   |      -0.0430187   |
| ratings_4                 | -0.620964   |         -0.0596144  |    -0.0528654  | -0.0534363  |     0.283337  |  0.0235814  |  0.0380212  |  0.0146659   |                 -0.0739464  |       0.0308105  |  0.00123311  |    -0.00780162  |       0.0190353  |      0.882114   |          0.916951    |                0.619666   |  0.612061   |  0.728502   |  0.863316    |  1          |  0.777082    | -0.0417465   |      -0.0417465   |
| ratings_5                 | -0.572266   |         -0.061704   |    -0.0551533  | -0.0522307  |     0.23492   |  0.0015732  |  0.0135543  |  0.0184655   |                 -0.0806321  |       0.0114161  | -0.0145198   |    -0.000447764 |       0.165441   |      0.84838    |          0.847453    |                0.582712   |  0.639039   |  0.634639   |  0.699578    |  0.777082   |  1           | -0.0401271   |      -0.0401271   |
| image_url                 |  0.0285986  |         -0.0485227  |    -0.0413664  | -0.0608614  |     0.0159082 |  0.0222938  |  0.00167828 | -0.000605178 |                 -0.0371185  |      -0.00801772 | -0.0225237   |     0.0140639   |      -0.00345457 |     -0.0419701  |         -0.0393832   |               -0.0637657  | -0.03699    | -0.0519799  | -0.0430187   | -0.0417465  | -0.0401271   |  1           |       1           |
| small_image_url           |  0.0285986  |         -0.0485227  |    -0.0413664  | -0.0608614  |     0.0159082 |  0.0222938  |  0.00167828 | -0.000605178 |                 -0.0371185  |      -0.00801772 | -0.0225237   |     0.0140639   |      -0.00345457 |     -0.0419701  |         -0.0393832   |               -0.0637657  | -0.03699    | -0.0519799  | -0.0430187   | -0.0417465  | -0.0401271   |  1           |       1           |

    **Key Feature Relationships**:
    - **goodreads_book_id** and **best_book_id** have a strong positive correlation (correlation = 0.96).
- **goodreads_book_id** and **work_id** have a strong positive correlation (correlation = 0.85).
- **best_book_id** and **goodreads_book_id** have a strong positive correlation (correlation = 0.96).
- **best_book_id** and **work_id** have a strong positive correlation (correlation = 0.82).
- **work_id** and **goodreads_book_id** have a strong positive correlation (correlation = 0.85).
- **work_id** and **best_book_id** have a strong positive correlation (correlation = 0.82).
- **original_title** and **title** have a strong positive correlation (correlation = 0.80).
- **title** and **original_title** have a strong positive correlation (correlation = 0.80).
- **ratings_count** and **work_ratings_count** have a strong positive correlation (correlation = 0.95).
- **ratings_count** and **ratings_2** have a strong positive correlation (correlation = 0.74).
- **ratings_count** and **ratings_3** have a strong positive correlation (correlation = 0.81).
- **ratings_count** and **ratings_4** have a strong positive correlation (correlation = 0.88).
- **ratings_count** and **ratings_5** have a strong positive correlation (correlation = 0.85).
- **work_ratings_count** and **ratings_count** have a strong positive correlation (correlation = 0.95).
- **work_ratings_count** and **ratings_2** have a strong positive correlation (correlation = 0.75).
- **work_ratings_count** and **ratings_3** have a strong positive correlation (correlation = 0.84).
- **work_ratings_count** and **ratings_4** have a strong positive correlation (correlation = 0.92).
- **work_ratings_count** and **ratings_5** have a strong positive correlation (correlation = 0.85).
- **ratings_1** and **ratings_2** have a strong positive correlation (correlation = 0.77).
- **ratings_2** and **ratings_count** have a strong positive correlation (correlation = 0.74).
- **ratings_2** and **work_ratings_count** have a strong positive correlation (correlation = 0.75).
- **ratings_2** and **ratings_1** have a strong positive correlation (correlation = 0.77).
- **ratings_2** and **ratings_3** have a strong positive correlation (correlation = 0.87).
- **ratings_2** and **ratings_4** have a strong positive correlation (correlation = 0.73).
- **ratings_3** and **ratings_count** have a strong positive correlation (correlation = 0.81).
- **ratings_3** and **work_ratings_count** have a strong positive correlation (correlation = 0.84).
- **ratings_3** and **ratings_2** have a strong positive correlation (correlation = 0.87).
- **ratings_3** and **ratings_4** have a strong positive correlation (correlation = 0.86).
- **ratings_4** and **ratings_count** have a strong positive correlation (correlation = 0.88).
- **ratings_4** and **work_ratings_count** have a strong positive correlation (correlation = 0.92).
- **ratings_4** and **ratings_2** have a strong positive correlation (correlation = 0.73).
- **ratings_4** and **ratings_3** have a strong positive correlation (correlation = 0.86).
- **ratings_4** and **ratings_5** have a strong positive correlation (correlation = 0.78).
- **ratings_5** and **ratings_count** have a strong positive correlation (correlation = 0.85).
- **ratings_5** and **work_ratings_count** have a strong positive correlation (correlation = 0.85).
- **ratings_5** and **ratings_4** have a strong positive correlation (correlation = 0.78).
- **image_url** and **small_image_url** have a strong positive correlation (correlation = 1.00).
- **small_image_url** and **image_url** have a strong positive correlation (correlation = 1.00).

    **Implications**:
    - Strong correlations suggest potential redundancy, where one feature may predict another. These features could be considered for dimensionality reduction or combined into a new feature.
    - Weak correlations may still hold value for non-linear models or interaction effects.

    ## Principal Component Analysis (PCA)
    PCA was applied to reduce dimensionality while retaining key variance:
    - The first two principal components explain a significant proportion of the dataset variance.
    - This technique simplifies visualization and highlights underlying patterns.

    **Insights**:
    - The PCA scatter plot (see `pca_plot.png`) reveals clusters and separations in the data.
    - Features contributing the most to the principal components can guide feature selection or engineering.

    ## Clustering Analysis (KMeans)
    Clustering helps identify groups of similar observations. Here are the results:
    - **Number of Clusters**: {len(set(clusters))}
    - **Cluster Sizes**:
      ```
      {cluster_counts.to_string()}
      ```

    **Cluster Insights**:
    - Cluster 0 contains 9300 observations.
- Cluster 1 contains 585 observations.
- Cluster 2 contains 115 observations.

    - Clustering can uncover meaningful segments, such as customer groups or geographic regions.
    - For example, smaller clusters might represent niche segments or outliers.

    ## Data Distributions
    Distributions for each numerical column provide insights into their spread, central tendency, and potential skewness:
    
        ### book_id
        - **Mean**: 5000.50
        - **Median**: 5000.50
        - **Standard Deviation**: 2886.90
        - **Skewness**: 0.00 (symmetric)
        - **Kurtosis**: -1.20 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### goodreads_book_id
        - **Mean**: 5073922.41
        - **Median**: 394965.50
        - **Standard Deviation**: 7262737.40
        - **Skewness**: 1.31 (right-skewed)
        - **Kurtosis**: 0.51 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### best_book_id
        - **Mean**: 5249498.42
        - **Median**: 425123.50
        - **Standard Deviation**: 7459231.52
        - **Skewness**: 1.31 (right-skewed)
        - **Kurtosis**: 0.51 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### work_id
        - **Mean**: 7654477.84
        - **Median**: 2719524.50
        - **Standard Deviation**: 10010161.67
        - **Skewness**: 1.74 (right-skewed)
        - **Kurtosis**: 2.62 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### books_count
        - **Mean**: 56.98
        - **Median**: 40.00
        - **Standard Deviation**: 66.20
        - **Skewness**: 3.93 (right-skewed)
        - **Kurtosis**: 19.78 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### isbn
        - **Mean**: 4324.03
        - **Median**: 4299.50
        - **Standard Deviation**: 2848.00
        - **Skewness**: 0.04 (right-skewed)
        - **Kurtosis**: -1.24 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### isbn13
        - **Mean**: 9778612383858.68
        - **Median**: 9780000000000.00
        - **Standard Deviation**: 6131522906.91
        - **Skewness**: -3.52 (left-skewed)
        - **Kurtosis**: 11.38 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### authors
        - **Mean**: 2344.09
        - **Median**: 2369.50
        - **Standard Deviation**: 1321.70
        - **Skewness**: -0.05 (left-skewed)
        - **Kurtosis**: -1.17 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### original_publication_year
        - **Mean**: 1991.69
        - **Median**: 2004.00
        - **Standard Deviation**: 40.74
        - **Skewness**: -5.19 (left-skewed)
        - **Kurtosis**: 38.28 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### original_title
        - **Mean**: 4359.85
        - **Median**: 4341.50
        - **Standard Deviation**: 2814.96
        - **Skewness**: 0.03 (right-skewed)
        - **Kurtosis**: -1.23 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### title
        - **Mean**: 4983.13
        - **Median**: 4987.50
        - **Standard Deviation**: 2875.60
        - **Skewness**: -0.00 (left-skewed)
        - **Kurtosis**: -1.20 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### language_code
        - **Mean**: 5.77
        - **Median**: 6.00
        - **Standard Deviation**: 1.22
        - **Skewness**: 6.11 (right-skewed)
        - **Kurtosis**: 82.01 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### average_rating
        - **Mean**: 4.01
        - **Median**: 4.02
        - **Standard Deviation**: 0.24
        - **Skewness**: -0.28 (left-skewed)
        - **Kurtosis**: 0.06 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### ratings_count
        - **Mean**: 41358.74
        - **Median**: 21155.50
        - **Standard Deviation**: 61677.62
        - **Skewness**: 4.29 (right-skewed)
        - **Kurtosis**: 22.31 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### work_ratings_count
        - **Mean**: 45513.29
        - **Median**: 23832.50
        - **Standard Deviation**: 65612.85
        - **Skewness**: 4.22 (right-skewed)
        - **Kurtosis**: 21.70 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### work_text_reviews_count
        - **Mean**: 2346.15
        - **Median**: 1402.00
        - **Standard Deviation**: 2929.49
        - **Skewness**: 3.04 (right-skewed)
        - **Kurtosis**: 11.23 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### ratings_1
        - **Mean**: 975.63
        - **Median**: 391.00
        - **Standard Deviation**: 1963.51
        - **Skewness**: 5.35 (right-skewed)
        - **Kurtosis**: 35.64 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### ratings_2
        - **Mean**: 2310.51
        - **Median**: 1163.00
        - **Standard Deviation**: 3507.19
        - **Skewness**: 4.01 (right-skewed)
        - **Kurtosis**: 19.93 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### ratings_3
        - **Mean**: 8874.41
        - **Median**: 4894.00
        - **Standard Deviation**: 11919.53
        - **Skewness**: 3.77 (right-skewed)
        - **Kurtosis**: 17.18 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### ratings_4
        - **Mean**: 15307.72
        - **Median**: 8269.50
        - **Standard Deviation**: 20862.67
        - **Skewness**: 3.96 (right-skewed)
        - **Kurtosis**: 18.97 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### ratings_5
        - **Mean**: 17628.49
        - **Median**: 8836.00
        - **Standard Deviation**: 27854.69
        - **Skewness**: 4.49 (right-skewed)
        - **Kurtosis**: 25.00 (leptokurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### image_url
        - **Mean**: 4444.56
        - **Median**: 4999.50
        - **Standard Deviation**: 2222.94
        - **Skewness**: -0.50 (left-skewed)
        - **Kurtosis**: -1.20 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
        ### small_image_url
        - **Mean**: 4444.56
        - **Median**: 4999.50
        - **Standard Deviation**: 2222.94
        - **Skewness**: -0.50 (left-skewed)
        - **Kurtosis**: -1.20 (platykurtic)

        **Implications**:
        - A skewness of ±1 indicates moderate skew; features with strong skewness may benefit from transformations (e.g., log or square root).
        - High kurtosis may indicate heavy tails or outliers, requiring further attention.
        
    ## Visualizations
    Several visualizations were generated to support the analysis:
    - **Missing Values Heatmap**: Highlights patterns of missing data (see `missing_values.png`).
    - **Correlation Heatmap**: Displays feature relationships (see `correlation_matrix.png`).
    - **PCA Scatter Plot**: Visualizes the first two principal components (see `pca_plot.png`).
    - **Feature Distributions**: Each numerical column's distribution is saved as a PNG file.

    ## Recommendations
    Based on the analysis:
    - Strongly correlated features can be combined or reduced for more efficient modeling.
    - Features with high skewness should be transformed for better normalization.
    - Cluster assignments can be used as additional features or for segmentation analysis.

    ## Conclusion
    This analysis provided a comprehensive overview of the dataset, addressing missing values, outliers, feature relationships, and clustering patterns. These insights can guide further modeling efforts and domain-specific decision-making.
    