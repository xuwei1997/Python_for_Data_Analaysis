import json
import  numpy as np
import  pandas as pd
import matplotlib.pyplot as plt

from  pandas import  DataFrame,Series

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return (counts)

if __name__ == '__main__':
    # 输入文件路径，注意\用\\转义
    path = 'E:\\pydata-book-master\\ch02\\usagov_bitly_data2012-03-16-1331923249.txt'

    #打开文件
    with open(path , 'r') as f:
       data0=[json.loads(line) for line in f]
    time_zones = [rec['tz'] for rec in data0 if 'tz' in rec]
    counts=get_counts(time_zones)
    print(counts)
    print(len(time_zones))


    frame = DataFrame(data0)
    print(frame['tz'].value_counts())
    clean_tz = frame['tz'].fillna("Missing")
    clean_tz[clean_tz == ''] =  'Unkown'
    tz_counts=clean_tz.value_counts()
#    print(tz_counts)
    tz_counts[:10].plot(kind='barh',rot=0)
    plt.show()

    # dropna方法删除缺失数据,x.split()按空格切割字符串
    results= Series([x.split()[0]  for x in frame.a.dropna()])
#    print(results)
    a_counts=results.value_counts()
#    print(a_counts)
    a_counts[:10].plot(kind='barh',rot=0)
    plt.show()

    cframe=frame[frame.a.notnull()]
    operating_system = Series(np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')) #Series
#    print(operating_system[:5])

    by_tz_os = cframe.groupby(['tz',operating_system])
    agg_couts=by_tz_os.size().unstack().fillna(0)
#    print(agg_couts[:10])

    indexer = agg_couts.sum(1).argsort()
#    print(indexer[:10])
    counts_subset=agg_couts.take(indexer)[-10:]
    print(counts_subset)
    counts_subset.plot(kind='barh',stacked=True)

    normed_subset=counts_subset.div(counts_subset.sum(1),axis=0)
    normed_subset.plot(kind='barh',stacked=True)

    plt.show()
