from Homestayes_data.config.configuration import ConfigurationManager
from Homestayes_data.components.model_evalutation import ModelEvaluation
from Homestayes_data import logger

STAGE_NAME = "model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config =ConfigurationManager()
        model_evaluation_config =config.get_model_evalutation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_result()
 
 
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e    

