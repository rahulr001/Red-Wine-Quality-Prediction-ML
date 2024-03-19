import os
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
import yaml
from src import logger
import json

class Helpers:

    @staticmethod
    def read_yaml(yaml_path: Path) -> ConfigBox:
        try:
            print(yaml_path)
            with open(yaml_path) as yaml_file:
                content = yaml.safe_load(yaml_file)
                logger.info(f"yaml file: {yaml_path} loaded successfully")
                return ConfigBox(content)
        except BoxValueError:
            raise ValueError("yaml file is empty")
        except Exception as e:
            raise e
        
        
    @staticmethod
    def create_directories(dir_paths: list) -> None:
        try:
            for path in dir_paths:
                os.makedirs(path, exist_ok=True)
                logger.info(f"created directory at: {path}")
        except Exception as e:
            raise e


    @staticmethod
    def save_json(path: Path, data: dict) -> None:
        try:
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"json file saved at: {path}")
        except Exception as e:
            raise e
        

    @staticmethod
    def load_json(path: Path) -> ConfigBox:
        try:
            with open(path) as f:
                logger.info(f"json file loaded succesfully from: {path}")
                return ConfigBox(json.load(f))
        except Exception as e:
            raise e


    @staticmethod
    def get_size(path: Path) -> str:
        try:
            return f'{round(os.path.getsize(path)/ 1024)} KB'
        except Exception as e:
            raise e