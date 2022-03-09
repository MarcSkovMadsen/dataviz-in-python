import panel as pn
import vtk

from vtk.util.colors import tomato

from dataviz_in_python import config

config.configure("vtk", url="lib_vtk", title="VTK")

TEXT = """
# VTK: Process images and create 3D computer graphics with the Visualization Toolkit.

[VTK](https://vtk.org/) is open source software for manipulating and 
displaying scientific data. It comes with state-of-the-art tools for 3D 
rendering, a suite of widgets for 3D interaction, and extensive 2D 
plotting capability.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_vtk.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default", accent_base_color="red"):
    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(tomato)
    # We must set ScalarVisibilty to 0 to use tomato Color
    cylinderMapper.SetScalarVisibility(0)
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # Create the graphics structure. The renderer renders into the render
    # window.
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)

    # Add the actors to the renderer, set the background and size
    ren.AddActor(cylinderActor)
    if theme == "dark":
        ren.SetBackground(0.13, 0.13, 0.13)
    else:
        ren.SetBackground(0.97, 0.97, 0.97)
    return renWin

plot = get_plot(theme=config.get_theme())
component = pn.pane.VTK(plot, height=700, sizing_mode="stretch_both").servable()