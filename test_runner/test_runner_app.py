from datetime import date

current_date = date.today()

# Convert the current date to a string in the MM/DD/YYYY format
formatted_date = current_date.strftime("%m/%d/%Y")
print(formatted_date)
