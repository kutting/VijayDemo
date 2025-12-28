import argparse
import sys
import pandas as pd

def main(csv_file):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Print the first few rows of the DataFrame
        print("First few rows of the dataset:")
        print(df.head())
        
        # Print summary statistics
        print("\nSummary statistics:")
        print(df.describe())
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file}' is empty or invalid.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read a CSV file and print summary statistics.")
    parser.add_argument('csv_file', help='Path to the CSV file')
    args = parser.parse_args()
    
    main(args.csv_file)
    
    # Print summary statistics
    print("\nSummary statistics:")
    print(df.describe())
    
    # Print information about the DataFrame
    print("\nDataFrame info:")
    print(df.info())
if __name__ == "__main__":
    main()

