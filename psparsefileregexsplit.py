"""demo for the regex split"""

import re

for line in open('listing.dat'):
    temp = re.split('\ +', line)
    print(temp[3:5])