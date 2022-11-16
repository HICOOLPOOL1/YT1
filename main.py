from datetime import      datetime
from pytz import      timezone
 
tz = timezone("US/Eastern")
Hi = 0
while Hi < 10:
  date  = datetime.now(tz)
  print("Current date and time: ")
  print(date.strftime("%Y-  %m-%d %H:%M:%S"))
Hi = Hi + 1

  