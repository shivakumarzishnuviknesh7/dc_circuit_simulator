import asyncio
import time

from dc_Circuit_Simulator.devices.ohmmeter import Ohmmeter


class RollingAverageOhmmeter(Ohmmeter):
    def __init__(self, voltmeter, ammeter):
        super().__init__(voltmeter, ammeter)
        self.voltage_readings = []
        self.current_readings = []

    async def calculate_resistance(self):
        while time.time() - self.voltmeter.circuit.t_start <= 10:
            voltage, v_time = self.voltmeter.get_last_value()
            current, c_time = self.ammeter.get_last_value()

            # Store the readings with their timestamp
            self.voltage_readings.append((voltage, v_time))
            self.current_readings.append((current, c_time))

            # Remove readings older than 2 seconds
            self.voltage_readings = [(v, t) for v, t in self.voltage_readings if time.time() - t <= 2]
            self.current_readings = [(i, t) for i, t in self.current_readings if time.time() - t <= 2]

            if len(self.voltage_readings) > 0 and len(self.current_readings) > 0:
                avg_voltage = sum(v for v, t in self.voltage_readings) / len(self.voltage_readings)
                avg_current = sum(i for i, t in self.current_readings) / len(self.current_readings)
                if avg_current != 0:
                    RL_avg = avg_voltage / avg_current
                    print(
                        f"[RollingAverageOhmmeter] Time: {time.time() - self.voltmeter.circuit.t_start:.2f}s, Rolling Avg RL: {RL_avg:.2f}Ω")
            await asyncio.sleep(1)