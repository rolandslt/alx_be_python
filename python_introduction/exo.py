import unittest

# --- Function to test ---
def cuboid_volume(l):
    """Return the volume of a cube given its side length l."""
    return (l * l * l)

# --- Manual checks (optional) ---
lengths = [2, 1.1, -2.5, 2j, 'two']

for i in range(len(lengths)):
    try:
        print("The volume of cuboid:", cuboid_volume(lengths[i]))
    except Exception as e:
        print(f"Error for {lengths[i]}: {e}")

# --- Automated unit tests ---
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),1)
    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, True)
unittest.main(argv=[''],verbosity=2, exit=False)