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