"""
User Configuration File

Author:
- Shunmuga Priya Subbiah, WAREM

"""

# Importing standard libraries
try:
    import os
    import logging
except ImportError:
    print("ERROR: Cannot import basic Python libraries.")

# Importing global libraries
try:
    import numpy as np
    import pandas as pd
except ImportError:
    print("ERROR: Cannot import SciPy libraries.")

# Importing third-party libraries
try:
    import plotly.graph_objects as go
    import plotly.offline as pyo
except ImportError:
    print("ERROR: Cannot import plotly.graph_objects, plotly.offline packages.")

# File paths
BASE_PATH = os.getcwd()
CSV_FILE_NAME = os.path.join(BASE_PATH, "data", "CAMELS_GB_hydromet_timeseries_12007.csv")
OUTPUT_FILE = os.path.join(BASE_PATH, "Data_with_discharge_simulated_output1.csv")


# Check if the CSV file exists
print("File Exists:", os.path.exists(CSV_FILE_NAME))

# Snow parameters
TT = 0  # Threshold temperature for snow accumulation
CMELT = 15  # Melting coefficient
SWE_INITIAL = 0  # Initial snow water equivalent (SWE)

# Evapotranspiration parameters
PWP = 100  # Permanent Wilting Point (mm)
INITIAL_SOIL_MOISTURE = 5  # Initial soil moisture (mm)
FIELD_CAPACITY = 300  # Field Capacity (mm)

# Soil moisture parameters
BETA = 2  # Parameter for soil moisture calculation
K = 0.5  # Coefficient representing efficiency of converting soil moisture into runoff
TIME_STEP = 1  # Time step (daily)

# Catchment parameters
CATCHMENT_AREA = 289 * 1_000_000  # m²
MM_TO_M = 1 / 1000  # Conversion factor from mm to m
DAY_TO_S = 1 / (24 * 3600)  # Conversion factor from day to seconds

# Plotting option
ENABLE_PLOTTING = True

