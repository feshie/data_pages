import sys
sys.path.append("/home/mountainsensing/database-scripts/")

from data_dump import DataDump
from datetime import datetime

LIVE_CONFIG = "/home/pjb/database-scripts/db.ini"
TEST_CONFIG = "/home/pjb/database-scripts/db_test.ini"

def index(req):
	output = """<html><head>
		<title>Feshie Data Overview</title>
		</head>
		<body><h1>Feshie Data Overview</h1>
		<p>As at """
	output += str(datetime.utcnow())
	output += """ UTC</p>
		<div style="width:50%; float:left; background-color:#E78B7E">
		<h2>Test Data</h2>"""
	TEST_DUMPER = DataDump(TEST_CONFIG)
	TEST_LATEST = TEST_DUMPER.get_latest_readings()
	output += """<table><tr><th>Node</th><th>Latest</th></tr>"""
	for node in TEST_LATEST:
		output +="<tr><td>%s</td><td>%s</td></tr>"% (node[0], node[1])
	output +="</table>"
	output += """
	<h3>Combined Graphs</h3>
	<a href="graph.py?test&sensor=temp">Temperature</a><br/>
	<a href="graph.py?test&sensor=batt">Battery</a><br/>
	<a href="graph.py?test&sensor=adc&adc_id=1">ADC 1</a><br/>
	<a href="graph.py?test&sensor=adc&adc_id=2">ADC 2</a><br/>
	<a href="graph.py?test&sensor=moisture">Moisture</a><br/>
	<a href="graph.py?test&sensor=rain">Rainfall</a><br/>
	"""
	
	TEST_NODES = TEST_DUMPER.get_nodes()
	output += "<h3>Node specific graphs</h3>"
	output += """<table>"""
	for node in TEST_NODES:
		output += "<tr><td>%s</td>" % node
		output += "<td><a href = \"graph.py?test&sensor=accel&node=%s\">Accelerometer</a></td>" % node
		output += "<td><a href = \"graph.py?test&sensor=ow&node=%s\">Spider</a></td>" % node
		output += "<td><a href = \"graph.py?test&sensor=wp&node=%s\">Water Pressure</a></td>" % node
		output += "<td><a href = \"graph.py?test&sensor=chain&node=%s\">Chain</a></td>" % node
		output +="</tr>"
	output +="</table></div>"



	output += "<div style=\"width:50%; float:right; background-color:#A2E382\"><h2>LIVE Data</h2>"
	LIVE_DUMPER = DataDump(LIVE_CONFIG)
	LIVE_LATEST = LIVE_DUMPER.get_latest_readings()
	output += """<table><tr><th>Node</th><th>Latest</th></tr>"""
	for node in LIVE_LATEST:
		output +="<tr><td>%s</td><td>%s</td></tr>"% (node[0], node[1])
	output +="</table>"
	output += """
	<h3>Combined Graphs</h3>
	<a href="graph.py?sensor=temp">Temperature</a><br/>
	<a href="graph.py?sensor=batt">Battery</a><br/>
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
	output +="</table></div>"
	output +="</body></html>"
	return output
