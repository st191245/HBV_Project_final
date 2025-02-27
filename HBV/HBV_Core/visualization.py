from HBV_Core.log_config import *
import plotly.graph_objects as go
import plotly.offline as pyo  # Importing Plotly offline mode


# Authored by Shunmuga Priya & Hedieh
def create_plots(data_hbv):
    """
    Creates and displays scatter plots comparing simulated and observed discharge volumes.

    This function generates a scatter plot for both the simulated discharge volume and
    the observed discharge volume over time and displays it interactively.
    The plot is also saved as an interactive HTML file.

    :param data_hbv: DataFrame containing the date and discharge volume data
    :return: Plotly figure object representing the generated scatter plot
    """

    # Creating scatter plots for simulated and observed discharge volumes
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

    # Update the layout with titles and a range slider for zooming
    fig.update_layout(
        title="Discharge Volume: Simulated vs Observed",
        xaxis_title="Date",
        yaxis_title="Discharge Volume in m³/s",
        legend_title="Runoff Type",
        xaxis=dict(rangeslider=dict(visible=True)),
    )

    action_logger.info("Figure layout updated with titles and range slider.")

    # Show the figure interactively
    fig.show()

    # Save the plot as an interactive HTML file
    pyo.plot(fig, filename="discharge_volume_simulation.html")

    return fig


def create_plots2(data_hbv):
    """
    Creates and displays scatter plots comparing soil moisture and precipitation over time.

    This function generates a scatter plot showing the relationship between precipitation
    and soil moisture. The plot is interactive and also saved as an HTML file.

    :param data_hbv: DataFrame containing soil moisture and precipitation data
    :return: Plotly figure object representing the generated scatter plot
    """

    # Creating scatter plots for precipitation and soil moisture
    soil_moisture_plot = [
        go.Scatter(
            x=data_hbv["date"],
            y=data_hbv["precipitation"],
            mode="lines+markers",
            name="Precipitation",
            line=dict(color="red"),
        ),
        go.Scatter(
            x=data_hbv["date"],
            y=data_hbv["Soil_moisture"],
            mode="lines+markers",
            name="Soil Moisture",
            line=dict(color="purple"),
        ),
    ]

    action_logger.info("Scatter plots for soil moisture and precipitation created successfully.")

    # Create the figure
    fig1 = go.Figure(data=soil_moisture_plot)

    # Update the layout with titles and a range slider for zooming
    fig1.update_layout(
        title="Soil Moisture & Precipitation",
        xaxis_title="Date",
        yaxis_title="Soil Moisture and Precipitation",
        legend_title="Legend",
        xaxis=dict(rangeslider=dict(visible=True)),
    )

    fig1.show()  # Show the figure interactively

    action_logger.info("Scatter plots displayed successfully.")

    # Save the plot as an interactive HTML file
    pyo.plot(fig1, filename="soil_moisture_and_precipitation.html")

    return fig1
