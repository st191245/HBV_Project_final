# Project : Package for Hydrological Modeling of River Discharge

***

## Table of Contents:

1. [Project's name](#Projects-name)
2. [Project purpose/description](#Project-purposedescription)
3. [Motivation](#Motivation)
4. [Goal](#Goal)
5. [Theory behind the Package](#Theory)
6. [Package requirements](#Package-requirements)
7. [Code Overview](#code-overview)
8. [Code diagram UML](#Code-Diagram)
9. [Installation and run a project](#Installation-and-running-a-project)

***

### Authors:  BKS
      1. Hedieh Beigi Pouya-3762109
      2. Mohammad Sharif Khaleqi-3638660
      3. Shunmuga Priya Subbiah-3703058
## Project's name 
***
Package for Hydrological Modeling of River Discharge
***
## Project purpose/description 

The project aims to implement a hydrological model for simulating river discharge based on various factors such as rainfall and snowfall,temperature,evapotranspiration and soil moisture storage.The project helps in understanding hydrological processes and their role in water resource management and flood forecasting. This model is important for understanding water flows and how it is stored in nature, which helps in managing water resources, anticipating how environmental changes will affect water systems, and making informed decisions in areas related to water use and conservation. 
***
## Motivation
Hydrological models play a vital role in water resources engineering by enabling the approximate simulation of river discharge, which is crucial for effective water supply management, hydraulic structure design, and flood risk mitigation. This project implements an HBV-based model to enhance the understanding of catchment hydrology and provide a computational framework for predicting river water flow using meteorological data
***
## Goal
 * 1.Create a Python package for simulating river discharge.

 * 2.Implement a simplified HBV hydrological model.

 * 3.Enable logging and visualization for better analysis.

The full package is available in: **GitHub Repository URL**
```
https://github.com/st191245/HBV_Project_final.git
```
***
## Theory
The primary goal of this project is to calculate the river discharge resulting form the rainfall and snow melt according to temperature considering evapotranspiration and soil moisture storage. According to simple water balance equation

P = Q + ET + &#916;S

Where,
* P- precipitation
* Q- runoff
* ET- Evapotranspiration
* &#916;S- change in soil moisture storage.

The HBV approach basically contains 3 modules.They are

#### 1. Snow Module

The model determines snow accumulation and melting based on temperature and precipitation. If the current temperature (T) is lower than the threshold temperature (TT), precipitation accumulates as snow. If T exceeds TT, snowmelt occurs, calculated as:

    liquid water =  𝑪𝒎𝒆𝒍𝒕∗ (𝑇 −𝑇𝑇)

where,
   * Cmelt - the coefficient that determines snow melt per degree of temperature

#### 2. Evapo Transpiration(ET) Module

 Evapotranspiration (ET) refers to the combined process of water evaporation from the soil and transpiration from plants. To calculate ET, this project considered several factors including the  soil moisture , potential evapotranspiration (𝒑et), and the permanent wilting point (𝒑𝒘𝒑). If the previous soil moisture is greater than the permanent wilting point, evapotranspiration occurs at its potential rate (𝐸𝑇𝑡 = 𝑃𝐸𝑡). However, if the soil moisture is less than or equal to the permanent wilting point, the actual evapotranspiration is proportional to the ratio of soil moisture to the wilting point and the potential evapotranspiration (𝐸𝑇𝑡 = 𝑆𝑀𝑡−1/𝒑𝒘𝒑 * 𝑃𝐸𝑡). This balance ensures that plants get the necessary water while accounting for soil moisture conditions.

#### 3. Soil Moisture Module

The soil moisture module tracks the dynamics of soil moisture and groundwater outflow. It uses previous soil moisture (𝑠𝑚𝑡−1), outflow from the snow module (𝐿𝑊𝑡), evapotranspiration (𝐸𝑇𝑡), field capacity (𝑭𝑪), and a coefficient (𝜷).
   
i. Current Soil Moisture (𝑠𝑚𝑡):
* Current Soil Moisture (𝑠𝑚𝑡):
* Formula: SMt = max(0.0, SM - 1 + LWt * &#946;)


ii. Final Soil Moisture:
* Adjusted for outflow to groundwater and evapotranspiration.
* Formula: SMt = max(0, SMt  1 + LWt  (Qb,t + ETt))

#### 4. Runoff Calculation

The surface runoff (Q) is computed using the following formula:
 
Q=k*S

where: 
- **Q**- Surface runoff in mm/day
- **k**- a coefficient that representing the efficiency of converting soil moisture into runoff 
- **S**- Soil moisture storage
  
***
## Package requirements
The required dependencies for successfully run this project are,
1. Python 3.11 or more recent versions
2. Libraries/Modules
* pandas
* numpy
* plotly
* os
* logging
### Input data
The reference data used in this project is taken from catchment attributes and hydro-meteorological timeseries for 671 catchments across Great Britain (CAMELS-GB) dataset.
The CSV file for the catchment -12007 - Dee at Mar Lodge, Scotland(CAMELS_GB_hydromet_timeseries_12007.csv) 
which contains data from 01-10-1987 to 30-09-2015 is used in this project

Note:The data file should contain the following columns for the input of the project:


| date | precipitation | peti | temperature | discharge_spec | discharge_vol |
|-----------------|:-------------:|:----:|:-----------:|:--------------:|:-------------:|
| 01/10/1987      |       0       | 0.93 |    7.91     |      1.54      |     5.205     |
| 02/10/1987      |       0       | 0.55 |    6.41     |      1.4       |     4.731     |
| .....           |      ...      |..|...|..|...|
date(DD/MM/YYYY),precipitaion (mm/day),temperature(°C),specific discharge in (mm/day), and discharge volume in (m³/s) for the necessary calculations 
for the project.The catchment area is 289 Km<sup>2</sup>.

***
## Code Overview
The object-oriented code utilizes custom classes, which are referenced within a main.py script to calculate runoff resulting from precipitation based on provided inputs. The code structure is built upon custom classes and functions defined in the following package.
The HBV_Core package contains,
1. user_config.py file:
 * Library Imports: Loads essential Python libraries (numpy, pandas, plotly) for data handling and visualization.
* File Paths: Defines paths for input (CSV_FILE_NAME) and output (OUTPUT_FILE) data files.
* Snow Parameters: Sets values for threshold temperature (TT), melting coefficient (Cmelt), and initial snow water equivalent (SWE_INITIAL).
* Evapotranspiration Parameters: Specifies soil moisture limits, including Permanent Wilting Point (PWP), initial soil moisture, and field capacity.
* Soil Moisture Parameters: Includes key hydrological coefficients (BETA, K) and time step (TIME_STEP).The time step mentioned here is 1 day.
* Catchment Properties: Defines catchment area (CATCHMENT_AREA) and unit conversion factors (mm_to_m, day_to_s).
* Plotting Option: A toggle (ENABLE_PLOTTING) to enable or disable visualization.
2. log_config.py

This file contains a function `setup_logger()` which,Sets up a logger to log messages to a specified log file with the given logging level.
This function creates a logger object with a file handler, sets the logging level,
and attaches a formatter to structure the log messages.This will create 3 logfiles such as actions.log,warnings.log,errors.log.These log files stores all
the logged messages.

3.snow.py 

This file contains two classes:

1. DataReader-This class is responsible for loading and handling HBV model data.It has 3 functions.
   
i.`__init__`  (csv_file_name, delimiter)- Initializes the object, sets the delimiter, and loads data from the specified CSV file
 
ii.`get_hbv_data(csv_file_name)`- Reads HBV model data into a Pandas DataFrame, handling errors and logging actions.

iii.`drop_missing_data()` - Removes rows with missing values from the dataset and logs the action.

2. Snow: This class inherits from _DataReader_, Models snow accumulation and melting.This class is also contain 3 functions.

i.`__init__(csv_file_name, TT, Cmelt, SWE)` _-Initializes the snow model with threshold temperature (TT), melting coefficient (Cmelt), and initial Snow Water Equivalent (SWE).

ii.`calculate_snow_melt()`- Simulates snow accumulation and melting based on temperature and precipitation data.
* This method uses TT and Cmelt to compute liquid water.
* Updates SWE after melting.

iii.`__str__()` - Returns a string summary of the snow model parameters (TT, Cmelt, and SWE).

3. runoff.py file
   
This file contains one class,SoilMoisture which inherits class Snow.It models soil moisture, evapotranspiration, and runoff processes.This Class contains 4 methods.

i. ` ___init__(csv_file_name, beta, TT, Cmelt, SWE, mm_to_m, day_to_s, Area, initial_soil_moisture, FC, pwp)`-
Initializes the soil moisture model with parameters for soil properties, evapotranspiration, and runoff.

ii.`calculate_ET_and_soil_moisture()` -Computes evapotranspiration (ET), soil moisture, and runoff for each time step.
Uses beta, field capacity (FC), and permanent wilting point (PWP) to update moisture balance.
Updates the dataset with calculated Simulated_Runoff, Soil_moisture, and ET values.

iii.`__str__()` -
Returns a string summary of the soil moisture model parameters (beta, k, and timeStep).

iv.`volume_discharge()` -This function computes the discharge volume (m³/s) from simulated runoff which will be in(mm/day) using catchment area and time conversion factors.
Stores the results in Discharge_Vol_simulated column and Saves the updated dataframe to an output file (Data_with_discharge_simulated_output1.csv) for further analysis and record-keeping.

5. visualization.py

This file contains two functions, `create_plots()` and `create_plots2()`, which generate interactive scatter plots using Plotly to visualize hydrological data. These functions help in analyzing the simulated and observed discharge volumes as well as soil moisture and precipitation trends over time.
Both functions utilize Plotly for dynamic visualization and include logging to track their execution status.

#### main.py file Overview: Executing HBV Modeling
The main.py file accesses the `HBV_Core` package to execute the HBV hydrological modeling process.It has 3 functions.

i.`hbv_calculation()`-  This function is responsible for executing the entire runoff modeling process using the HBV hydrological model. It begins by initializing a `SoilMoisture` object with the provided CSV file, which contains the necessary hydrometeorological data. The function then sequentially processes the data by loading it, removing missing values, calculating snowmelt, estimating evapotranspiration (ET) and soil moisture, and computing the discharge volume. The processed data is stored in the data_hbv attribute of the runoff object. If plotting is enabled, it generates visualizations to compare simulated and observed values and Precipitation and SoilMoisture values. Throughout the process, logging is used to track execution steps and handle any unexpected errors. Finally, the processed dataset is returned for further analysis.

ii.`statistics(processed_data)`-This function looks at runoff data and calculates the average and standard deviation for key variables like precipitation, simulated discharge, and observed discharge. This helps to see how the model's results compare to actual data, making it easier to understand and improve the model.

iii.`main()`-This function serves as the entry point for the runoff modeling process. It first calls `hbv_calculation()` to process hydrological data, including snowmelt, evapotranspiration, soil moisture, and discharge volume calculations. Once the data is processed, it passes the results to the `statistics()` function, which analyzes key metrics like mean and standard deviation. This function ensures the complete execution of the model and statistical evaluation in a structured manner.

## Code diagram UML
>   ![Imgname](Structure-uml.png)
## Installation and run a project

To install the required libraries, run:
```
pip install numpy pandas plotly os logging
```
Upon meeting software requirements and getting the input python file in the local device, run the main script
```
python main.py
```
to get output file and plots for results.
The Generated output files would be,

- 1.Data_with_discharge_simulated_output.csv file with updated dataframe columns will look like,


| date | precipitation | peti | temperature | discharge_spec | discharge_vol | liquid_water | Simulated_Runoff | Soil_moisture | ET            | Discharge_Vol_simulated |
|-----------------|:-------------:|:----:|:-----------:|:--------------:|:-------------:|-----------|------|:--------------|---------------|-------------------------|
| 01/10/1987      |       0       | 0.93 |    7.91     |      1.54      |     5.205     |0  | 5    | 10            | 0.031 |  16.724                 |
| 02/10/1987      |       0       | 0.55 |    6.41     |      1.4       |     4.731     | 0| 0    | 9.969         | 0.018         | 0                       |
| .....           |      ...      |..|...|..|...|..| ...  | ...           | ...           | ..                      |

-  2.Enabled plots as interactive html file
        
    - 1.Discharge Volume: Simulated vs Observed

     - 2.Soil_Moisture and Precipitation

## Source:
1.Bergström, Sten & FORSMAN, ARNE. (1973). Development of a conceptual deterministic rainfall-runoff model. Nordic Hydrol.. 4. 147-170. 10.2166/nh.1973.0012.
2.https://nrfa.ceh.ac.uk/data/station/info/12007




