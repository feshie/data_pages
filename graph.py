from mod_python import util

BASE_URL = "http://data.mountainsensing.org/feshie/data/data.py"
BASE_TITLE = "Feshie Mountain Sensing: "

def index(req):
    parameters = util.FieldStorage(req, keep_blank_values=1)
    if not "sensor" in parameters.keys():
        return "Must specify sensor type"
    sensor = parameters.getfirst("sensor")
    if sensor in ["temperature", "temp"]:
        url = BASE_URL + "?sensor=temp"
        title = BASE_TITLE + "Temperature"
    elif sensor in ["battery", "batt", "batts"]:
        url = BASE_URL + "?sensor=batt"
        title = BASE_TITLE + "Battery"
    elif sensor in ["accelerometer", "accel"]:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        url = BASE_URL + "?sensor=accel&node=" + node
        title = "Accelerometer:" + node
    elif sensor in ["analog", "adc", "adcs"]:
        if not "adc_id" in parameters.keys():
            return "Must specify adc_id for this sensor type"
        adc = parameters.getfirst("adc_id")
        title = "ADC %s" % adc
        url = BASE_URL + "?sensor=adc&adc_id=" + adc
    elif sensor in ["onewire", "ow", "one-wire"]:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")  
        title = "One Wire:" + node 
        url = BASE_URL + "?sensor=ow&node=" + node
    elif sensor in ["water", "wp", "smart-analog"]:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        title = "Water pressure:" + node
        url = BASE_URL + "?sensor=wp&node=" + node
    elif sensor in ["chain", "tad"]:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        title = "Chain data:" + node
        url = BASE_URL + "?sensor=chain&node=" + node
    else:
        return "Unknown sensor type"
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
        height: 600,
        width: 800,
        lengend: "always",
        showRoller: true
        }
    );
</script>
</body>
</html>
"""
    return output