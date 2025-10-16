#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Preprocessing Script - Linux Compatible
Performs cleaning, normalization, and feature engineering on dataset.csv
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import os


def preprocess_df(df: pd.DataFrame, normalize_method: str = 'standard') -> pd.DataFrame:
    """
    Clean and preprocess a pandas DataFrame.

    Steps:
    - Drop duplicate rows
    - Handle missing values: numeric -> median, categorical -> mode
    - Fix data types by attempting to cast numeric-like columns
    - Normalize/standardize numeric features
    - Feature engineering: create hour_of_day if timestamp exists, and value_diff

    Returns cleaned DataFrame.
    """
    df = df.copy()

    # Drop duplicates
    df = df.drop_duplicates()

    # Try to parse timestamps automatically
    for col in df.columns:
        if df[col].dtype == object:
            try:
                parsed = pd.to_datetime(df[col], errors='coerce')
                if parsed.notna().any():
                    df[col] = parsed
            except Exception:
                pass

    # Handle missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            median = df[col].median()
            df[col] = df[col].fillna(median)
        else:
            mode = df[col].mode()
            if not mode.empty:
                df[col] = df[col].fillna(mode.iloc[0])
            else:
                df[col] = df[col].fillna('')

    # Attempt numeric type casting
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except Exception:
                pass

    # Feature Engineering
    if 'timestamp' in df.columns and pd.api.types.is_datetime64_any_dtype(df['timestamp']):
        df['hour_of_day'] = df['timestamp'].dt.hour

    if 'value' in df.columns and pd.api.types.is_numeric_dtype(df['value']):
        df['value_diff'] = df['value'].diff().fillna(0)

    # Normalization
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_cols:
        if normalize_method == 'standard':
            scaler = StandardScaler()
        else:
            scaler = MinMaxScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df


if __name__ == "__main__":
    # Define file paths
    input_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
    output_path = os.path.join(os.path.dirname(__file__), "cleaned_dataset.csv")

    print("🔹 Reading dataset from:", input_path)

    # Load dataset
    try:
        df = pd.read_csv(input_path)
        print("✅ Original Data:")
        print(df.head())
    except FileNotFoundError:
        print("❌ Error: dataset.csv not found.")
        exit(1)

    # Process data
    cleaned_df = preprocess_df(df, normalize_method='standard')

    print("\n✅ Cleaned and Processed Data:")
    print(cleaned_df.head())

    # Save cleaned data
    cleaned_df.to_csv(output_path, index=False)
    print("\n💾 Cleaned dataset saved to:", output_path)
