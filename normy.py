from typing import List, Any

import dateutil.parser
import re
from datetime import datetime, timedelta
from pytz import timezone


# Open File
def ouvrir(timeadj):
    mctimepattern = '[\d]{4}-[\d]{1,2}-[\d]{1,2}\s+[\d]{1,2}:[\d]{1,2}:[\d]{1,2}[\,\.][\d]{1,3}'
    with open('mcmr31188.txt') as f:
        lines = f.readlines()
        mctimestamp: list[Any] = re.findall(mctimepattern, str(lines))  # mobicontrol log timestamp format
        mcmsg = re.findall(r'\b\|.*$', str(lines))
        # time conversion
        for mem1 in mctimestamp:
            oldhr = (re.findall(r'\s+[\d]{1,2}', mem1)[0]).strip()
            newhr = int(oldhr) + timeadj
            print(re.sub(r'\s+[\d]{1,2}:', ' ' + str(newhr) + ":", str(mem1)))
            print('---')


# Dissect timestamp
# e.g. 2021-08-30 16:34:54,560
# e.g. yr, mth, day, hr, min, sec, msec

def getDateStr():
    dtStr = "blah blah blagg 2021-08-30 16:59:28.634Not a single message has been shown on net.soti.mobicont."
    diss2 = re.findall(r'[\d]{4}-[\d]{1,2}-[\d]{1,2}\s+[\d]{1,2}:', dtStr)
    for dat2 in diss2:
        print(dat2)


def convertTime():
    timeFormat = '%Y-%m-%d %H:%M:%S %Z%z'
    now = datetime.now().strftime(timeFormat)
    print(now)


ouvrir(4)
# getDateStr()
# convertTime()
