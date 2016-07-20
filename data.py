from mod_python import util
from logging import CRITICAL

import sys
sys.path.append("/home/pjb/database-scripts/")

from data_dump import DataDump, csv_convert
from aliases import *

LIVE_CONFIG = "/home/mountainsensing/database-scripts/db.ini"
TEST_CONFIG = "/home/pjb/database-scripts/db_test.ini"

def index(req):
    output = ""
    parameters = util.FieldStorage(req, keep_blank_values=1)
    if not "sensor" in parameters.keys():
    	return "Must specify sensor type"

    if "test" in parameters.keys():
        DUMPER = DataDump(TEST_CONFIG, CRITICAL)
    else:
    	DUMPER = DataDump(LIVE_CONFIG, CRITICAL)
    
    sensor = parameters.getfirst("sensor")
    if sensor in TEMPERATURE_ALIASES:
    	output += csv_convert(DUMPER.get_temperature_readings())
    elif sensor in BATTERY_ALIASES:
        output += csv_convert(DUMPER.get_battery_readings())
    elif sensor in MOISTURE_ALIASES:
        output += csv_convert(DUMPER.get_moisture_readings())
    elif sensor in RAIN_ALIASES:
        output += csv_convert(DUMPER.get_rain_readings())
    elif sensor in MPPT_ALIASES:
        output += csv_convert(DUMPER.get_mppt_readings())
    elif sensor in SOC_ALIASES:
        output += csv_convert(DUMPER.get_soc_readings())
    elif sensor in SOLAR_CURRENT_ALIASES:
        output += csv_convert(DUMPER.get_solar_current_readings())
    elif sensor in ACCELEROMETER_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        output += csv_convert(DUMPER.get_accelerometer_readings(node))
    elif sensor in ADC_ALIASES:
        if not "adc_id" in parameters.keys():
            return "Must specify adc_id for this sensor type"
        adc = parameters.getfirst("adc_id")
        output += csv_convert(DUMPER.get_adc_readings(adc))
    elif sensor in ONE_WIRE_ALISES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        output += csv_convert(DUMPER.get_onewire_readings(node))
    elif sensor in WATER_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        output += csv_convert(DUMPER.get_analog_smart_readings(node))
    elif sensor in CHAIN_ALIASES:
        if not "node" in parameters.keys():
            return "Must specify node for this sensor type"
        node = parameters.getfirst("node")
        output += csv_convert(DUMPER.get_chain_readings(node))
    else:
        output += "Invalid sensor type"
    req.content_type = "text/csvi"
    return output
