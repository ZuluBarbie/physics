"""Interactive mechanics calculator using SI units (Python 3.10+)."""
import math


def number(value, name, nonnegative=False):
    try:
        value = float(value)
    except (ValueError, TypeError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number.") from exc
    if not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number.")
    if nonnegative and value < 0:
        raise ValueError(f"{name} cannot be negative.")
    return value


def finite_result(value):
    if not math.isfinite(value):
        raise ValueError("Result too large; use smaller inputs.")
    return value


def force(mass, acceleration):
    """Signed force in N; mass in kg, acceleration in m/s^2."""
    return finite_result(number(mass, "Mass", True) * number(acceleration, "Acceleration"))


def kinetic_energy(mass, speed):
    """Energy in J; mass in kg and nonnegative speed in m/s."""
    m = number(mass, "Mass", True)
    v = number(speed, "Speed", True)
    return finite_result(0.5 * m * v * v)


def weight(mass, gravity=9.81):
    """Weight magnitude in N; gravity magnitude in m/s^2."""
    return finite_result(number(mass, "Mass", True) * number(gravity, "Gravity", True))


def main():
    calculations = {
        "1": (force, "Acceleration (m/s^2): ", "Force", "N"),
        "2": (kinetic_energy, "Speed (m/s): ", "Kinetic energy", "J"),
        "3": (weight, "Gravity (m/s^2; Enter for 9.81): ", "Weight", "N"),
    }
    print("PHYSICS | Mechanics calculator (SI units)")
    while True:
        try:
            choice = input("\n1 Force | 2 Kinetic energy | 3 Weight | q Quit\nChoose: ").strip().lower()
            if choice == "q":
                break
            if choice not in calculations:
                print("Choose 1, 2, 3, or q.")
                continue
            calculate, prompt, label, unit = calculations[choice]
            mass = input("Mass (kg): ")
            other = input(prompt).strip()
            if choice == "3" and not other:
                other = "9.81"
            print(f"{label}: {calculate(mass, other):.6g} {unit}")
        except ValueError as exc:
            print(f"Error: {exc}")
        except (EOFError, KeyboardInterrupt):
            print()
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()
