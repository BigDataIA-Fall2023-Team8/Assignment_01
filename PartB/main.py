import streamlit as st
import pandas as pd
import ydata_profiling
from pandas_profiling import ProfileReport
import great_expectations as ge
from great_expectations.data_context import DataContext
import os

from pandas_profiling import ProfileReport
# from great_expectations.datasource import DatasourceConfig
# from great_expectations.execution_engine import PandasExecutionEngineConfig
# from great_expectations.data_connector import FilesystemDataConnectorConfig, InferredAssetFilesystemDataConnector


yaml = ge.core.yaml_handler.YAMLHandler()
# Assuming context is already set up
# context = DataContext("/path/to/your/great_expectations/directory/")

st.title("Data Summarizer Pandas Profiling and GX")
st.sidebar.title("Settings")

# Upload the file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
data_asset_name = os.path.splitext(uploaded_file.name)[0]


import os
def get_file_type_from_filename(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension == '.csv':
        return 'CSV'
    elif file_extension in ['.xls', '.xlsx']:
        return 'Excel'
    else:
        return 'Unknown'
st.title("File Type Checker")

if uploaded_file is not None:
    file_type = get_file_type_from_filename(uploaded_file.name)
    st.write(f"Uploaded file type: {file_type}")


data_type = st.sidebar.radio("Select Data Type:", ("Origination Data", "Monthly Performance Data"))

# # Defining DataSource config
datasource_config = {
    "name": "pandas_datasource",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "PandasExecutionEngine"
    },
    "data_connectors":{
        "default_inferred_data_connector_name":  {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "/content/GX",
            "default_regex": {
                "group_names": ["data_asset_name"],
                #"pattern": "(.*)\\.csv|(.*)\\.xlsx",
                "pattern": "(.*)(\.csv|\.xlsx)",

            },
        },
},
}


if st.sidebar.button("Run Expectation"):
    context = DataContext("./gx/")
    datasource = context.test_yaml_config(yaml.dump(datasource_config))
    datasource = context.add_datasource(**datasource_config)  # datasource config
    # datasource = context.add_datasource("pandas_datasource",data_connectors)

    batch_request = ge.core.batch.BatchRequest(
    datasource_name = "pandas_datasource",
    data_connector_name =  "default_inferred_data_connector_name",

    data_asset_name = "data_asset_name" 

    )


    validator1 = context.get_validator(
        expectation_suite_name="Origination_Data",
        batch_request=batch_request
    )


    validator1.expect_column_values_to_match_regex(
            column="Credit_Score",
            # This regex matches either 9999 or values in the range [300, 850]
            regex=r'^(9999|[3-8]\d{2})$',  
            result_format="COMPLETE"
            )

context = DataContext("./gx/")

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

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    ge_df = ge.from_pandas(df)

    data_type = check_data_type(df)

    if data_type is not None:
         st.subheader(f"This appears to be {data_type}.")
         if data_type == "Origination Data":
            #  checkpoint_name = "my_checkpoint_type2"
            #  results = context.run_checkpoint(checkpoint_name=checkpoint_name, batches=[{"batch_kwargs": {"dataset": ge_df}}])

             profile = ProfileReport(df, explorative=True)
             if st.button("Generate Report: Pandas Profile"):
                report = profile.to_file("report.html")
                st.success("Report generated successfully!")


             if "report.html" in locals():
                 st.download_button("Download Report", "report.html")

         else:
            #  checkpoint_name = "my_checkpoint_type2"
            #  results = context.run_checkpoint(checkpoint_name=checkpoint_name, batches=[{"batch_kwargs": {"dataset": ge_df}}])

             profile = ProfileReport(df, explorative=True)
             if st.button("Generate Report: Pandas Profile"):
                    report = profile.to_file("report.html")
                    st.success("Report generated successfully!")

             if "report.html" in locals():
                 st.download_button("Download Report", "report.html")

    else:
         st.warning("The uploaded file does not match either Origination or Monthly Performance Data patterns. Please select the correct file.")
