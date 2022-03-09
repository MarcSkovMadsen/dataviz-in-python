import panel as pn

from dataviz_in_python import config

config.configure("echarts", title="Echarts", url="lib_echarts")

TEXT = """
# Echarts: Modern .js visualization in the browser

[ECharts](https://echarts.apache.org/en/index.html) is a a very powerful and appealing open source javaScript visualization library.

For a more Pythonic interface see [PyEcharts](lib_pyecharts). For another example see [awesome-panel.org/echarts](https://awesome-panel.org/echarts).

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_echarts.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot():
    return {
        "xAxis": {"data": ["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"]},
        "yAxis": {},
        "series": [
            {
                "type": "k",
                "data": [
                    [20, 34, 10, 38],
                    [40, 35, 30, 50],
                    [31, 38, 33, 44],
                    [38, 15, 5, 42],
                ],
            }
        ],
        "responsive": True,
    }

plot = get_plot()
pn.pane.ECharts(plot, min_height=700, sizing_mode="stretch_both").servable()
