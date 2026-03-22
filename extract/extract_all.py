import papermill as pm
from settings import page_settings

ignore = [2, 15, 23, 40, 141, 148, 158]

for id in range(0, 226):
    if id in ignore:
        print(f'ignoring script with id {id}')
        continue
    id_str = f"{id:>03}"
    print(f"Starting notebook for script {id_str}")
    try:
        pm.execute_notebook(
            "template.ipynb",
            f"output/output_{id_str}.ipynb",
            parameters={"script_number": id_str},
        )
    except pm.exceptions.PapermillExecutionError as e:
        if e.ename == "FileNotFoundError":
            print(f"pdf file for id {id} could not be found")
        else:
            raise e
