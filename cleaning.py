import matplotlib.pyplot as plt
import pandas as pd
#import for QQ plots?
import scipy.stats as stats

#Import as Pandas Dataframe on this line?: 
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove rows will null values: 
loansData.dropna(inplace=True)


#Generate a Box Plot: 
#loansData.boxplot(column='Amount.Funded.By.Investors')
loansData.boxplot(column='Amount.Requested')
return_type ='dict'
plt.show()


# Generate a Histogram: 
#loansData.hist(column='Amount.Funded.By.Investors')
loansData.hist(column='Amount.Requested')
plt.show()

# Generate QQ Plot: 
plt.figure()
#graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()

