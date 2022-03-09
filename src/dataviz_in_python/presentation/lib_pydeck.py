import pydeck
import panel as pn

from dataviz_in_python import config

config.configure("deckgl", url="lib_pydeck", title="PyDeck")

TEXT = """
# PyDeck: High-scale spatial rendering in Python, powered by deck.gl.

[PyDeck](https://deckgl.readthedocs.io/en/latest/) is a Python wrapper for [deck.gl](lib_deckgl).

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_deckgl.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default", accent_base_color="blue"):
    LAND_COVER = [[[-123.0, 49.196], [-123.0, 49.324], [-123.306, 49.324], [-123.306, 49.196]]]
    polygon = pydeck.Layer(
        "PolygonLayer",
        LAND_COVER,
        stroked=False,
        # processes the data as a flat longitude-latitude pair
        get_polygon="-",
        get_fill_color=[0, 0, 0, 20],
    )

    DATA_URL = "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
    geojson = pydeck.Layer(
        "GeoJsonLayer",
        DATA_URL,
        opacity=0.8,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation="properties.valuePerSqm / 20",
        get_fill_color="[255, 255, properties.growth * 255]",
        get_line_color=[255, 255, 255],
        pickable=True,
    )

    if theme == "dark":
        deckgl_map_style = "mapbox://styles/mapbox/dark-v9"
    else:
        deckgl_map_style = "mapbox://styles/mapbox/light-v9"
    MAPBOX_KEY = (
        "pk.eyJ1IjoicGFuZWxvcmciLCJhIjoiY2s1enA3ejhyMWhmZjNobjM1NXhtbWRrMyJ9.B_frQsAVepGIe-HiOJeqvQ"
    )
    INITIAL_VIEW_STATE = pydeck.ViewState(
        latitude=49.254, longitude=-123.13, zoom=11, max_zoom=16, pitch=45, bearing=0
    )

    r = pydeck.Deck(
        api_keys={"mapbox": MAPBOX_KEY},
        layers=[polygon, geojson],
        initial_view_state=INITIAL_VIEW_STATE,
        map_style=deckgl_map_style,
    )

    # Tooltip (you can get the id directly from the layer object)
    geojson_tooltip = {
        "html": """
        <b>Value per Square meter:</b> {properties.valuePerSqm}<br>
        <b>Growth:</b> {properties.growth}
        """,
        "style": {"backgroundColor": accent_base_color, "color": "white"},
    }
    tooltips = {geojson.id: geojson_tooltip}
    return r, tooltips


plot, tooltips = get_plot()

pn.pane.DeckGL(plot, tooltips=tooltips, height=800, sizing_mode="stretch_both").servable()
