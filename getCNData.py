# import os
# import pandas as pd
# import json

# def concatenate_files_by_folder(base_path):
#     # Dictionary to hold dataframes for each folder
#     folder_dfs = {}

#     # List of target folders
#     folders = ['Java', 'Python']  # Add more folder names if needed

#     # Loop through each folder in the base path
#     for folder in folders:
#         folder_path = os.path.join(base_path, folder)

#         # Only process if folder exists
#         if os.path.exists(folder_path) and os.path.isdir(folder_path):
#             # List to store content for this folder
#             data_list = []

#             # Loop through each file in the folder
#             for filename in os.listdir(folder_path):
#                 if filename.endswith('.py') or filename.endswith('.java'):  # Customize the file extensions
#                     file_path = os.path.join(folder_path, filename)

#                     # Read the content of each file
#                     with open(file_path, 'r') as file:
#                         file_content = file.read()

#                     # Append filename and content to the list
#                     data_list.append({"filename": filename, "content": file_content})

#             # Store the data as a dataframe
#             df = pd.DataFrame(data_list)

#             # Store the dataframe in the dictionary with the folder name as the key
#             folder_dfs[f'{folder.lower()}_df'] = df

#     return folder_dfs


# # Example usage:
# base_path = 'path'  # Replace with the correct base folder path
# folder_dataframes = concatenate_files_by_folder(base_path)

# # Separate the JSON files for each folder
# for df_name, df in folder_dataframes.items():
#     # Save each dataframe as a separate JSON file
#     output_filename = f'{df_name.replace("_df", "")}_output.json'
#     combined_data = df.to_dict(orient='records')
    
#     # Save the JSON array to file
#     with open(output_filename, 'w') as json_file:
#         json.dump(combined_data, json_file, indent=4)

# print("JSON files for each folder have been created.")

import os
import pandas as pd

def concatenate_files_by_folder(base_path):
    # Dictionary to hold dataframes for each folder
    folder_dfs = {}

    # List of target folders
    folders = ['Java', 'Python']  # Add more folder names if needed

    # Loop through each folder in the base path
    for folder in folders:
        folder_path = os.path.join(base_path, folder)

        # Only process if folder exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # List to store content for this folder
            data_list = []

            # Loop through each file in the folder
            for idx, filename in enumerate(os.listdir(folder_path)):
                if (folder == 'Python' and filename.endswith('.py')) or (folder == 'Java' and filename.endswith('.java')):  
                    file_path = os.path.join(folder_path, filename)

                    # Read the content of each file
                    with open(file_path, 'r') as file:
                        file_content = file.read()

                    # Append unique ID and content to the list
                    data_list.append({"id": idx + 1, "code_snippet": file_content})

            # Store the data as a dataframe
            df = pd.DataFrame(data_list)

            # Store the dataframe in the dictionary with the folder name as the key
            folder_dfs[f'{folder.lower()}_df'] = df

    return folder_dfs


# Example usage:
base_path = 'path'  # Replace with the correct base folder path
folder_dataframes = concatenate_files_by_folder(base_path)

# Save each dataframe as a CSV file
for df_name, df in folder_dataframes.items():
    output_filename = f'{df_name.replace("_df", "")}_output.csv'
    
    # Save the dataframe as a CSV file
    df.to_csv(output_filename, index=False)

print("CSV files for each folder have been created.")

