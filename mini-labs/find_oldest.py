# Find the oldest person in a group.

from datetime import datetime

# Input data {name: "YYYY-MM-DD"}
group = {
    "Alice": "1995-04-12",
    "Bob": "2002-11-23",
    "Charlie": "1988-08-05",
    "Frank": "2011-09-01",
    "Grace": "1975-03-20"
}

oldest_name = None
oldest_date = None

for name, date_str in group.items():
    # Convert string to datetime object (strptime(): string "p"arsing time)
    birth_date = datetime.strptime(date_str, "%Y-%m-%d")
    if oldest_date is None or birth_date < oldest_date:
        oldest_name = name
        oldest_date = birth_date

print(f"The oldest person is {oldest_name}, born on {oldest_date.strftime('%Y-%m-%d')}.")