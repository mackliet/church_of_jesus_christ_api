from church_of_jesus_christ_api import ChurchOfJesusChristAPI
from os import environ
import datetime

username = environ["CHURCH_USERNAME"]
password = environ["CHURCH_PASSWORD"]

api = ChurchOfJesusChristAPI(username, password)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# Same as api.get_birthdays(unit=api.user_details['homeUnits'][0])
birthday_list = api.get_birthdays()

for month in birthday_list:
    for member in month["birthdays"]:
        birthdate = datetime.datetime.strptime(
            member["birthDayFormatted"], "%d %b"
        ).date()
        if birthdate.month == today.month and birthdate.day == today.day:
            print(f"It's {member['spokenName']}'s birthday today!")

            # Use email or phone to automate sending a birthday message here if desired...

# Same as api.get_moved_in(unit=api.user_details['homeUnits'][0])
moved_in_list = api.get_moved_in()

for record in moved_in_list:
    move_date = birthdate = datetime.datetime.strptime(
        record["moveDate"], "%d %b %Y"
    ).date()
    if move_date == yesterday:
        print(f"Records for {record['name']} arrived to the unit yesterday")

        # Use email or phone to automate sending a message to welcome them to the unit...

# Same as api.get_missionary_progress_record(unit=api.user_details['homeUnits'][0])
for record in api.get_missionary_progress_record():
    last_vist_timestamp = (
        int(record["lastVisit"]) / 1000.0
    )  # Convert milliseconds to seconds

    if last_vist_timestamp == 0:
        print(f"No last visit recorded for {record['fullName']}")
        # Tell missionaries to update info for this person...
    else:
        visit_date = datetime.datetime.fromtimestamp(last_vist_timestamp).date()
        if visit_date == yesterday:
            print(f"Missionaries visited {record['fullName']} yesterday")
            # Ask the missionaries how the visit went...
