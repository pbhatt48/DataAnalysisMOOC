from os import listdir
from os.path import isfile, join
import re


print re.search('\(([0-9].[0-9].[0-9].([0-9A-Z]+))\)' ,'Split()(4.2.5.1)').group(1)

dir = "./old_resources"
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
counter = 0
for f in onlyfiles:
    print f
    # m = re.search('\([0-9].[0.9].[0-9].[0-9]\)', f).group(1)
    m = re.search('\(([0-9].[0-9].[0-9].[0-9A-Z]+)\)', f).group(1)
    print m
    counter+=1

sorted = sorted([re.search('\(([0-9].[0-9].[0-9].[0-9A-Z]+)\)', i).group(1) for i in onlyfiles])

print sorted

print counter
