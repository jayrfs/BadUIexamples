# please do not abuse!
from csv import reader
import requests, time

with open('names.csv', 'r') as names_but_in_csv:
    names_but_as_reader = reader(names_but_in_csv)
    names_but_as_list = list(names_but_as_reader)

for person in names_but_as_list[1:]:
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"persons/{person[0]} {person[1]}.jpg", 'wb') as f:
            f.write(response.content)
    time.sleep(2)
    print(person)