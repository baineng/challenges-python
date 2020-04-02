import unittest
import enum


class EnumTest(unittest.TestCase):

    class BugStatus(enum.Enum):
        new = 7
        incomplete = 6
        invalid = 5
        wont_fix = 4
        in_progress = 3
        fix_committed = 2
        fix_released = 1

    def test_use(self):
        self.assertEqual(self.BugStatus.wont_fix.name, 'wont_fix')
        self.assertEqual(self.BugStatus.wont_fix.value, 4)

    def test_iteration(self):
        for status in self.BugStatus:
            self.assertEqual(status.name, 'new')
            self.assertEqual(status.value, 7)
            break

    def test_comparing(self):
        actual_state = self.BugStatus.wont_fix
        desired_state = self.BugStatus.fix_released

        self.assertFalse(actual_state == desired_state)
        self.assertTrue(actual_state == self.BugStatus.wont_fix)
        self.assertFalse(actual_state is desired_state)
        self.assertTrue(actual_state is self.BugStatus.wont_fix)


if __name__ == '__main__':
    unittest.main()