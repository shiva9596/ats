## creating end to end resume ats using google gemini pro vision llm model


```bash
project repo: https://github.com/
```

### Step -01 - Create a conda environment aftr opening the repository

```bash
conda create -n atsbot python=3.10 -y
```

### Step -02 - install the requirements file.
```bash
pip install -r requirements.txt
```


### Step -03 Create new file named app.py
```bash
touch app.py
```

### As a step 4 we need to make sure to create a new Google API Key by visiting to the official site: (https://aistudio.google.com/apikey)
### in next stpe write all code requireemnts in app.py
### Key step: for few users there might be a issue faced by poppeyes then in that case download the official and latest package of Popplers from here [popplers](https://github.com/oschwartz10612/poppler-windows/releases), Extract Poppler by Right -click on ZIp Folder. then make sure to add the following path of the Popplers folders in system environments (C:\poppler\Library\bin). 


### now run the following command. 
```bash
streamlit run app.py
```
### after running the above file it should now redirect to the browser stating the following localhost address: http://localhost:8501
### now you can make all necessary changes to the Resume as per JD