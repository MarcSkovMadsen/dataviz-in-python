import hvplot.xarray  # noqa
import panel as pn
import xarray as xr
from dataviz_in_python import config

config.configure(url="lib_datashader", title="Datashader")

TEXT = """
# Datashader: Accurately render even the largest data

[Datashader](https://datashader.org/) is something unique in the Python ecosystem. It enables you 
to interactively explore big data of Terabyte or even Peta byte scale. For 
example for use cases at Cern, at intelligence Institutions.

You would be using it in combination with [hvplot](lib_hvplot), 
[Holoviews](lib_holoviews) or [Plotly](lib_plotly).

Rapids by NVidia bases their [CuxFilter](https://github.com/rapidsai/cuxfilter) 
framework on Datashader, HoloViews and Panel. For more inspiration see [Google Search](https://www.google.com/search?q=datashader+youtube)

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_datashader.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()

if not "air" in pn.state.cache:
    air = pn.state.cache["air"] = xr.tutorial.open_dataset("air_temperature").load().air
else:
    air = pn.state.cache["air"]


def get_plot(accent_base_color="blue"):
    plot = air.hvplot.scatter(
        "time",
        groupby=[],
        rasterize=True,
        dynspread=True,
        responsive=True,
        cmap="YlOrBr",
        colorbar=True,
    ) * air.mean(["lat", "lon"]).hvplot.line("time", color=accent_base_color, responsive=True)
    plot.opts(responsive=True, active_tools=["box_zoom"])
    return plot


plot = get_plot(accent_base_color=config.ACCENT_BASE_COLOR)

pn.pane.HoloViews(plot, min_height=600, sizing_mode="stretch_both").servable()
