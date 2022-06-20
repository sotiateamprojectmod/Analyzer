Description:
- Device and server logs may have different timezones. 
- This project aims to make the timezones between log files consistent. 
- As a result, it makes the log merger easy to read and display the log entries in a chronological and orderly manner.


Logic:
- Server logs as time of reference (TOR)
- Read Server logs timestamp
  - Find regex pattern of timestamp for DS and Agent logs
- Check it against


- normy -f mobicontrol.log -s IST -d EST > newfile.txt
  -f = file name
  -s = file name timezone
  -d = target timezone
  -a = adjust
  
- normy -f mobicontrol.log -a +3


- read file
- ignore year
- read "hour" field (regex)
- store into a variable -> "hour"
- add "x" from argument
- print "hour+x"