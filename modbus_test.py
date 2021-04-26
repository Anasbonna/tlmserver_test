import time
import copy
from threading import Thread, Lock

from pymodbus.client.sync import ModbusTcpClient
from flask import Flask, jsonify

reg_1 = []
reg_2 = []


def thread_function_1():
    client = ModbusTcpClient(host='127.0.0.1', port=502)
    op_counter = 0

    while True:
        start = time.perf_counter()
        result = client.read_holding_registers(unit=1, address=0, count=10)
        op_counter += 1
        global reg_1
        reg_1 = copy.deepcopy(result.registers)
        end = time.perf_counter()

        print(f'[Thread 1] operation #{op_counter:04d}:')
        print(result)
        print(result.registers)
        print(f'operation ends in {end - start:2.2f} s\n')

    client.close()


def thread_function_2():
    client = ModbusTcpClient(host='127.0.0.1', port=503)
    op_counter = 0

    while True:
        start = time.perf_counter()
        result = client.read_holding_registers(unit=1, address=0, count=10)
        op_counter += 1
        global reg_2
        reg_2 = copy.deepcopy(result.registers)
        end = time.perf_counter()

        print(f'[Thread 2] operation #{op_counter:04d}:')
        print(result)
        print(result.registers)
        print(f'operation ends in {end - start:2.2f} s\n')

    client.close()


th1 = Thread(target=thread_function_1)
th1.start()
th2 = Thread(target=thread_function_2)
th2.start()

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = {
        'device_1': copy.deepcopy(reg_1),
        'device_2': copy.deepcopy(reg_2)
    }

    return jsonify(data)


app.run()
