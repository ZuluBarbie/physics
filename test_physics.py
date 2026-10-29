import subprocess
import sys
import unittest
from pathlib import Path
from physics import force, kinetic_energy, weight


class PhysicsTests(unittest.TestCase):
    def test_known_results(self):
        self.assertEqual(force(2, 3), 6)
        self.assertEqual(force(2, -3), -6)
        self.assertEqual(kinetic_energy(2, 4), 16)
        self.assertAlmostEqual(weight(2), 19.62)
        self.assertAlmostEqual(weight(2, 1.62), 3.24)

    def test_zero(self):
        for fn in (force, kinetic_energy, weight):
            self.assertEqual(fn(0, 0), 0)

    def test_invalid_inputs(self):
        for fn in (force, kinetic_energy, weight):
            for invalid in ('abc', None, float('nan'), float('inf')):
                with self.subTest(fn=fn.__name__, value=invalid):
                    with self.assertRaises(ValueError):
                        fn(invalid, 2)
                    with self.assertRaises(ValueError):
                        fn(2, invalid)
            with self.assertRaises(ValueError):
                fn(-1, 2)
        for fn in (kinetic_energy, weight):
            with self.assertRaises(ValueError):
                fn(2, -1)

    def test_overflow(self):
        for fn in (force, kinetic_energy, weight):
            with self.assertRaises(ValueError):
                fn(1e308, 1e308)

    def run_cli(self, inputs):
        result = subprocess.run([sys.executable, str(Path(__file__).with_name('physics.py'))],
                                input=inputs, text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_full_session(self):
        output = self.run_cli('1\n2\n3\n2\n2\n4\n3\n2\n\nq\n')
        for expected in ('Force: 6 N', 'Kinetic energy: 16 J', 'Weight: 19.62 N', 'Goodbye!'):
            self.assertIn(expected, output)

    def test_recovery(self):
        output = self.run_cli('bad\n1\n-1\n2\n1\n2\n3\nq\n')
        self.assertIn('Choose 1, 2, 3, or q.', output)
        self.assertIn('Mass cannot be negative', output)
        self.assertIn('Force: 6 N', output)

    def test_eof(self):
        self.assertIn('Goodbye!', self.run_cli('1\n'))


if __name__ == '__main__':
    unittest.main()
