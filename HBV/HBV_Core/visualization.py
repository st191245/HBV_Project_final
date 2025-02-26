from HBV_Core.log_config import *

def create_plots(data_hbv): # Creating Scatter plots using plotly.graph_objects
    """
       Creates and displays scatter plots comparing simulated and observed discharge volumes.

       This function generates a scatter plot for both the simulated discharge volume and
       the observed discharge volume over time, and displays it interactively. The plot is
       also saved as an interactive HTML file.

       :param data_hbv: DataFrame containing the date and discharge volume data
       :return: Plotly figure object representing the generated scatter plot
       Authors: Hedieh & Shunmuga Priya
       """

    discharge_plots = [
        go.Scatter(
            x=data_hbv["date"],
            y=data_hbv["Discharge_Vol_simulated"],
            mode="lines+markers",
            name="Discharge_Vol_simulated",
            line=dict(color="blue"),
        ),
        go.Scatter(
            x=data_hbv["date"],
            y=data_hbv["discharge_vol"],
            mode="lines+markers",
            name="Discharge Volume Observed",
            line=dict(color="orange"),
        ),
    ]

    action_logger.info("Scatter plots for discharge volume created successfully.")

    # Create the figure
    fig = go.Figure(data=discharge_plots)

    # Update the layout
    fig.update_layout(
        title='Discharge Volume: Simulated vs Observed',
        xaxis_title='Date',
        yaxis_title='Discharge Volume in m3/s',
        legend_title='Runoff Type',
        xaxis=dict(rangeslider=dict(visible=True)),  # Adding the range slider for zooming
    )

    action_logger.info("Figure layout updated with titles and range slider.")


    fig.show()

    return fig

def create_plot2(data_hbv):

    soil_moisture_plot = [
        go.Scatter(
            x=data_hbv["date"],
            y=data_hbv["precipitation"],
            mode="lines+markers",
            name="precipitation",
            line=dict(color="red"),
        ),
        go.Scatter(
            x=data_hbv["date"],
            y=data_hbv["Soil_moisture"],
            mode="lines+markers",
            name="Soil_moisture",
            line=dict(color="purple"),
        ),
    ]

    action_logger.info("Scatter plots for soil_moisture and precipitation created successfully.")


    # Create the figure
    fig1 = go.Figure(data=soil_moisture_plot)

    # Update the layout
    fig1.update_layout(
        title='Soil_Moisture vs Precipitation',
        xaxis_title='Date',
        yaxis_title='Soil_moisture',
        legend_title='soil_moisture',
        xaxis=dict(rangeslider=dict(visible=True)),  # Adding the range slider for zooming
    )


    fig1.show()

    return fig1

    action_logger.info("Scatter plots displayed successfully.")

    # Save the plot as an interactive HTML file
    pyo.init_notebook_mode()
    pyo.iplot(fig,fig1, filename='discharge_volume_simulation.html,Soil_Moisture vs Precipitation')



