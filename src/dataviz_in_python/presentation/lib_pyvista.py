import json
import panel as pn
import pyvista as pv

from dataviz_in_python import config

config.configure("vtk", url="lib_vista", title="PyVista")

TEXT = """
# PyVista: 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK)

[PyVista](https://docs.pyvista.org/) PyVista is a helper module for the Visualization Toolkit (VTK) 
that takes a different approach on interfacing with VTK through NumPy and direct array access

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_pyvista.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default", accent_base_color="blue"):
    plotter = pv.Plotter()  # we define a pyvista plotter
    if theme == "dark":
        plotter.background_color = (0.13, 0.13, 0.13)
    else:
        plotter.background_color = (0.97, 0.97, 0.97)

    # we create a `VTK` panel around the render window
    pvcylinder = pv.Cylinder(resolution=8, direction=(0, 1, 0))
    cylinder_actor = plotter.add_mesh(pvcylinder, color=accent_base_color, smooth_shading=True)
    cylinder_actor.RotateX(30.0)
    cylinder_actor.RotateY(-45.0)
    plotter.add_mesh(
        pv.Sphere(theta_resolution=8, phi_resolution=8, center=(0.5, 0.5, 0.5)),
        color=accent_base_color,
        smooth_shading=True,
    )
    return plotter.ren_win


plot = get_plot(theme=config.get_theme(), accent_base_color=config.ACCENT_BASE_COLOR)
pn.panel(plot, height=700, sizing_mode="stretch_both").servable()
