machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

producing = set()

for machine, status in machines.items():

    if status == "Active":
        producing.add(machine)

print("Machine Status")

for machine, status in machines.items():
    print(machine, ":", status)

print("\nInferred Production Status")

for machine in machines:
    if machine in producing:
        print("Producing(", machine, ")")
    else:
        print("NOT Producing(", machine, ")")

print("\nProduct Availability")
print("Cannot be determined because Produces(machine, product) facts are not given.")

print("\nGear Production")
print("Cannot be determined from the given data.")