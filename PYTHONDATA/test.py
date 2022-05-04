import plotly.graph_objects as go


exampleVar = 100


fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 85,
    mode = "gauge+number+delta",
    title = {'text': "Test"},
    delta = {'reference': exampleVar},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 250], 'color': "lightgray"},
                 {'range': [250, 400], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

fig.show()