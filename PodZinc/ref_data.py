def get_sp100():

    '''
    Returns list of SP100 tickers as strings

    PATH OF SP100 MUST BE UPDATED PER USER
    HARD-CODED
    '''
    
    import pandas as pd

    ticker_list = []

    SP100 = pd.read_excel('C:\\Users\\Kevin\\python\\PodZinc-Part1-Production\\Production\\SP100.xlsx')

    for x in SP100:

        ticker_list = SP100['Symbol'].unique().tolist()

    return ticker_list



#3b
def get_yahoo_data(start_date, end_date, tickers):

    '''
    Creates a dataframe of yahoo financials data from SP100 companies
    Requires tickers specified from get_sp100()
    
    '''

    import pandas as pd
    import yfinance as yf

    final_df = pd.DataFrame()

    for i, ticker in enumerate(tickers):
        df_yahoo = yf.download(tickers[i],
        start= start_date,
        end= end_date,
        progress=False,
        group_by = tickers)
        df = pd.DataFrame(df_yahoo)

        df = df.rename(columns={'Adj Close': 'Price'})  ##df.pop to remove columns
        df = df.reindex(columns=['High', 'Low','Price', 'Volume'])
        df['1daily_returns'] = df['Price'].pct_change(1)
        df['2daily_returns'] = df['Price'].pct_change(2)
        df['3daily_returns'] = df['Price'].pct_change(3)
        df['5daily_returns'] = df['Price'].pct_change(5)
        df['10daily_returns'] = df['Price'].pct_change(10)
        df['Symbol'] = tickers[i]

        #df = df.fillna(0)

        final_df = pd.concat([final_df, df], axis=0)


    return final_df

#3c

def get_sentiment_word_dict():

    '''
    Returns a dictionary containing the LM sentiment words.
    The keys for the dictionary are the sentiments, and the values will be a list of words associated with that particular sentiment.
    For example, get_sentiment_word_dict()[‘Negative’] will return a list of words associated with negative sentiment.

    PATH OF filelms MUST BE UPDATED PER USER
    HARD-CODED
    '''

    import pandas as pd

    sentiment_list  = ['Negative', 'Positive', 'Uncertainty','Litigious','Strong_Modal','Weak_Modal', 'Constraining']


    sentiment_dict = {}

    for word in sentiment_list:
         sentiment_dict[word] = []

    filelms = pd.read_csv('C:\\Users\\Kevin\\python\\PodZinc-Part1-Production\\Production\\LM master dict.csv')
    
    for word in sentiment_list:
        column = filelms[word]

        for x in range(len(column)):
            if column.iloc[x] != 0:
                sentiment_dict[word].append(filelms['Word'].iloc[x])
    
    return sentiment_dict

# #3a
# def get_sp100():

#     '''
#     Returns list of SP100 tickers as strings

#     PATH OF SP100 MUST BE UPDATED PER USER
#     HARD-CODED
#     '''
    
#     import pandas as pd

#     ticker_list = []

#     SP100 = pd.read_excel('C:\\Users\\Kevin\\python\\PodZinc\\SP100.xlsx')

#     for x in SP100:

#         ticker_list = SP100['Symbol'].unique().tolist()
    
#     return ticker_list



# #3b
# def get_yahoo_data(start_date, end_date, tickers):

#     '''
#     Creates a dataframe of yahoo financials data from SP100 companies
#     Requires tickers specified from get_sp100()
    
#     '''

#     import pandas as pd
#     import yfinance as yf

#     final_df = pd.DataFrame()

#     for i, ticker in enumerate(tickers):
#         df_yahoo = yf.download(tickers[i],
#         start= start_date,
#         end= end_date,
#         progress=False,
#         group_by = tickers)
#         df = pd.DataFrame(df_yahoo)

#         df = df.rename(columns={'Adj Close': 'Price'})  ##df.pop to remove columns
#         df = df.reindex(columns=['High', 'Low','Price', 'Volume'])
#         df['1daily_returns'] = df['Price'].pct_change(1)
#         df['2daily_returns'] = df['Price'].pct_change(2)
#         df['3daily_returns'] = df['Price'].pct_change(3)
#         df['5daily_returns'] = df['Price'].pct_change(5)
#         df['10daily_returns'] = df['Price'].pct_change(10)
#         df['Symbol'] = tickers[i]

#         #df = df.fillna(0)

#         final_df = pd.concat([final_df, df], axis=0)


#     return final_df

# #3c

# def get_sentiment_word_dict():

#     '''
#     Returns a dictionary containing the LM sentiment words.
#     The keys for the dictionary are the sentiments, and the values will be a list of words associated with that particular sentiment.
#     For example, get_sentiment_word_dict()[‘Negative’] will return a list of words associated with negative sentiment.

#     PATH OF filelms MUST BE UPDATED PER USER
#     HARD-CODED
#     '''

#     import pandas as pd

#     sentiment_list  = ['Negative', 'Positive', 'Uncertainty','Litigious','Strong_Modal','Weak_Modal', 'Constraining']


#     sentiment_dict = {}

#     for word in sentiment_list:
#          sentiment_dict[word] = []

#     filelms = pd.read_csv('C:\\Users\\\Kevin\\python\\part3\\LM master dict.csv')
    
#     for word in sentiment_list:
#         column = filelms[word]

#         for x in range(len(column)):
#             if column.iloc[x] != 0:
#                 sentiment_dict[word].append(filelms['Word'].iloc[x])
    
#     return sentiment_dict