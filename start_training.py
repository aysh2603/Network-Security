# This is the master file to call the training_pipeline

import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.pipeline.training_pipeline import TrainingPipeline

def start_training():
    try:
        #creating an object of TrainingPipeline
        model_training = TrainingPipeline()
        #executing the pipeline
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    start_training()