from DA5_plotlyAvailabilityGauge import run_plotly_Availability
from DA5_plotlyPerformanceGauge import run_plotly_Performance
from DA5_plotlyQualityGauge import run_plotly_Quality
from DA5_plotlyOEEGauge import run_plotly_OEE
from DA5_plotlyTimeSeries import run_plotly_TimeSeries

def run_update_plots():

    print("Running Update Plots Function")
    run_plotly_TimeSeries()
    run_plotly_Availability()
    run_plotly_Performance()
    run_plotly_Quality()
    run_plotly_OEE()

run_update_plots()
    
    

