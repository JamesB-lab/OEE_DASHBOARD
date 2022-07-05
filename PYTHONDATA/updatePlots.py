from plotlyAvailabilityGauge import run_plotly_Availability
from plotlyPerformanceGauge import run_plotly_Performance
from plotlyQualityGauge import run_plotly_Quality
from plotlyOEEGauge import run_plotly_OEE
from plotlyTimeSeries import run_plotly_TimeSeries

def run_update_plots():

    print("Running Update Plots Function")
    run_plotly_Availability()
    run_plotly_Performance()
    run_plotly_Quality()
    run_plotly_OEE()
    run_plotly_TimeSeries()
    

