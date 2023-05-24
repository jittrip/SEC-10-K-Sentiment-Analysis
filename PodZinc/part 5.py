import pandas as pd
from datetime import datetime
from datetime import timedelta
import ref_data as edgar_data

#USE THIS VERSION IF YOU GET DATE TYPE ERRORS OF IT NOT FITTING IN FORMAT. 
#THIS VERSION IS WITH DATE FORMATTED WITH xxxx-xx-xx
#PRINT TO DATE IN SECOND ITERATION TO FIND OUT WHICH

def joined_data(document_sentiments_input, output_file, ticker):
    dfbase=None
    dfadd_on=None
    df=pd.read_csv(document_sentiments_input)
    #print(df)
    #dfticker=pd.read_csv('C:\Users\Kevin\python\PodZinc-Part1-Production\Production\SP100.xlsx')
    #s=(get_sp100())
    #print(s)
    #ticker.remove('BRK.B')
    for index,a in enumerate(ticker):
        #print(a)
        df2=df[(df == a).any(axis=1)]
        print(df2)
        filing_date_list=(df2['FilingDate'].to_list())
        #companies=(df2['Symbol'].to_list())
        #print(companies)
        company=ticker[index]
        company_in_list=[]
        company_in_list.append(company)
        #print(filing_date_list)
        for i,date in enumerate(filing_date_list):
            #print(date)
            ending_date=datetime.strptime(date,"%Y-%m-%d")+timedelta(days=20)
            ending_date_str=str(ending_date)
            split=ending_date_str.split()
            end_date=split[0]
            #print(company)
            # print(date)
            # print(end_date)
            # print(company[0])
            yahoo_data=edgar_data.get_yahoo_data(date,end_date, company_in_list)
            resetted_yahoo_data=yahoo_data.reset_index()
            #display(resetted_yahoo_data)
            #display(yahoo_data)
            words_row=df2.iloc[i]
            #print(words_row)
            worddf=pd.DataFrame(words_row)
            transposed=worddf.transpose()
            #display(transposed)
            concatteddf=pd.merge(resetted_yahoo_data, transposed, on = 'Symbol', how='left')
            #display(concatteddf)
            dfbase=pd.concat([dfbase,concatteddf], axis=0)
    #display(dfbase)
    dfbase.to_csv(output_file, index=False)

joined_data('C:\\Users\\Kevin\\python\\export_csv_folder\\sentiment_factorsss.csv','C:\\Users\\Kevin\\python\\final_export_csv_folder\\final_sentimentsss.csv' , ['AMD','AAPL'])
#print(edgar_data.get_sp100())