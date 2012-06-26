import yaml
from datetime import datetime
import random

y = yaml.load(open("hope9.yaml"))

room_offset = {}
room_offset["Dennis"] = 300
room_offset["Sassaman"] = 600
room_offset["Nutt"] = 900

min_time = 1e10
max_time = -1e10

width = 300
height = 100

for s in y["schedule"]:
	min_time = min(s["start"], min_time)
	max_time = max(s["end"], max_time)

t = min_time

while t < max_time:
	print "<div style=\"position: absolute; left: 0; top: %d; height: %d; width: %d; background-color: #%06x\">%s</div>" % ((t - min_time) / 50 + height, height, width, random.randint(0, 256*256*256), datetime.fromtimestamp(t))
	t += 60*60

def print_room(room):
	print "<div style=\"position: absolute; left: %d; top: 0; height: %d; width: %d; background-color: #%06x\">%s</div>" % (room_offset[room], height, width, random.randint(0, 256*256*256), room)

print_room("Dennis")
print_room("Sassaman")
print_room("Nutt")

for s in y["schedule"]:
	print "<div style=\"position: absolute; left: %d; top: %d; height: %d; width: %d; background-color: #%06x\">%s</div>" % (room_offset[s["room"]], (s["start"] - min_time) / 50 + height, height, width, random.randint(0, 256*256*256), s["title"])


