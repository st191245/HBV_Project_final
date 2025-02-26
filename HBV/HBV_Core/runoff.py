from HBV_Core.snow import Snow
from HBV_Core.log_config import *


class SoilMoisture(Snow):
    """
    This class models the soil moisture and runoff process. This class extends the Snow model and calculates
    evapotranspiration (ET), runoff, and soil moisture based on given input parameters.
    Authored by: Shunmuga Priya
    """

    def __init__(self, csv_file_name=CSV_FILE_NAME, beta=BETA, TT=TT, Cmelt=CMELT, SWE=SWE_INITIAL, mm_to_m=MM_TO_M,
                 day_to_s=DAY_TO_S, Area=CATCHMENT_AREA, initial_soil_moisture=INITIAL_SOIL_MOISTURE, FC=FIELD_CAPACITY,
                 pwp=PWP):
        """
        Initializes the SoilMoisture model with given parameters.
        """
        # Call the parent class (Snow) constructor to initialize the snow model with the given file and parameters
        super().__init__(csv_file_name, TT, Cmelt, SWE)

        # Initialize the specific parameters for the SoilMoisture model
        self.beta = beta,
        self.k = K
        self.time_step = TIME_STEP
        self.initial_soil_moisture = initial_soil_moisture
        self.FC = FC
        self.pwp = pwp
        self.area = Area
        self.mm_to_m = mm_to_m
        self.day_to_s = day_to_s
        self.processed_data = None  # Placeholder for processed data (initialized to None)

        action_logger.info(
            f"SoilMoisture model initialized with beta={self.beta}, k={self.k}, time_step={self.time_step}"
        )

    def calculate_ET_and_soil_moisture(self):
        """
        Calculate evapotranspiration (ET) and soil moisture for each time step.

        This method computes soil moisture, runoff, and ET values and updates the DataFrame
        with the calculated values.

        :return: Updated DataFrame with 'Simulated_Runoff', 'Soil_moisture', and 'ET' columns
        :rtype: pandas.DataFrame
        :raises KeyError: If required columns ('liquid_water' or 'peti') are missing
        """
        # Check if required columns 'liquid_water' or 'peti' exist in the DataFrame
        if 'liquid_water' not in self.data_hbv.columns or 'peti' not in self.data_hbv.columns:
            error_logger.error("Required columns 'liquid_water' or 'peti' are missing from the DataFrame.")
            raise KeyError("Required columns 'liquid_water' or 'peti' are missing from the DataFrame.")

        # Initialize empty lists to store the calculated values
        soil_moisture, runoff,et_values = [],[],[]

        # Loop through the DataFrame to calculate ET, soil moisture, and runoff for each time step
        for index, row in self.data_hbv.iterrows():
            liquid_water = row['liquid_water']  # Get the liquid water row from Dataframe
            peti = row['peti']  # Get the peti (Potential Evapotranspiration) row from Dataframe

            if index == 0:  # For the first row, initialize with the initial conditions
                s_new = self.initial_soil_moisture
                q_new = self.k * s_new  # runoff for the first time step
                et = (s_new / self.FC) * peti if s_new < self.pwp else peti  # ET for the first time step
            else:  # For subsequent rows, calculation based on previous values
                inflow = liquid_water  # Incoming water from precipitation and snow melt
                outflow = runoff[-1] + et_values[-1]  # Sum of previous runoff and ET values
                sm_t = max(0, soil_moisture[-1] + inflow - outflow)  # Calculate the new soil moisture
                qb_t = liquid_water * ((sm_t / self.FC) ** self.beta)  # Calculate runoff based on soil moisture
                s_new = max(0.0, soil_moisture[-1] + inflow - qb_t - et_values[-1])  # Update soil moisture
                q_new = qb_t  # Update runoff value
                et = (s_new / self.FC) * peti if s_new < self.pwp else peti  # Calculate ET for this time step

            # Append the calculated values to their respective lists
            soil_moisture.append(s_new), runoff.append(q_new),  et_values.append(et)

        # Update the DataFrame with the new calculated values
        self.data_hbv["Simulated_Runoff"] = runoff
        self.data_hbv["Soil_moisture"] = soil_moisture
        self.data_hbv["ET"] = et_values

        action_logger.info("ET and soil moisture calculations completed successfully.")

        return self.data_hbv

    def __str__(self):
        """
        Return a string summarizing the parameters of the SoilMoisture model.

        :return: String with the values of beta, k, and time_step
        :rtype: str
        """
        return f"SoilMoisture model with beta={self.beta}, k={self.k}, time_step={self.time_step}"

    def volume_discharge(self):
        """
        Calculate the discharge volume based on the simulated runoff values.

        This method iterates over each row of the data to calculate the discharge volume
        using the formula for converting runoff (in mm/day) to discharge volume (in m³/s).
        The calculated discharge volumes are added to a new column in the DataFrame.

        The updated DataFrame can be saved to an Excel file.

        :return: Updated DataFrame with 'Discharge_Vol_simulated' column containing the calculated discharge volumes
        :rtype: pandas.DataFrame
        """

        discharge_volume_simulated = []  # List to store calculated discharge volumes

        for index, row in self.data_hbv.iterrows():
            simulated_runoff = row['Simulated_Runoff']  # Accessing simulated runoff for the current row

            # Ensure 'Simulated_Runoff' is in mm/day, converting it to m³/s using the given formula
            discharge_volume = simulated_runoff * self.mm_to_m * self.area * self.day_to_s

            discharge_volume_simulated.append(discharge_volume)

            # Add the calculated discharge volumes to the DataFrame as a new column
        self.data_hbv["Discharge_Vol_simulated"] = discharge_volume_simulated

        action_logger.info(f"Range of discharge volume calculated: {np.ptp(discharge_volume_simulated)}")

        output_file = "../HBV/Data_with_discharge_simulated_output1.csv"
        self.data_hbv.to_csv(output_file, index=False)  # Save the DataFrame to CSV file
        print(f"DataFrame with discharge volume has been saved to {output_file}")

        return self.data_hbv

