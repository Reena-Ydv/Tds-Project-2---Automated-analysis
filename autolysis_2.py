# -*- coding: utf-8 -*-
"""autolysis_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1goAPGP9k0OmPEOxBFImz-zkZehahMzXQ
"""



import sys
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import geopandas as gpd
import networkx as nx





os.environ["API_KEY"] = ("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjEwMDE5ODFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.yVytEJB5w0iOk2ijlLKbx2ieRlIbmzuC_QYl2c4EAuU")

api_key = os.getenv("API_KEY")  # Access the API key



# Function to make an API request using the API key
def make_api_request(api_url):
    api_key = os.getenv("API_KEY")  # Get API key from environment variable
    if api_key is None:
        print("API key is missing!")
        return None

    headers = {
        'Authorization': f'Bearer {api_key}'  # Use API key in the headers
    }

# Example usage
api_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"  # Replace with the actual API URL
response_data = make_api_request(api_url)

if response_data:
    print("API Response:", response_data)



# Detect encoding of CSV file
def detect_encoding(file_path):
    try:
        # Try reading with UTF-8
        df = pd.read_csv(file_path, encoding='utf-8')
        return df
    except UnicodeDecodeError:
        # If decoding fails, try ISO-8859-1 (latin1)
        print("File encoded with ISO-8859-1")
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        return df

def load_data(file_path):
    # Try to detect file encoding and load the data
    data = detect_encoding(file_path)

    # Show basic info
    info = data.info()
    summary = data.describe()
    missing_values = data.isnull().sum()

    return data, summary, missing_values

# Handle missing values
def handle_missing_values(data):
    # Fill missing numerical data with mean and categorical with mode
    for column in data.select_dtypes(include=[np.number]).columns:
        data[column].fillna(data[column].mean(), inplace=True)

    for column in data.select_dtypes(include=[object]).columns:
        data[column].fillna(data[column].mode()[0], inplace=True)

    return data

# Encode categorical variables
def encode_categorical_data(data):
    label_encoders = {}
    for column in data.select_dtypes(include=[object]).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data, label_encoders

# Outlier detection and treatment
def handle_outliers(data):
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        z_scores = np.abs(stats.zscore(data[column]))
        data[column] = np.where(z_scores > 3, np.nan, data[column])  # Replace outliers with NaN
    data.fillna(data.mean(), inplace=True)  # Replace NaNs (outliers) with column mean
    return data

# Generic data analysis functions
def analyze_data(data):
    # Correlation Analysis
    correlation_matrix = data.corr()

    # PCA for dimensionality reduction
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data[numeric_columns].dropna())

    # Clustering using KMeans
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(data[numeric_columns].dropna())

    return correlation_matrix, pca_result, clusters

# Plot data and generate visualizations
def plot_data(data, correlation_matrix, pca_result, clusters):
    # Missing Values Heatmap
    plt.figure(figsize=(10, 7))
    sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values Heatmap")
    plt.savefig("missing_values.png")

    # Correlation Heatmap
    plt.figure(figsize=(10, 7))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.savefig("correlation_matrix.png")

    # PCA Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis')
    plt.title("PCA Analysis")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.savefig("pca_plot.png")

# Time Series Analysis (if time-related column exists)
def time_series_analysis(data):
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        data.set_index('date', inplace=True)
        resampled_data = data.resample('M').mean()  # Monthly resampling
        plt.figure(figsize=(10, 6))
        plt.plot(resampled_data)
        plt.title("Time Series Analysis")
        plt.savefig("time_series.png")
        return resampled_data
    else:
        print("No date column found for time series analysis.")
        return None

# Geographic Analysis (if geographic columns like 'latitude' and 'longitude' exist)
def geographic_analysis(data):
    if 'latitude' in data.columns and 'longitude' in data.columns:
        gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude))
        gdf.plot(marker='o', color='red', markersize=5)
        plt.title("Geographic Analysis")
        plt.savefig("geographic_analysis.png")
        return gdf
    else:
        print("No geographic data (latitude/longitude) found.")
        return None

# Network Analysis (if columns like 'source' and 'target' exist)
def network_analysis(data):
    if 'source' in data.columns and 'target' in data.columns:
        G = nx.from_pandas_edgelist(data, 'source', 'target')
        nx.draw(G, with_labels=True, node_size=700, node_color='skyblue')
        plt.title("Network Analysis")
        plt.savefig("network_analysis.png")
        return G
    else:
        print("No network data (source/target) found.")
        return None

# Generate summary report (Markdown)
def generate_markdown_report(correlation_matrix, pca_result, clusters, time_series, geographic, network):
    markdown = """
    # Automated Data Analysis Report

    ## Correlation Matrix
    The correlation matrix is shown below, displaying relationships between numerical features.
    """
    markdown += correlation_matrix.to_markdown() + "\n"

    markdown += "\n## PCA Analysis\n\n"
    markdown += "The PCA plot is visualized as the first two components representing the data in reduced dimensions.\n"

    markdown += "\n## Clustering (KMeans)\n\n"
    markdown += f"Clustering identified {len(set(clusters))} clusters in the dataset.\n"

    if time_series is not None:
        markdown += "\n## Time Series Analysis\n\n"
        markdown += "Time series trends have been analyzed and plotted over time.\n"

    if geographic is not None:
        markdown += "\n## Geographic Analysis\n\n"
        markdown += "Geographic data has been visualized on a map.\n"

    if network is not None:
        markdown += "\n## Network Analysis\n\n"
        markdown += "A network analysis of relationships between entities has been conducted.\n"

    return markdown

# Main function to run the analysis
def main(file_path):
    # Load and prepare the data
    data, summary, missing_values = load_data(file_path)

    # Handle missing values
    data = handle_missing_values(data)

    # Handle outliers
    data = handle_outliers(data)

    # Encode categorical variables
    data, label_encoders = encode_categorical_data(data)

    # Analyze data
    correlation_matrix, pca_result, clusters = analyze_data(data)

    # Perform additional analyses
    time_series = time_series_analysis(data)
    geographic = geographic_analysis(data)
    network = network_analysis(data)

    # Plot and save visualizations
    plot_data(data, correlation_matrix, pca_result, clusters)

    # Generate markdown report
    markdown = generate_markdown_report(correlation_matrix, pca_result, clusters, time_series, geographic, network)

    # Save Markdown report
    with open("README.md", "w") as file:
        file.write(markdown)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
    else:
        main(sys.argv[1])