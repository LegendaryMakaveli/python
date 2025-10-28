from fuel import Fuel
from dispenser_machine import DispenserMachine
from fuel_attendant import FuelAttendant


def main():
    print("⛽ Fuel Dispenser System\n")
    machine = DispenserMachine({})
    attendant = FuelAttendant("Mary")

    print(f"Attendant on duty: {attendant.name}\n")

    print("Adding new fuels...")
    attendant.add_new_fuel(machine, "Petrol", 5.0, 500.0)
    attendant.add_new_fuel(machine, "Diesel", 6.5, 300.0)
    attendant.add_new_fuel(machine, "Kerosene", 4.0, 200.0)
    print("Fuels added successfully.\n")

    print("Current Fuel Inventory:")
    for info in machine.get_available_fuel():
        print("  -", info)

    print("Updating Diesel price...")
    result = attendant.update_fuel_price(machine, "Diesel", 7.2)
    print(result)

    print("Dispensing 50L of Petrol...")
    try:
        cost = machine.dispense_fuel("Petrol", 50.0)
        print(f"Transaction successful! You bought 50L of Petrol for ₦{cost:.2f}")
    except ValueError as error:
        print(f"❌ Transaction failed: {error}")

    print("Updated Fuel Inventory:")
    for info in machine.get_available_fuel():
        print("  -", info)

    print("\nSystem shutting down...")


if __name__ == "__main__":
    main()
