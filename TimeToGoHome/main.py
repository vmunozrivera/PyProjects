# Time to go home
# This script calculate the time to stop working and go home

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_h = now.strftime("%H")
current_m = now.strftime("%M")

if int(current_h) >= 19 and int(current_m) >= 0:
    print('Time to go HOME!')
else:
    time_left_h = 18 - int(current_h)
    time_left_m = 59 - int(current_m)
    print(f'Time left to go home ----- Hrs: {time_left_h} | Min: {time_left_m}')
