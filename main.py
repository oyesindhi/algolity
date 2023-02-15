import pandas as pd
import streamlit as st
import random
import string
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

# set page config
st.set_page_config(page_title='Algolity',page_icon=':bar_chart:',layout='wide')

# upload file
file = st.file_uploader('Upload Excel File',help='Excel File Only',accept_multiple_files=False)

# if file is uploaded, read it else give a warning
if file is not None:
    file_df = pd.read_excel(file)
else:
    st.warning('Please upload the excel file')
    st.stop()

# print raw file
st.subheader('Raw File')
st.dataframe(file_df)

# the df convert to excel
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data

# choose which tool to use
select_tool = st.radio('Convert the excel file',options=['Whole PNL Wise / Date Wise','Strike Wise / Individual PNL Wise'],help='"PNL Wise" means only main trade will be taken & individual legs/trades will be removed & "Strike Wise / Individual PNL Wise means individual legs will be considered and final PNL amount will be removed.')

# if you want pnl wise statement
if select_tool == 'Whole PNL Wise / Date Wise':

    # drop child entries & plot new df
    file_df = file_df.drop_duplicates(subset='Entry Date')
    st.dataframe(file_df)

    # export df to excel
    df_xlsx = to_excel(file_df)

    # download excel button
    download_button = st.download_button('Download File',df_xlsx,file_name='PNL_Wise_Report.xlsx')

if select_tool == 'Strike Wise / Individual PNL Wise':

    # drop child entries & plot new df
    new_file_df = file_df.dropna()
    st.dataframe(new_file_df)

    # convert the df to excel & export
    from io import BytesIO
    from pyxlsb import open_workbook as open_xlsb
        
    # export df to excel
    df_xlsx = to_excel(new_file_df)

    # download excel button
    download_button = st.download_button('Download File',df_xlsx,file_name='Individual_Trades.xlsx')
    
#this is the css code to hide main menu button, stream logo at the bottom, top header colored ribbon
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
