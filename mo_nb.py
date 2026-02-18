import marimo as mo
import pandas as pd

__generated_with = "0.19.11"
app = mo.App(width="medium")


@app.cell
def load_data():
    # Define the 26 columns as specified by NASA
    index_columns = ['unit_id', 'cycles']
    setting_columns = ['setting_1', 'setting_2', 'setting_3']
    sensor_columns = [f'sensor_{i}' for i in range(1, 22)]
    column_names = [index_columns + setting_columns + sensor_columns]

    
    


    return


if __name__ == "__main__":
    app.run()
