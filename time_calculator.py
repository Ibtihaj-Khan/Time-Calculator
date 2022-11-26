def add_time(start, duration, day=None):
  day_indeces = {
    "sunday": 0,
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6
  }
  day_tuple = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

  startHours = int(start.split()[0].split(":")[0])
  startMins = int(start.split()[0].split(":")[1])
  startAMPM = start.split()[1]

  durationHours = int(duration.split()[0].split(":")[0])
  durationMins = int(duration.split()[0].split(":")[1])
  
  normalizedHrs = startHours
  if startAMPM == "PM":
    normalizedHrs = startHours+12

  totalMins = startMins + durationMins
  minsToH = totalMins // 60
  minsRemaining = totalMins % 60

  hrsFinal = normalizedHrs + minsToH + durationHours

  #Total days passed, final calculation for output hours
  #minsRemaining will be mins Place
  total_days_passed = hrsFinal // 24
  ans_hour = (hrsFinal % 24) % 12

  ans_hour_str = str(ans_hour)
  ans_min_str = str(minsRemaining)
  ans_total_days = str(total_days_passed)
  ans_AMPM = "PM"

  if len(ans_min_str) == 1:
    ans_min_str = "0"+ans_min_str

  if int(hrsFinal%24) <= 11: 
    ans_AMPM = "AM"

  if ans_hour_str == "0":
    ans_hour_str = "12"

  if day is None:
    if ans_total_days == "0":
      return "{}:{} {}".format(ans_hour_str, ans_min_str, ans_AMPM)
    if ans_total_days == "1":
      return "{}:{} {} (next day)".format(ans_hour_str, ans_min_str, ans_AMPM)
    else :
      return "{}:{} {} ({} days later)".format(ans_hour_str, ans_min_str, ans_AMPM, ans_total_days)

  else:
    dayIndex = day_indeces.get(day.lower())
    newDay = day_tuple[(dayIndex+int(ans_total_days))%7].capitalize()

    if ans_total_days == "0":
      return "{}:{} {}, {}".format(ans_hour_str, ans_min_str, ans_AMPM, newDay)
    if ans_total_days == "1":
      return "{}:{} {}, {} (next day)".format(ans_hour_str, ans_min_str, ans_AMPM, newDay)
    else :
      return "{}:{} {}, {} ({} days later)".format(ans_hour_str, ans_min_str, ans_AMPM,newDay, ans_total_days)
    