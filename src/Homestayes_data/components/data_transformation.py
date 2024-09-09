import os 
from Homestayes_data import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from Homestayes_data.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        col=data.select_dtypes(include='object').columns
        data.drop(columns=col,inplace=True)
        data.dropna(inplace=True)
        data.drop(columns='id',inplace=True)
        train , test =train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        
        logger.info("splited data into training and test set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        
        
        