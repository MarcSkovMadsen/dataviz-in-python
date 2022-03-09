import json
import panel as pn

from pyecharts.charts import Bar

from dataviz_in_python import config

config.configure("echarts", url="lib_pyecharts", title="PyECharts")

TEXT = """
# PyEcharts: 

[PyEcharts](https://pyecharts.org/#/) is a Python wrapper for [ECharts](lib_echarts).

Please note **currently I cannot recommend PyEcharts** as the documentation often seems out of date 
and the examples not working. But Echarts and thus PyEcharts is an Apache project and produces 
business plots of a higher quality than Plotly. So it worth monitoring.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_pyecharts.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(accent_base_color="blue"):
    plot = (
        Bar()
        .add_xaxis(["Helicoptors", "Planes", "Air Ballons"])
        .add_yaxis("Total In Flight", [50, 75, 25], color=accent_base_color)
    )

    # Workaround to make plot responsive
    plot = json.loads(plot.dump_options())
    plot["responsive"] = True
    return plot


theme = config.get_theme()
plot = get_plot(accent_base_color=config.ACCENT_BASE_COLOR)
pn.pane.ECharts(plot, min_height=500, sizing_mode="stretch_both", theme=theme).servable()
