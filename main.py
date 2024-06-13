import pandas as pd
import random
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("medium_data.csv")

df.head()


mean=statistics.mean(df["reading_time"])
median=statistics.median(df["reading_time"])
mode=statistics.mode(df["reading_time"])
stdev=statistics.stdev(df["reading_time"])

print("MEAN : ",mean)
print("MEDIAN : ",median)
print("MODE : ",mode)
print("STANDARD DEVIATION : ",stdev)

sample=[]
reading_time=df["reading_time"].tolist()
for i in range (100):
  index=random.randint(0,len(reading_time)-1)
  sample.append(reading_time[index])


mean=statistics.mean(sample)
median=statistics.median(sample)
mode=statistics.mode(sample)
stdev=statistics.stdev(sample)

print("MEAN : ",mean)
print("MEDIAN : ",median)
print("MODE : ",mode)
print("STANDARD DEVIATION : ",stdev)

fig1=ff.create_distplot([sample],["SAMPLE"],show_hist=False)
fig1.show()


sampled_data=[]
for i in range(1000):
  sample=[]
  for i in range (100):
      index=random.randint(0,len(reading_time)-1)
      sample.append(reading_time[index])

  sampled_data.append(statistics.mean(sample))

mean=statistics.mean(sampled_data)
median=statistics.median(sampled_data)
mode=statistics.mode(sampled_data)
stdev=statistics.stdev(sampled_data)

print("MEAN : ",mean)
print("MEDIAN : ",median)
print("MODE : ",mode)
print("STANDARD DEVIATION : ",stdev)

fig=ff.create_distplot([sampled_data],["SAMPLED MEAN"],show_hist=False)
fig.show()