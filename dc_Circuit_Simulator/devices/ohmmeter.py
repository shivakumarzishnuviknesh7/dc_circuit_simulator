import asyncio
import time


class Ohmmeter:
    def __init__(self, voltmeter, ammeter):
        self.voltmeter = voltmeter
        self.ammeter = ammeter

    async def calculate_resistance(self):
        while time.time() - self.voltmeter.circuit.t_start <= 10:
            voltage, _ = self.voltmeter.get_last_value()
            current, _ = self.ammeter.get_last_value()
            if current != 0:
                RL = voltage / current
                print(f"[Ohmmeter] Time: {time.time() - self.voltmeter.circuit.t_start:.2f}s, Calculated RL: {RL:.2f}Ω")
            await asyncio.sleep(1)