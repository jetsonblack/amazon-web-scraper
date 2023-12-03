import pandas as pd

def remove_duplicates(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicate rows based on all columns
    df_no_duplicates = df.drop_duplicates()

    # Write the DataFrame without duplicates to a new CSV file
    df_no_duplicates.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Replace 'input.csv' and 'output.csv' with your file names
    input_file = 'amazon_review_scrape.csv'
    output_file = 'output.csv'

    remove_duplicates(input_file, output_file)
    print(f"Duplicate rows removed. Result saved to {output_file}")
