import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import great_expectations as ge
import warnings

st.title("Data Summarizer Pandas Profiling and GX")
st.sidebar.title("Settings")

uploaded_file = st.sidebar.file_uploader("Upload a CSV or XLSX file", type=["csv", "xlsx"])

data_type = st.sidebar.radio("Select Data Type:", ("Origination Data", "Monthly Performance Data"))

def run_expectations_Origination(ge_df):
    
    #add expectations here
    #ge_df.expect_column_values_to_be_unique("column_name1")
    return ge_df.validate()

def run_expectations_Monthly(ge_df):
    
    #ge_df.expect_column_values_to_be_unique("column_name2")
    return ge_df.validate()

def check_data_type(df):
    # Check if it's Origination Data
    origination_columns = ['Credit_Score', 'First_Payment_Date', 'First_Time_Homebuyer_Flag',
       'Maturity_Date',
       'Metropolitan_Statistical_Area_(MSA)_Or_Metropolitan_Division',
       'Mortgage_Insurance_Percentage_(MI_%)', 'Number_of_Units',
       'Occupancy_Status', 'Original_Combined_Loan-to-Value_(CLTV)',
       'Original_Debt-to-Income_(DTI)_Ratio', 'Original_UPB',
       'Original_Loan-to-Value_(LTV)', 'Original_Interest_Rate', 'Channel',
       'Prepayment_Penalty_Mortgage_(PPM)_Flag',
       'Amortization_Type_(Formerly_Product_Type)', 'Property_State',
       'Property_Type', 'Postal_Code', 'Loan_Sequence_Number', 'Loan_Purpose',
       'Original_Loan_Term', 'Number_of_Borrowers', 'Seller_Name',
       'Servicer_Name', 'Super_Conforming_Flag',
       'Pre-HARP_Loan_Sequence_Number', 'Program_Indicator', 'HARP_Indicator',
       'Property_Valuation_Method', 'Interest_Only_(I/O)_Indicator',
       'Mortgage_Insurance_Cancellation_Indicator']  
    if all(col in df.columns for col in origination_columns):
        return "Origination Data"


    performance_columns = ['Loan_Sequence_Number', 'Monthly_Reporting_Period',
       'Current_Actual_UPB', 'Current_Loan_Delinquency_Status', 'Loan_Age',
       'Remaining_Months_to_Legal_Maturity', 'Defect_Settlement_Date',
       'Modification_Flag', 'Zero_Balance_Code', 'Zero_Balance_Effective_Date',
       'Current_Interest_Rate', 'Current_Deferred_UPB',
       'Due_Date_of_Last_Paid_Installment_(DDLPI)', 'MI_Recoveries',
       'Net_Sales_Proceeds', 'Non_MI_Recoveries', 'Expenses', 'Legal_Costs',
       'Maintenance_and_Preservation_Costs', 'Taxes_and_Insurance',
       'Miscellaneous_Expenses', 'Actual_Loss_Calculation',
       'Modification_Cost', 'Step_Modification_Flag', 'Deferred_Payment_Plan',
       'Estimated_Loan-to-Value_(ELTV)', 'Zero_Balance_Removal_UPB',
       'Delinquent_Accrued_Interest', 'Delinquency_Due_to_Disaster',
       'Borrower_Assistance_Status_Code', 'Current_Month_Modification_Cost',
       'Interest_Bearing_UPB']  
    if all(col in df.columns for col in performance_columns):
        return "Monthly Performance Data"

    return None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    #ge_df = ge.from_pandas(df)

    data_type = check_data_type(df)

    if data_type is not None:
        st.subheader(f"This appears to be {data_type}.")
        if data_type == "Origination Data":
            ge_df = ge.from_pandas(df)
            results = run_expectations_Origination(ge_df)
        else:
            ge_df = ge.from_pandas(df)
            results = run_expectations_Monthly(ge_df)
        #st.write(df) testing

        st.subheader("Great Expectations Results")
        st.write(results)

    else:
        st.warning("The uploaded file does not match either Origination or Monthly Performance Data patterns. Please select the correct file.")

    #profile = ProfileReport(df, explorative=True) #testing
    profile = ProfileReport(results, explorative=True)
    if st.button("Generate Report"):
        
        report = profile.to_file("report.html")
        st.success("Report generated successfully!")

    
    if "report.html" in locals():
        st.download_button("Download Report", "report.html")

# if uploaded_file is not None:
    
#     if data_type == "Origination Data":
#         df = pd.read_csv(uploaded_file, encoding='utf-8')
#     else:
#         df = pd.read_excel(uploaded_file, encoding='utf-8', engine='openpyxl')

#     st.subheader("Data Preview:")
#     st.write(df)

   
    # st.subheader("Pandas Profiling Report:")
    # profile = ProfileReport(df, explorative=True)
    # #st.write(profile.to_widgets())
    # st.write(profile.to_html())


