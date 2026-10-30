# Physics — Mechanics calculator

An interactive, dependency-free Python 3.10+ calculator for basic mechanics.

## Run

Run `python physics.py` from this folder (or `py physics.py` on Windows). Choose force, kinetic energy, or weight, then enter your own values. Repeat calculations or enter q at the menu to quit. Ctrl+C or end-of-input exits cleanly.

## Units and formulas

- Force: F = ma, in newtons. Mass is kilograms; acceleration is m/s² and may be negative.
- Kinetic energy: E = 0.5mv², in joules. Speed is a nonnegative magnitude in m/s.
- Weight: W = mg, in newtons. Press Enter for Earth gravity of 9.81 m/s² or supply another nonnegative gravity.

Mass must be nonnegative. Invalid text, NaN, infinity, and overflowing results are rejected; you can return to the menu and try again. Results display six significant digits using floating-point arithmetic. This is an educational tool.

## Tests

Run `python -m unittest discover -v`.
Seven tests cover known values, zero values, signed acceleration, invalid inputs, overflow, full CLI sessions, error recovery, and end-of-input.

## Files

- physics.py: reusable calculations and interactive menu.
- test_physics.py: unit and subprocess tests.

No data is saved and no network connection is used.
