import panel as pn

from dataviz_in_python import config

config.configure(title="Introduction")

INTRODUCTION = """
## DataViz in Python

The Python visualization landscape can seem daunting at first. In this presentation I will give my 
take on the Python dataviz ecosystem.

I will be focusing on **browser based, interactive** dataviz.

For a general, up to date overview check out [PyViz.org](https://pyviz.org/).
"""

LANDSCAPE = "https://rougier.github.io/python-visualization-landscape/landscape-colors.png"

pn.Column(
    pn.panel(INTRODUCTION, css_classes=[config.TEXT_CLASS]),
    pn.layout.Divider(),
    pn.panel(LANDSCAPE, height=700, align="center"),
).servable()
