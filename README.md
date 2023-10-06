# Assignment_01
## Part 1 - Nougat/PyPDF OCR Application on StreamLit

Intallation/Guide on how to run Part A:

Step 1:
- Once the github repo has been cloned, we need to go to the following file Assignment_01 > PartA > main.py using any IDE (preferably VSCODE)
- Open the integrated terminal for the same
- Create the required virtual environment by writing > python -m venv .ocrenv
- Activate the Virtual Environment > source .ocrenv/bin/activate
- Then import the required modules from requirements.txt > pip install -r requirements.txt
- This will set up the initial requirements

Step 2:
- Open the Nougat_API_Hosting.ipynb file on Google Colab and reset the runtime at first
- Connect to T4 GPU4 and visit the site https://dashboard.ngrok.com/auth to generate an auth code
- Save the auth code somewhere and add it in the file at the bottom where it is mentioned
- Further run the entire document step by step and in the end we get an ngrok link where the local host 8503 has been hosted somewhere else
- Visit the site and check if the Nougat API is working properly with the status code: 200 If it’s not working, try deleting and creating a new runtime as well as reset the auth token for ngrok and redo step 2

Step 3:
- Once Step 1 and Step 2 are done, come back to the main.py file
- On the terminal run the streamlit app with the following code: > streamlit run main.py
- This will redirect the user to a streamlit app page

Note: The streamlit application has also been deployed on streamlit community and can be accessed using - https://bigdataia-fall2023-team8-assignment-01-partamain-soham-sovmhy.streamlit.app/


## Part 2 - Pandas Profiling and Great Expectations on StreamLit

Intallation/Guide on how to run Part B:

- Once the github repo has been cloned, we need to go to the following file Assignment_01 > PartB > main.py
- Open the integrated terminal for the same
- Create the required virtual environment by writing > python -m venv .gxenv
- Activate the Virtual Environment > source .gxenv/bin/activate
- Then import the required modules from requirements.txt > pip install -r requirements.txt
- Run great expectations command on terminal > great_expectations init
- On the terminal run the streamlit app with the following code: > streamlit run main.py

Link to Codelabs File - [https://codelabs-preview.appspot.com/?file_id=1IOtgAn5DYxGa9WVIyqiJ8KyA_FHH0HGAUe_u6FTMMZU#0](url)
## Structure of Github

```
.
├── LICENSE
├── PartA
│   ├── Nougat_API_Hosting.ipynb
│   ├── diagram.py
│   ├── main.py
│   └── requirements.txt
├── PartB
│   ├── PartB_a.ipynb
│   ├── PartB_a.ipynbZone.Identifier
│   ├── __pycache__
│   ├── diagrams.py
│   ├── gx
│   ├── main.py
│   └── requirements.txt
├── README.md
├── Tech Doc Assignment 1.pdf
└── architecture_diagram.png
```
