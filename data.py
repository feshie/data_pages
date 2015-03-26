from mod_python import util
from logging import CRITICAL

import sys
sys.path.append("/home/pjb/database-scripts/")

from data_dump import DataDump, csv_convert

LIVE_CONFIG = "/home/pjb/database-scripts/db.ini"
TEST_CONFIG = "/home/pjb/database-scripts/db_test.ini"

def index(req):
    output = ""
    parameters = util.FieldStorage(req, keep_blank_values=1)
    if "sensor" in parameters.keys():
    	req.content_type = "text/csvi"
    else:
    	return "Must specify sensor type"

    if "test" in parameters.keys():
        DUMPER = DataDump(TEST_CONFIG, CRITICAL)
    else:
    	DUMPER = DataDump(LIVE_CONFIG, CRITICAL)
    
    sensor = parameters.getfirst("sensor")
    if sensor in ["temperature", "temp"]:
    	output += csv_convert(DUMPER.get_temperature_readings())
    elif sensor in ["battery", "batt", "batts"]:
        output += csv_convert(DUMPER.get_battery_readings())
    elif sensor in ["accelerometer", "accel"]:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        output += csv_convert(DUMPER.get_accelerometer_readings(node))
    else:
        output += "Invalid sensor type"
    return output