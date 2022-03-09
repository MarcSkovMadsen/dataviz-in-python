import panel as pn

from dataviz_in_python import config

config.configure(title="Considerations")

TEXT = """
What data visualization tool or framework to pick depends on your **use case, experience, 
preferences, team and much more**.

- Do you need something for quick data exploration, business communication or highly specialized use cases?
- Will this be a part of an interactive data app built using Dash, Jupyter Voila, Panel, Streamlit, Angular etc.?
- How will you deploy and share with users?

I would always recommend to **start out with the Pandas .plot api** or something very similar if possible.

But visualization is not only plots. Its also interactive images, tables etc. And closely related are other formats like Audio, Video etc.
"""

pn.Column(
    pn.panel(TEXT, css_classes=[config.TEXT_CLASS])
).servable()
