import pandas as pd
import re

def remove_comments_and_whitespace(code_snippet, language):
    # Define regex patterns for Python and Java comments
    if language == 'Python':
        # Remove Python comments (single-line and multi-line)
        code_snippet = re.sub(r'(?s)#.*?\n|\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"', '', code_snippet)
    elif language == 'Java':
        # Remove Java comments (single-line and multi-line)
        code_snippet = re.sub(r'(?s)//.*?\n|/\*.*?\*/', '', code_snippet)

    # Remove unnecessary extra whitespaces
    # Remove leading/trailing whitespaces and reduce multiple spaces/newlines to a single space/newline
    code_snippet = re.sub(r'\n\s*\n', '\n', code_snippet).strip()

    return code_snippet

def process_csv_files(file_paths):
    for file_path in file_paths:
        # Identify the language based on the file name
        if 'python' in file_path.lower():
            language = 'Python'
        elif 'java' in file_path.lower():
            language = 'Java'
        else:
            print(f"Unknown language for file: {file_path}. Skipping.")
            continue

        # Load the CSV into a dataframe
        df = pd.read_csv(file_path)

        # Process each code snippet to remove comments and extra whitespaces
        df['code_snippet'] = df['code_snippet'].apply(lambda x: remove_comments_and_whitespace(x, language))

        # Save the cleaned dataframe back to the CSV
        df.to_csv(file_path, index=False)

        print(f"Processed and cleaned {file_path}.")

# Example usage:
csv_files = ['python_output.csv', 'java_output.csv']  # Replace with actual CSV file paths
process_csv_files(csv_files)
