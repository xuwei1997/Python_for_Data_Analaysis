import json
import  numpy as np
import  pandas as np
from  pandas import  DataFrame,Series

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return (counts)

path = 'E:\\pydata-book-master\\ch02\\usagov_bitly_data2012-03-16-1331923249.txt'
with open(path , 'r') as f:
    data0=[json.loads(line) for line in f]
time_zones = [rec['tz'] for rec in data0 if 'tz' in rec]
counts=get_counts(time_zones)
print(counts)
print(len(time_zones))

