import papermill as pm
from settings import page_settings

for key, value in page_settings.items():
    id = key
    settings = value
    pm.execute_notebook(
        "template.ipynb",
        f"output/output_{id}.ipynb",
        parameters={"script_number": id}
    )