import pandas as pd

# File path of the Excel file
file_path = r'C:\Users\Администратор\PycharmProjects\pythonProject9\ganteli.xlsx'

# Sheet name to read
sheet_name = 'Лист1'

# Read Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the data in the DataFrame
print(df)

# User input prompt to request information based on ID
while True:
    request = input("Enter id (or 'q' to quit): ")
    if request.lower() == 'q':
        break
    else:
        try:
            id = int(request)
            result = df[df['id'] == id]
            if result.empty:
                print("id not found.")
            else:
                print(result)
        except ValueError:
            print("Invalid input. Please enter a valid integer id.")
        except Exception as e:
            print("Error:", e)
