from HBV_Core.runoff import SoilMoisture
from HBV_Core.visualization import *
from HBV_Core.log_config import *
from HBV_Core.user_config import *

# Authors: Hedieh,Sharif and Shunmuga Priya
def hbv_calculation():
    """
       Execute the runoff modeling process, including loading data,
       performing snowmelt calculations, calculating evapotranspiration (ET),
       soil moisture, and discharge volume. Optionally, generates plots if enabled.

       :return: Processed data (DataFrame)
       :raises Exception: If an error occurs during the process, it is logged and re-raised
       """
    try:
        action_logger.info("Starting the main process for runoff modeling.")


        runoff = SoilMoisture(CSV_FILE_NAME) #Initialize SoilMoisture object to handle the data and calculations
        action_logger.info("SoilMoisture object initialized.")


        runoff.get_hbv_data(CSV_FILE_NAME)  # Reads data from CSV
        runoff.drop_missing_data()  # Removes rows with missing values
        runoff.calculate_snow_melt()       #  Calculates snowmelt based on input arguments
        runoff.calculate_runoff()  # Calculates runoff,ET and Soil Moisture
        runoff.volume_discharge()          # Calculates discharge volume


        processed_data = runoff.data_hbv  #  The processed data is stored in the runoff object's data_hbv attribute

        # Generate plots if enabled
        if ENABLE_PLOTTING:
            action_logger.info("Plotting is enabled. Generating plots.")
            create_plots(processed_data)  # plot1
            create_plot2(processed_data)  # plot2

        action_logger.info("Runoff modeling process completed successfully.")
        return processed_data #for further analysis
    except Exception as e:
        error_logger.error(f"An unexpected error occurred in the main process: {str(e)}")
        raise  # Re-raise the exception after logging

def statistics(processed_data):
    """
        Calculate and print the mean and standard deviations for key columns
        in the processed data.

        :param processed_data: DataFrame containing processed runoff data
        :return: None
        """
    print("Mean and Standard Deviation:")
    print("Precipitation - Mean:", np.nanmean(processed_data['precipitation']),
          "Std:", np.nanstd(processed_data['precipitation']))
    print("Discharge Simulated - Mean:", np.nanmean(processed_data['Discharge_Vol_simulated']),
          "Std:", np.nanstd(processed_data['Discharge_Vol_simulated']))
    print("Discharge Volume observed - Mean:", np.nanmean(processed_data['discharge_vol']),
          "Std:", np.nanstd(processed_data['discharge_vol']))

def main():
    """
    Main function to run the entire process, starting with the runoff modeling
    calculation and then calculating statistics.
    """
    processed_data = hbv_calculation()  # Get processed data from hbv_calculation and call the function
    statistics(processed_data)          # Pass processed data to statistics function to calculate the statistics

if __name__ == "__main__":
    main()
