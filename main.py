from Homestayes_data import logger
from Homestayes_data.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Homestayes_data.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Homestayes_data.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Homestayes_data.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from Homestayes_data.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME= "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME ="DATA VALIDATION STAGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME="DATA TRANSFORMATION SATGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME = "MODEL TRAINER STAGE"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj =ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME = "MODEL EVALUATION  STAGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj =ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  