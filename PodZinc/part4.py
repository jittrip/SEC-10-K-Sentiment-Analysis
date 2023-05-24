import ref_data as edgar_data
import os
import re
import pandas as pd


def write_document_sentiments(input_folder,output_file):
    dfbase=None
    dfadd_on=None
    sentiment_dict= edgar_data.get_sentiment_word_dict()
    #print(sentiment_dict)
    variants_list=None
    sentiment_str=''
    occurances=[]      #print(variants_list)
    for filename in os.listdir(input_folder):
        #print(filename)
        full_path = f'{input_folder}\{filename}'
        #print(full_path)
        cleaned_file=open(full_path,'r', encoding='utf-8')
        cleaned_txt=cleaned_file.read()
        #print(cleaned_txt)
        file_split=str(filename).split('_')
        symbol=file_split[0]
        reporttype=file_split[1]
        filingdate=file_split[2][:-4]
        occurances.append(symbol)
        occurances.append(reporttype)
        occurances.append(filingdate)
        for lists in sentiment_dict:
            variants_list = sentiment_dict[lists]
            #print(lists)
            for words in variants_list:
                #print(words)
                sentiment_str = sentiment_str+f'\\b(?i){words}\\b|'
            sentiment_str_fin=(sentiment_str[:-1])
            sentiment_str=''
        #print(sentiment_str_fin)
    #print(sentiment_str_fin)
            keywords=re.findall(sentiment_str_fin,cleaned_txt, re.DOTALL)
            length=len(keywords)
            keywords=''
            occurances.append(length)
        df=pd.DataFrame([occurances], columns=['Symbol','ReportType','FilingDate','Negative','Positive','Uncertainty','Litigious','Strong_Modal','Weak_Modal', 'Constraining'])
        #print(df)
        dfadd_on=df
        base=pd.concat([dfbase,dfadd_on], axis=0)
        #print(base)
        dfbase=base
        occurances=[]
        # print(dfbase)
        #print(aggregate_occurance)
        # print(keywords)
        # print(variants_list)
    dfbase.to_csv(output_file, index=False)
    # for i in variants_list:
    #     sentiment_str = sentiment_str +rf'\b(?i){i}\b|'
    #     sentiment_str_fin=(sentiment_str[:-1])
    #     keywords=re.findall(sentiment_str_fin,cleaned_txt, re.DOTALL)
    #     #print(keywords)
    # print(sentiment_str_fin)
        #Take off final | from string
        #when word exists in doc
        #add one to counter
        #append each word counter to sentiment counter
        #put sentiment counter as column in csv

#keywords=re.findall(r'\bnegative\b|\bpositive\b|\buncertainty\b|\blitigious\b|\bconstraining\b|\bsuperfluous\b|\bmodal\b', cleaned_txt,re.DOTALL)

write_document_sentiments('C:\\Users\\Kevin\\python\\cleaned_files_beta', 'C:\\Users\\Kevin\\python\\export_csv_folder\\test.csv')


# import os
# import re
# import pandas as pd
# import ref_data as edgar_data

# #NEEDS TO RUN PART 3A,3B,3C TO FULLY FUNCTION

# def write_document_sentiments(input_folder,output_file):
#     import ref_data as edgar_data
#     import os
#     import re
#     import pandas as pd

#     dfbase=None
#     dfadd_on=None
#     sentiment_dict= edgar_data.get_sentiment_word_dict()
#     variants_list=None
#     sentiment_str=''
#     occurances=[]

    
#         #print(variants_list)
#     for filename in os.listdir(input_folder):
#         full_path = os.path.join(input_folder,filename)
#         cleaned_file=open(full_path,'r')
#         cleaned_txt=cleaned_file.read()
#         file_split=str(filename).split('_')
#         symbol=file_split[0]
#         reporttype=file_split[1]
#         filingdate=file_split[2][:-4]
#         occurances.append(symbol)
#         occurances.append(reporttype)
#         occurances.append(filingdate)
#         for lists in sentiment_dict:
#             variants_list = sentiment_dict[lists]
#             #print(lists)
#             for words in variants_list:
#                 #print(words)
#                 sentiment_str = sentiment_str+f'\\b(?i){words}\\b|'
#             sentiment_str_fin=(sentiment_str[:-1])
#             sentiment_str=''
#         #print(sentiment_str_fin)
#     #print(sentiment_str_fin)
#             keywords=re.findall(sentiment_str_fin,cleaned_txt, re.DOTALL)
#             length=len(keywords)
#             keywords=''
#             occurances.append(length)
#         df=pd.DataFrame([occurances], columns=['Symbol','ReportType','FilingDate','Negative','Positive','Uncertainty','Litigious','Strong_Modal','Weak_Modal', 'Constraining'])
#         #print(df)
#         dfadd_on=df
#         base=pd.concat([dfbase,dfadd_on], axis=0)
#         #print(base)
#         dfbase=base
#         occurances=[]
#         print(dfbase)
#         #print(aggregate_occurance)
#         # print(keywords)
#         # print(variants_list)
#     dfbase.to_csv(output_file, index=False)
#     # for i in variants_list:
#     #     sentiment_str = sentiment_str +rf'\b(?i){i}\b|'
#     #     sentiment_str_fin=(sentiment_str[:-1])
#     #     keywords=re.findall(sentiment_str_fin,cleaned_txt, re.DOTALL)
#     #     #print(keywords)
#     # print(sentiment_str_fin)
#         #Take off final | from string

