import sys
sys.path.append("/home/mountainsensing/database-scripts/")

from data_dump import DataDump
from datetime import datetime

LIVE_CONFIG = "/home/pjb/database-scripts/db.ini"

def index(req):
	output = """<html><head>
		<title>Feshie Data Overview</title>
		</head>
		<body><h1>Feshie Data Overview</h1>
		<p>As at """
	output += str(datetime.utcnow())
	LIVE_DUMPER = DataDump(LIVE_CONFIG)
	LIVE_LATEST = LIVE_DUMPER.get_latest_readings()
	output += """<table><tr><th>Node</th><th>Latest</th></tr>"""
	for node in LIVE_LATEST:
		output +="<tr><td>%s</td><td>%s</td></tr>"% (node[0], node[2])
	output +="</table>"
	output += """
	<h3>Combined Graphs</h3>
	<a href="graph.py?sensor=temp">Temperature</a><br/>
	<a href="graph.py?sensor=batt">Battery</a><br/>
	<a href="graph.py?sensor=mppt">Max Power Point Tracking</a><br/>
	<a href="graph.py?sensor=soc">State of Charge</a><br/>
	<a href="graph.py?sensor=solar">Solar Charge Current</a><br/>
	<a href="graph.py?sensor=adc&adc_id=1">ADC 1</a><br/>
	<a href="graph.py?sensor=adc&adc_id=2">ADC 2</a><br/>
	<a href="graph.py?sensor=moisture">Moisture</a><br/>
	<a href="graph.py?sensor=rain">Rainfall</a><br/>
	"""
	
	LIVE_NODES = LIVE_DUMPER.get_nodes()
	output += "<h3>Node specific graphs</h3>"
	output += """<table>"""
	for node in LIVE_NODES:
		output += "<tr><td>%s</td>" % node
		output += "<td><a href = \"graph.py?sensor=accel&node=%s\">Accelerometer</a></td>" % node
		output += "<td><a href = \"graph.py?sensor=ow&node=%s\">Spider</a></td>" % node
		output += "<td><a href = \"graph.py?sensor=wp&node=%s\">Water Pressure</a></td>" % node
		output += "<td><a href = \"graph.py?sensor=chain&node=%s\">Chain</a></td>" % node
		output +="</tr>"
	output +="</table>"
	output +="</body></html>"
	return output
