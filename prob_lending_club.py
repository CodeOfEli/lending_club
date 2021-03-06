import matplotlib.pyplot as plt
import pandas as pd
#import for QQ plots?
import scipy.stats as stats
import collections

#Import as Pandas Dataframe on this line?: 
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove rows will null values: 
loansData.dropna(inplace=True)

#Do Collectinons
# c = collections.Counter(loansData['Amount.Funded.By.Investors'])
# print c


#Generate a Box Plot: 
loansData.boxplot(column='Amount.Requested')
loansData.boxplot(column='Amount.Funded.By.Investors')
return_type ='dict'
plt.show()

# Generate a Histogram: 
loansData.hist(column='Amount.Requested')
loansData.hist(column='Amount.Funded.By.Investors')

plt.show()

# Generate QQ Plot: 
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()


