import papermill as pm
from settings import page_settings
import concurrent.futures
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def notebook_worker(id_str: str):
    logging.info(f'Starting notebook for script {id_str}')
    try:
        pm.execute_notebook(
            "template.ipynb",
            f"output/output_{id_str}.ipynb",
            parameters={"script_number": id_str}
        )
    except pm.exceptions.PapermillExecutionError as e:
        if e.ename == 'FileNotFoundError':
            print(f'pdf file for id {id} could not be found')
        else:
            logging.error(f"Exception in notebook with id {id_str}: {e}")


id_strings = [f'{id:>03}' for id in range(0, 226)]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(notebook_worker, id_strings)
