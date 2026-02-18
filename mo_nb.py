import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import marimo as mo

    # Define the 26 columns as specified by NASA
    index_columns = ['unit_id', 'cycles']
    setting_columns = ['setting_1', 'setting_2', 'setting_3']
    sensor_columns = [f'sensor_{i}' for i in range(1, 22)]
    column_names = index_columns + setting_columns + sensor_columns

    # Load the training data (sep=r'\s+' to handle whitespace separation)
    df = pd.read_csv('data/train_FD001.txt', sep=r'\s+', header=None, names=column_names)

    # FOCUS: Sensors related to Fuel System & Core Health
    # s_14: Physical Core Speed (Fuel Pump efficiency)
    # s_11: HPC Outlet Pressure (Combustion pressure)
    # s_12: LPT Outlet Pressure (Burn efficiency)
    focused_sen_df = df[['unit_id', 'cycles', 'sensor_14', 'sensor_11', 'sensor_12']].copy()

    # Display the first few rows of the focused sensor data
    focused_sen_df.head()



    return


if __name__ == "__main__":
    app.run()
