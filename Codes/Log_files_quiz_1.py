#We're using the same syslog, and we want to display the date, time, and process id that's 
# inside the square brackets. We can read each line of the syslog and pass the contents to the show_time_of_pid function. 
# Fill in the gaps to extract the date, time, 
#and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.

import re
def show_time_of_pid(line):
  pattern = r"(^.*) computer.*\[(\d+)\]"
  result = re.search(pattern, line)
  print(result.group(0))
  print(result.group(1))
  print(result.group(2))
  print(result)
  print(result[0])
  print(result[1])
  print(result[2])
  return "{} pid:{}".format(result.group(1), result.group(2))

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440