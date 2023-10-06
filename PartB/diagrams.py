from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User
from diagrams.generic.storage import Storage

with Diagram("Data Validation and Reporting", show=False):

    with Cluster("User"):
        user = User("User")
        upload_file = user >> Blank() >> Storage("Upload CSV File")
        user_selects = user >> Blank() >> Blank("User Selects wrong file")
        run_expectation = user_selects >> Storage("Run Expectation Validation")
        generate_report = user_selects >> Storage("Generate Pandas Profile Report")

    with Cluster("Error Handling"):
        error_handling = Blank("Error Handling")
        upload_file >> user_selects
        user_selects >> run_expectation
        user_selects >> generate_report
        user_selects >> Edge(label="Upload Error", color="red") >> error_handling