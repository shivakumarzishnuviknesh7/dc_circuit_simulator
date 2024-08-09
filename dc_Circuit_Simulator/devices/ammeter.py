import asyncio
import time


class Ammeter:
    def __init__(self, circuit):
        self.circuit = circuit
        self.last_current = 0
        self.last_timestamp = 0

    async def read_current(self):
        while time.time() - self.circuit.t_start <= 10:
            self.last_current = self.circuit.get_current()
            self.last_timestamp = time.time()
            print(f"[Ammeter] Time: {self.last_timestamp - self.circuit.t_start:.2f}s, Current: {self.last_current:.2e}A")
            await asyncio.sleep(0.3)

    def get_last_value(self):
        return self.last_current, self.last_timestamp