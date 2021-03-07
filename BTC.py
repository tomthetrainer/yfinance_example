import yfinance as yf

####
# yfinance is a python library to grab yahoo finance data
# You probably need to install it
# pip install yfinance
####


####
# Create a ticker object
#####
BTC = yf.Ticker('BTC-USD')

###
# One method available is to print basic info
###

# print(BTC.info)

#####
## To Grab ticker info use history
#######

ticker_history  =  BTC.history(start="2020-01-01",  end="2021-01-01")
print(ticker_history.head())
