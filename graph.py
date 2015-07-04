from mod_python import util

from aliases import *

BASE_URL = "http://data.mountainsensing.org/feshie/data/data.py"
BASE_TITLE = "Feshie Mountain Sensing: "



def index(req):
    parameters = util.FieldStorage(req, keep_blank_values=1)
    url = BASE_URL
    if not "sensor" in parameters.keys():
        return "Must specify sensor type"
    sensor = parameters.getfirst("sensor")
    if sensor in TEMPERATURE_ALIASES:
        url = BASE_URL + "?sensor=temp"
        title = BASE_TITLE + "Temperature"
    elif sensor in BATTERY_ALIASES:
        url = BASE_URL + "?sensor=batt"
        title = BASE_TITLE + "Battery"
    elif sensor in ACCELEROMETER_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        url = BASE_URL + "?sensor=accel&node=" + node
        title = "Accelerometer:" + node
    elif sensor in ADC_ALIASES:
        if not "adc_id" in parameters.keys():
            return "Must specify adc_id for this sensor type"
        adc = parameters.getfirst("adc_id")
        title = "ADC %s" % adc
        url = BASE_URL + "?sensor=adc&adc_id=" + adc
    elif sensor in ONE_WIRE_ALISES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")  
        title = "One Wire:" + node 
        url = BASE_URL + "?sensor=ow&node=" + node
    elif sensor in WATER_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        title = "Water pressure:" + node
        url = BASE_URL + "?sensor=wp&node=" + node
    elif sensor in CHAIN_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        title = "Chain data:" + node
        url = BASE_URL + "?sensor=chain&node=" + node
    elif sensor in CHAIN_TEMPERATURE_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        title = "Chain Temperature data:" + node
        url = BASE_URL + "?sensor=chain-temperature&node=" + node
    elif sensor in MOISTURE_ALIASES:
        url = BASE_URL + "?sensor=moisture"
        title = BASE_TITLE + "Moisture Data"
    elif sensor in RAIN_ALIASES:
        url = BASE_URL + "?sensor=rain"
        title = BASE_TITLE + "Rain Data"
    else:
        return "Unknown sensor type"
    if "test" in parameters.keys():
        url += "&test"
    output = ""
    output += """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7; IE=EmulateIE9"> 
        <!--[if IE]><script src="excanvas.js"></script><![endif]-->
    <title> """
    output += title
    output += """
    </title>
    <script type="text/javascript"
      src="dygraph-combined.js"></script>
    </head>
    <body>
    <h1>"""
    output += title
    output +="""</h1>
    <p>To zoom on the graph highlight the region you would like to zoom in on, this works with both the X and Y axis.  To return the graph to showing all data double click on it</p>
    <div id="tempdiv"></div>
    <script type="text/javascript">
      g = new Dygraph(
        document.getElementById("tempdiv"),\""""
    output += url

    output += """\",{
        xlabel: "Date",
        height: 600,
        width: 800,
        lengend: "always",
        showRoller: true,
        ylabel:"""
    if sensor in TEMPERATURE_ALIASES + ONE_WIRE_ALISES + CHAIN_TEMPERATURE_ALIASES:
        output += "\"Temperature (c)\",\n"
    elif sensor in BATTERY_ALIASES:
        output += "\"Voltage (V)\",\n"
    elif sensor in WATER_ALIASES:
        output += "\"Pressure (mb)\",\n"
    elif sensor in ACCELEROMETER_ALIASES:
        output +="\"Angle (degrees)\",\n"
    elif sensor in RAIN_ALIASES:
        output += "\"Rainfall (mm/h)\",\n"
    elif sensor in CHAIN_ALIASES:
        output += "\"Angle (degrees)\",\n"
        output += "series: {'Temp 1':{axis:'y2'}, 'Temp 2':{axis:'y2'}, 'Temp 3':{axis:'y2'}, 'Temp 4':{axis: 'y2'},},axes:{y2:{labelsKMB: true}},y2label: 'Temperature (C)',"
    else:
        output += "\"counts\",\n"

    output +="""    }
    );
</script>
</body>
</html>
"""
    return output
