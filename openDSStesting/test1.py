import py_dss_interface

dss = py_dss_interface.DSS()

dss.text("clearall")
dss.text(r"compile C:\Users\jilli\OneDrive - University of Pittsburgh\Desktop\ECE 1893\OpenDSS_Basics\13Bus\IEEE13Nodeckt.dss")
dss.text("solve")
dss.text("Show Voltage LN Nodes")
dss.text("FormEdit Line.LINE1")