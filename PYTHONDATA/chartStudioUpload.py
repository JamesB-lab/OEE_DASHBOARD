import chart_studio

username = 'james.booth' # your username
api_key = 'cCmuSWNFC4GOKnshMCr2' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

import chart_studio.plotly as py
py.plot(fig, filename = 'gdp_per_cap', auto_open=True)