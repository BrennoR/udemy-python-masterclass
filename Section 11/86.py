## Timezone Challenge ##
import datetime
import pytz

available_zones = {'1': 'Africa/Johannesburg',
                   '2': 'America/Chicago',
                   '3': 'Europe/Bratislava',
                   '4': 'Asia/Omsk',
                   '5': 'Atlantic/Madeira',
                   '6': 'Europe/Skopje',
                   '7': 'Africa/Tripoli',
                   '8': 'Europe/Berlin',
                   '9': 'America/Maceio'}

print("Please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{}. {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
