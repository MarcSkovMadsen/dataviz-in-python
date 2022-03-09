import panel as pn

from dataviz_in_python import config

config.configure(title="Considerations")

TEXT = """
What data visualization to pick depends on your **use case, experience, preferences, team and much more**.

- Do you need a high resolution static visualization? Or do you need a interactive visualization for use in browser?
- Do you need something for quick data exploration? Or do you need something for business communication? Or do you need something for highly specialized use cases?

I would always recommend to **start out with the Pandas .plot api** or something very similar if possible.
"""

pn.Column(
    pn.panel(TEXT, css_classes=[config.TEXT_CLASS])
).servable()
