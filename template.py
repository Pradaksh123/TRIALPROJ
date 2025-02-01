import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


list_of_files = [


    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py", 
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup/init_setup.sh",
    "requirement/requirements.txt",
    "requirement/requirements_dev.txt",
    "setup/setup.py",
    "setup/setup.cfg",
    "projpy/pyproject.toml",
    "tox/tox.ini",
    "experiment/experiments.ipynb"

]
for filepath in list_of_files:
    filepath = Path(filepath)
    
    # Get the directory and filename
    filedir, filename = os.path.split(filepath)
    
    # Check if the directory is not empty
    if filedir:  # Ensure filedir is not an empty string
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

        # Check if the file does not exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, 'w') as f:
                pass  # Create an empty file
            logging.info(f"Created file: {filepath}")


