## Project Goals 🎯

### 🏠 Building a supervised ML model to predict housing prices based on the season, region, and housing features.

## Process 🔄

### Step 1: Data Extraction 📂

#### Extracting data from the JSON file, understanding it, and then selecting the features of interest, subsequently turning it into a dataframe. The features chosen for this model were:
* price_reduced_amount
* Year Built
* Sold Price
* Lot SqFt
* Baths
* Beds
* Garage
* Type (e.g., Condo, Townhouse)
* Tags Count (features the place has)
* list_season
* sold_season

### Step 2: Data Cleaning 🧼

#### Cleaning the data involved finding nulls and NaNs and either filling them with means, zeros, or dropping them. For example:
1. Replaced null values with zeros in the garage column since some houses might not have garages.
2. Nan values in Lot SqFt, Baths, Beds, Garage were replaced with the average for each unique Type of housing.
3. Dropped some NaN-valued columns like land which didn't have value for this model because it wasn't a house.

![Boxplot for Outliers](https://github.com/Asal-zou/predicting-the-housing-price/assets/134029102/ce2e79ef-d053-4741-b7e2-c01546c21393)


### Step 3: Outlier Detection 🚨

#### Detecting outliers with Boxplot and dropping them. For example:
* There were 107 outliers in Lot SqFt, which were dropped.

### Step 4: Data Splitting and Training 🔀

#### Split the data and trained the model before encoding and choosing a model.

### Step 5: Transformation for Encoding 🔧

#### Transformed categorical columns to make encoding easier:
1. Consolidated housing types. For example, renamed "condos" to "condo".
2. Changed dates into seasons since the season can affect the selling price.
3. Dropped the city and used the state to map the region.

### Step 6: Model Selection and Validation 📊

#### Chose different models to determine the best performer, using Mean Absolute Error (MAE) and R² to track their performances.

### Step 7: Cross-validation and Hyperparameter Optimization 🔍

#### Performed cross-validation and hyperparameter optimization to ensure the model was not overfitting and to find the best parameters for optimal performance.

### Step 8: Final Training 🏋️

#### Trained the model on the whole dataset after ensuring it was working well.

## Results 🏆

![Explained Variance by PCA Components](https://github.com/Asal-zou/predicting-the-housing-price/assets/134029102/93bf3740-725d-4d67-88ef-cc8bb493851c)

![Year Built vs. Sold Price](https://github.com/Asal-zou/predicting-the-housing-price/assets/134029102/dad956c0-1d20-464b-afb6-96266129dd02)


1. **Random Forest** was chosen for its lower MAE (MAE: 10.01) and higher R² (R²: 0.98), indicating a good ability to explain variance in the data.
2. After performing cross-validation and hyperparameter search, the best cross-validation score was:
   * Training set: 0.94
   * Test set: 0.981
   
   This indicates the model performs well on both the training and unseen test data, demonstrating good generalization and consistent hyperparameters.

## Challenges ⚠️

1. Loading JSON files correctly.
2. Understanding and handling the tags column.
3. Deciding how to encode the categorical columns without creating too many columns.

## Future Goals 🚀

* Create a functions and variables file.
* Experiment with more features and more complex categorical groups.

![Distribution of Year Built](https://github.com/Asal-zou/predicting-the-housing-price/assets/134029102/58c6b64d-c414-4806-92e7-161ca21ad606)

![Distribution of Sold Price](https://github.com/Asal-zou/predicting-the-housing-price/assets/134029102/91df1803-9fd2-4d8d-9950-203bf1c153bb)
