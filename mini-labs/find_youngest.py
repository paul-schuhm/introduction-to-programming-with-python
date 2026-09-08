from datetime import datetime


# Input data {name: "YYYY-MM-DD"}
group = {
    "Alice": "1995-04-12",
    "Bob": "2002-11-23",
    "Charlie": "1988-08-05",
    "Frank": "2011-09-01",
    "Grace": "1975-03-20"
}

youngest_name = None
youngest_date = None

for name, date_str in group.items():
    # Convert string to datetime object (strptime(): string "p"arsing time)
    birth_date = datetime.strptime(date_str, "%Y-%m-%d")
    if youngest_date is None or birth_date > youngest_date:
        youngest_name = name
        youngest_date = birth_date

print(f"The youngest person is {youngest_name}, born on {youngest_date.strftime('%Y-%m-%d')}.")