from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from pymodbus.client.sync import ModbusTcpClient, ModbusClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim'

toggled1 = 'Toggled1'
untoggled1 = 'Untoggled1'
toggled2 = 'Toggled2'
untoggled2 = 'Untoggled2'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_toggled_rtu_status') 
def toggled_rtu_status():
    parser = reqparse.RequestParser()
    parser.add_argument("status")
    args = parser.parse_args()
    state = args["status"]

    if state == untoggled1:
        client = ModbusClient(method='rtu', port='/dev/ttyS0', timeout=1)
        client.write_coil(1, True)
        result = client.read_coils(1,1)
        print result.bits[0]
        client.close()

        new_state = toggled1
        print new_state
        return new_state
    else:
        client = ModbusClient(method='rtu', port='/dev/ttyS0', timeout=1)
        client.write_coil(1, False)
        result = client.read_coils(1,1)
        print result.bits[0]
        client.close()

        new_state = untoggled1
        print new_state
        return new_state


@app.route('/get_toggled_tcp_status') 
def toggled_tcp_status():
    parser = reqparse.RequestParser()
    parser.add_argument("status")
    args = parser.parse_args()
    state = args["status"]

    if state == untoggled2:
        client = ModbusTcpClient('192.168.137.112')
        client.write_coil(1, True)
        result = client.read_coils(1,1)
        print result.bits[0]
        client.close()

        new_state = toggled2
        print new_state
        return new_state
    else:
        client = ModbusTcpClient('192.168.137.112')
        client.write_coil(1, False)
        result = client.read_coils(1,1)
        print result.bits[0]
        client.close()

        new_state = untoggled2
        print new_state
        return new_state


if __name__ == "__main__":
    api = Api(app)
    app.run(host='0.0.0.0', debug=True)            