#         #when word exists in doc
#         #add one to counter
#         #append each word counter to sentiment counter
#         #put sentiment counter as column in csv

# #keywords=re.findall(r'\bnegative\b|\bpositive\b|\buncertainty\b|\blitigious\b|\bconstraining\b|\bsuperfluous\b|\bmodal\b', cleaned_txt,re.DOTALL)

# write_document_sentiments ('C:\\Users\\Kevin\\python\\cleaned_files_folder', 'C:\\Users\\Kevin\\python\\export_csv_folder\\sentiment_factors.csv')




















#THIS IS FIRST VERSION THAT DOESN'T WORK!!!!!!!!!!!!!!

# # # def write_document_sentiments(input_folder,output_file):
# # #     dfbase=None
# # #     dfadd_on=None
# # #     for filename in os.listdir(input_folder):
# # #         full_path = os.path.join(input_folder,filename)
# # #         cleaned_file=open(full_path,'r')
# # #         cleaned_txt=cleaned_file.read()
# # #         file_split=str(filename).split('_')
# # #         #print(file_split)
# # #         #print(filename)
# # #         #keywords=re.findall(r'\baaa\b|\bbbb\b', cleaned_txt,re.DOTALL)
# # #         keywords=re.findall(r'\bnegative\b|\bpositive\b|\buncertainty\b|\blitigious\b|\bconstraining\b|\bsuperfluous\b|\bmodal\b', cleaned_txt,re.DOTALL)
# # #         # negative=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         # positive=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         # uncertainty=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         # constraining=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         # superfluous=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         # interesting=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         # modal=re.findall('aaa', cleaned_txt,re.DOTALL)
# # #         #print(negative)
# # #         #print(keywords)
# # #         # aaa_count=keywords.count('aaa')
# # #         # bbb_count=keywords.count('bbb')
# # #         symbol=file_split[0]
# # #         reporttype=file_split[1]
# # #         filingdate=file_split[2][:-4]
# # #         negative_count=keywords.count('negative')
# # #         positive_count=keywords.count('positive')
# # #         uncertainty_count=keywords.count('uncertainty')
# # #         litigious_count=keywords.count('litigious')
# # #         constraining_count=keywords.count('constraining')
# # #         superfluous_count=keywords.count('superfluous')
# # #         interesting_count=keywords.count('interesting')
# # #         modal_count=keywords.count('modal')
        
# # #         #print(aaa_count)
# # #         #print(bbb_count)
# # #         #df=pd.DataFrame([[aaa_count, bbb_count]], columns=['aaa','bbb'])
# # #         df=pd.DataFrame([[symbol,reporttype,filingdate,negative_count, positive_count,uncertainty_count, litigious_count, constraining_count, superfluous_count,interesting_count, modal_count]], columns=['Symbol','ReportType','FilingDate','Negative','Positive', 'Uncertainty','Litigious','Constraining','Superfluous', 'Interesting', 'Modal'])
# # #         #print(df)
# # #         dfadd_on=df
# # #         base=pd.concat([dfbase,dfadd_on], axis=0)
# # #         #print(base)
# # #         dfbase=base
# # #     dfbase.to_csv(output_file, index=False)

# # # write_document_sentiments('C:/Users/Kevin/python/cleaned_files_folder','C:/Users/Kevin/python/export_csv_folder/.sentiment_factors.csv')

