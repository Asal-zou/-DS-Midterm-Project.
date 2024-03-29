def encode_tags(df):

    """Use this function to manually encode tags from each sale.
    You could also provide another argument to filter out low 
    counts of tags to keep cardinality to a minimum.
       
    Args:
        pandas.DataFrame

    Returns:
        pandas.DataFrame: modified with encoded tags
    """
    tags = df["tags"].tolist()
    # create a unique list of tags and then create a new column for each tag
        
    return df


# Importing necessary libraries
import os
import json

def flatten_dict(d, parent_key='', sep='_'):
    """Flatten nested dictionaries."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # Example handling for lists: store the length of the list
            items.append((new_key, len(v)))
        else:
            items.append((new_key, v))
    return dict(items)

def load_and_flatten_json(directory):
    """Loading JSON files from a directory, flatten their structure, and add filename info."""
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            parts = filename.replace('.json', '').split('_')
            state, city, sequence = parts[0], '_'.join(parts[1:-1]), parts[-1]
            
            file_path = os.path.join(directory, filename)
            with open(file_path) as f:
                data = json.load(f)
                if 'data' in data and 'results' in data['data']:
                    for sale in data['data']['results']:
                        flat_sale = flatten_dict(sale)
                        flat_sale['state'] = state
                        flat_sale['city'] = city
                        flat_sale['sequence'] = sequence
                        data_list.append(flat_sale)
    return data_list




def find_duplicate_rows(df):
    """Find and return duplicate rows in the DataFrame."""
    duplicates = df.duplicated(keep=False)
    duplicate_rows = df[duplicates]
    return duplicate_rows


def find_columns_with_all_nulls(df):
    """Identify and return columns that contain only null values."""
    columns_with_all_nulls = df.isnull().all()[df.isnull().all()].index.tolist()
    return columns_with_all_nulls



def drop_columns_with_many_nulls(df, threshold_percentage=60):
    """Drop columns from a DataFrame where the percentage of missing values exceeds a specified threshold."""
    threshold = len(df) * (threshold_percentage / 100.0)
    return df.dropna(thresh=threshold, axis=1)


def drop_specified_columns(df, columns_to_drop):
    """
    Drops specified columns from a DataFrame.

    Parameters:
    - df: pandas.DataFrame from which columns will be dropped.
    - columns_to_drop: List of column names to be dropped.

    Returns:
    - DataFrame with specified columns dropped.
    """
    
    columns_to_drop = [col for col in columns_to_drop if col in df.columns]
    
    # Drop the columns
    return df.drop(columns=columns_to_drop)



import pandas as pd

def convert_to_datetime(df, columns, datetime_format='ISO8601'):
    """
    Converts specified columns of a DataFrame to datetime objects using a given format.
    
    Parameters:
    - df: The DataFrame containing the columns.
    - columns: A list of column names to convert.
    - datetime_format: The format string or 'ISO8601' for ISO8601 format. Default is 'ISO8601'.
    
    Returns:
    - The DataFrame with the columns converted to datetime.
    """
    for col in columns:
        df[col] = pd.to_datetime(df[col], format=datetime_format, errors='coerce')
    return df

def normalize_timezone(df, columns):
    """
    Normalizes the timezone of datetime columns to UTC and removes timezone information, 
    making them timezone-naive.
    
    Parameters:
    - df: The DataFrame containing the columns.
    - columns: A list of column names to normalize timezone for.
    
    Returns:
    - The DataFrame with timezone-normalized columns.
    """
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.tz_localize(None)
    return df

def extract_date_component(df, columns):
    """
    Extracts the date component from datetime columns, discarding time information.
    
    Parameters:
    - df: The DataFrame containing the columns.
    - columns: A list of column names to extract the date component from.
    
    Returns:
    - The DataFrame with the columns reduced to their date components.
    """
    for col in columns:
        df[col] = df[col].dt.date
    return df


def get_columns_to_drop(df, columns_to_keep):
    """
    Identifies columns to drop from a DataFrame based on the columns to keep.

    Parameters:
    - df: pandas.DataFrame to evaluate.
    - columns_to_keep: List of column names to keep.

    Returns:
    - List of column names to drop.
    """
    return [col for col in df.columns if col not in columns_to_keep]
