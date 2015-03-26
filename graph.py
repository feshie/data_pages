
def index(req):
    url = "http://data.mountainsensing.org/feshie/data/data.py?sensor=temp"
    output = ""
    output += """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7; IE=EmulateIE9"> 
        <!--[if IE]><script src="excanvas.js"></script><![endif]-->
    <title> Glacsweb TinyTag Data """

    output += """
    </title>
    <script type="text/javascript"
      src="dygraph-combined.js"></script>
    </head>
    <body>
    <h1> Glacsweb Davis Tinytag Data"""

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