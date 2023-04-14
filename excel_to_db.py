import os
import pandas as pd
from sqlalchemy import create_engine

# make sure LMSDataset folder is present in current directory
db_name = 'LMS'
files_dir = 'LMSDataset/'
db_url = f"sqlite:///{db_name}.db"

engine = create_engine(db_url)

files = os.listdir(files_dir)

for file in files:
    df = pd.read_excel(files_dir + file)
    df.to_sql(file.split('.')[0].upper(), con=engine)