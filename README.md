## Project Goals

### Building a supervised ML model so we can predict the housing price based on the season, region, and housing features.

## Process

### Step 1: Data Extraction

#### Extracting data from the JSON file, understanding it, and then selecting the features that we were interested in, subsequently turning it into a dataframe. The features that we chose to use for this model were:
###### price_reduced_amount, Year Built, Sold Price, Lot SqFt, Baths, Beds, Garage, Type (for example, Condo, Townhouse, etc.), Tags Count (what features the place has), list_season, sold_season.

### Step 2: Data Cleaning

#### Cleaning the data involved finding nulls and NaNs and either filling them with means, zeros, or dropping them. For example:
###### 1. We replaced null values with zeros for my garage column since some houses might not have garages.
###### 2. Nan values of Lot SqFt, Baths, Beds, Garage were replaced with the average that exists for each unique Type of housing.
###### 3. Dropped some of the NaN-valued columns like land which didn't have value for this model because it wasn't a house.

### Step 3: Outlier Detection

##### Detecting outliers with Boxplot and dropping them after calculating how many there were, for example:
###### There were 107 outliers in Lot SqFt variables, which I dropped.

### Step 4: Data Splitting and Training

#### Split and trained the data before encoding and choosing a model.

### Step 5: Transformation for Encoding

##### Transformed my categorical columns to make it easier to transform (encode) them.
###### 1. We made the housing Type to a shorter list. For example, renamed "condos" to "condo", which were different groupings because of the "s".
###### 2. Changed my dates into seasons since the season can affect the selling price.
###### 3. Lastly, I dropped the city and used the state to map the region.

### Step 6: Model Selection and Validation

### I chose different models to see which one performed the best and chose Mean Absolute Error (MAE) and R² to track their performances.

### Step 7: Cross-validation and Hyperparameter Optimization

##### Then did cross_validation() and hyperparameter_search() to make sure the model is not overfitting and performing well and to find the best parameters for a model to optimize its performance.

### Step 8: Final Training

#### Trained the whole data after making sure that the model is working well.

## Results

### 1. I chose Random Forest because it had a lower MAE (MAE: 10.01) and a higher R² (R²: 0.98), which showed good ability to explain variance in the data.
### 2. After performing cross-validation and hyperparameter search, the best cross-validation score was: "0.94" for the training set and "0.981" for the test set, indicating the model is performing well on both the training and unseen test data, demonstrating good generalization and consistent hyperparameters.

## Challenges
#### 1. Loading JSON files correctly.
#### 2. Understanding what is and what to do with the tags column.
#### 3. Deciding how to encode the categorical columns and what to do with them, to not have too many columns.

## Future Goals
#### -Making a functions_variables file.
#### -Trying more features and more complex categorical groups.
