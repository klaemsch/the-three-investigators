import papermill as pm
from settings import page_settings

for id in range(0, 226):
    id_str = f'{id:>03}'
    print(f'Starting notebook for script {id_str}')
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
            raise e