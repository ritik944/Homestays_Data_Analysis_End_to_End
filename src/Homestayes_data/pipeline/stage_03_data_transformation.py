from Homestayes_data.config.configuration import ConfigurationManager
from Homestayes_data.components.data_transformation import DataTransformation
from Homestayes_data import logger


STAGE_NAME= "DATA TRANSFORMATION STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_tranformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
            
            
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e    
    
