from pyscript import display
import sys
import FreeSimpleGUI as sg

layout = [[sg.T("ICH FRESS NEN BESEN")]]

w = sg.Window(title="GEIL", layout=layout)

w.read()

while True:
  e, v = w.read()

  if e is None:
    w.close()
    break
