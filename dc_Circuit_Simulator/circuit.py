import asyncio
import time


class CircuitSimulator:
    def __init__(self, VS=10, RL=30000):
        self.VS = VS
        self.RL = RL
        self.R1 = 0
        self.R2 = 100000
        self.t_start = time.time()

    def update_resistances(self):
        elapsed_time = time.time() - self.t_start
        if elapsed_time > 10:
            elapsed_time = 10
        self.R1 = (100000 / 10) * elapsed_time
        self.R2 = 100000 - self.R1

    def get_voltage(self):
        total_resistance = self.R1 + self.RL + self.R2
        if total_resistance == 0:
            return 0
        return self.VS * (self.RL / total_resistance)

    def get_current(self):
        total_resistance = self.R1 + self.RL + self.R2
        if total_resistance == 0:
            return 0
        return self.VS / total_resistance

    async def start_simulation(self):
        self.t_start = time.time()
        while time.time() - self.t_start <= 10:
            self.update_resistances()
            await asyncio.sleep(0.1)