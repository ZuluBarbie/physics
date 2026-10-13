"""Simple mechanics calculations using SI units."""


def force(mass, acceleration):
    """Return force in newtons for mass in kg and acceleration in m/s²."""
    return mass * acceleration


def kinetic_energy(mass, speed):
    """Return kinetic energy in joules for mass in kg and speed in m/s."""
    return 0.5 * mass * speed ** 2


def weight(mass, gravity=9.81):
    """Return weight in newtons for mass in kg and gravity in m/s²."""
    return mass * gravity


if __name__ == "__main__":
    print(f"Force (2 kg, 3 m/s²): {force(2, 3):.2f} N")
    print(f"Kinetic energy (2 kg, 4 m/s): {kinetic_energy(2, 4):.2f} J")
    print(f"Weight on Earth (2 kg): {weight(2):.2f} N")
