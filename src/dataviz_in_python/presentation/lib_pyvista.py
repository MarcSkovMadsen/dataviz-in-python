import json
import panel as pn

from pyecharts.charts import Bar

pn.extension("vtk", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="PyVista",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    plotter = pv.Plotter()  # we define a pyvista plotter
    if theme == "dark":
        plotter.background_color = (0.13, 0.13, 0.13)
    else:
        plotter.background_color = (0.97, 0.97, 0.97)

    # we create a `VTK` panel around the render window
    pvcylinder = pv.Cylinder(resolution=8, direction=(0, 1, 0))
    cylinder_actor = plotter.add_mesh(
        pvcylinder, color=accent_base_color, smooth_shading=True
    )
    cylinder_actor.RotateX(30.0)
    cylinder_actor.RotateY(-45.0)
    plotter.add_mesh(
        pv.Sphere(theta_resolution=8, phi_resolution=8, center=(0.5, 0.5, 0.5)),
        color=accent_base_color,
        smooth_shading=True,
    )
    return plotter.ren_win

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.panel(plot, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()