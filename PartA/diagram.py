from diagrams import Diagram, Cluster
from diagrams.generic.device import Tablet
from diagrams.generic.network import Router
from diagrams.generic.os import LinuxGeneral
from diagrams.onprem.client import User
from diagrams.generic.place import Datacenter
from diagrams.programming.language import Python

with Diagram("OCR Application Architecture", show=False, filename="architecture_diagram"):
    user = User("User")
    pdf_link = LinuxGeneral("PDF Link Input")

    with Cluster("Streamlit Community"):
        app = Datacenter("OCR App (Streamlit)")
        select_ocr = LinuxGeneral("OCR Selection")

    with Cluster("Local Environment"):
        backend = Python("Backend")
        pypdf = Python("PyPDF")
        api_router = Router("Localhost:8503")

    with Cluster("Colab Notebook via Ngrok"):
        colab = Tablet("Colab Notebook")
        nougat_api = Python("Nougat API")

    github = LinuxGeneral("GitHub Repository")

    user >> pdf_link >> app
    app >> select_ocr
    select_ocr >> pypdf
    select_ocr >> api_router >> colab >> nougat_api
    backend >> github
