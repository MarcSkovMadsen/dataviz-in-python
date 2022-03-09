import numpy as np
import pandas as pd
import panel as pn

from dataviz_in_python import config

config.configure(title="Streaming")

TEXT = """
# Streaming: Live data or story telling with a time dimension

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/streaming.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()

layout = pn.layout.FlexBox(
    *(
        pn.indicators.Trend(
            data={"x": list(range(10)), "y": np.random.randn(10).cumsum()},
            width=200,
            height=150,
            plot_type=pn.indicators.Trend.param.plot_type.objects[i % 4],
        )
        for i in range(36)
    )
).servable()


def stream():
    for trend in layout:
        trend.stream(
            {"x": [trend.data["x"][-1] + 1], "y": [trend.data["y"][-1] + np.random.randn()]},
            rollover=20,
        )


cb = pn.state.add_periodic_callback(stream, 500)
