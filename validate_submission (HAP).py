import sys
import pandas as pd

def validate(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'candidate_id' not in df.columns:
            print("Error: 'candidate_id' column not found.")
            return False
        if not df['candidate_id'].is_unique:
            print("Error: 'candidate_id' column contains duplicate values.")
            return False
        if df['candidate_id'].isnull().any():
            print("Error: 'candidate_id' column contains null values.")
            return False
        print("Validation successful!")
        return True
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return False
    except Exception as e:
        print(f"Validation failed: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_submission.py <submission_file>")
        sys.exit(1)
    file_to_validate = sys.argv[1]
    validate(file_to_validate)