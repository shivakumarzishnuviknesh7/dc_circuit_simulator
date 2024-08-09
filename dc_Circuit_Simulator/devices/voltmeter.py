import asyncio
import time


class Voltmeter:
    def __init__(self, circuit):
        self.circuit = circuit
        self.last_voltage = 0
        self.last_timestamp = 0

    async def read_voltage(self):
        while time.time() - self.circuit.t_start <= 10:
            self.last_voltage = self.circuit.get_voltage()
            self.last_timestamp = time.time()
            print(f"[Voltmeter] Time: {self.last_timestamp - self.circuit.t_start:.2f}s, Voltage: {self.last_voltage:.2f}V")
            await asyncio.sleep(0.1)

    def get_last_value(self):
        return self.last_voltage, self.last_timestamp