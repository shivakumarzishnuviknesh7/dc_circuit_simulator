import asyncio

from dc_Circuit_Simulator.circuit import CircuitSimulator
from dc_Circuit_Simulator.devices.RollingAverageOhmmeter import RollingAverageOhmmeter
from dc_Circuit_Simulator.devices.ammeter import Ammeter
from dc_Circuit_Simulator.devices.ohmmeter import Ohmmeter
from dc_Circuit_Simulator.devices.voltmeter import Voltmeter


async def main():
    circuit = CircuitSimulator()
    voltmeter = Voltmeter(circuit)
    ammeter = Ammeter(circuit)
    ohmmeter = Ohmmeter(voltmeter, ammeter)
    rolling_ohmmeter = RollingAverageOhmmeter(voltmeter, ammeter)

    await asyncio.gather(
        circuit.start_simulation(),
        voltmeter.read_voltage(),
        ammeter.read_current(),
        ohmmeter.calculate_resistance(),
        rolling_ohmmeter.calculate_resistance()
    )

if __name__ == "__main__":
    asyncio.run(main())