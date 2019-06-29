from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from pymodbus.client.sync import ModbusTcpClient, ModbusSerialClient
import logging


PORT = '/dev/ttyS0'
IP_ADDRESS = '192.168.137.112'


FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
RTU_TOGGLED = 'Toggled1'
RTU_UNTOGGLED = 'Untoggled1'
TCP_TOGGLED = 'Toggled2'
TCP_UNTOGGLED = 'Untoggled2'
UNIT = 0x01


app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim'
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_toggled_rtu_status') 
def toggled_rtu_status():
    parser = reqparse.RequestParser()
    parser.add_argument("status")
    args = parser.parse_args()
    state = args["status"]

    if state == RTU_UNTOGGLED:
        write_via_rtu_modbus(True)
        new_state = RTU_TOGGLED
        print new_state
        return new_state
    else:
        write_via_rtu_modbus(False)
        new_state = RTU_UNTOGGLED
        print new_state
        return new_state

@app.route('/get_toggled_tcp_status') 
def toggled_tcp_status():
    parser = reqparse.RequestParser()
    parser.add_argument("status")
    args = parser.parse_args()
    state = args["status"]

    if state == TCP_UNTOGGLED:
        write_via_tcp_modbus(True)
        new_state = TCP_TOGGLED
        print new_state
        return new_state
    else:
        write_via_tcp_modbus(False)
        new_state = TCP_UNTOGGLED
        print new_state
        return new_state


def write_via_rtu_modbus(state):
    client = ModbusSerialClient(method='rtu', port=PORT, timeout=1, baudrate=460800)
    log.debug("Writing Coils")
    rq = client.write_coil(1, state, unit=UNIT)
    log.debug(rq)
    log.debug("Reading Coils")
    rr = client.read_coils(1, 1, unit=UNIT)
    log.debug(rr)
    client.close()


def write_via_tcp_modbus(state):
    client = ModbusTcpClient(IP_ADDRESS)
    client.write_coil(1, state)
    result = client.read_coils(1, 1)
    print result.bits[0]
    client.close()


if __name__ == "__main__":
    api = Api(app)
    app.run(host='0.0.0.0', debug=True)            
