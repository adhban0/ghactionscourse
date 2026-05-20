import unittest

from ci_message import build_status_message


class BuildStatusMessageTests(unittest.TestCase):
    def test_build_status_message(self) -> None:
        message = build_status_message("gh-actions-course", "main", 5, 5)
        self.assertEqual(message, "gh-actions-course on main: 5/5 checks passed")

    def test_rejects_invalid_counts(self) -> None:
        with self.assertRaises(ValueError):
            build_status_message("gh-actions-course", "main", 6, 5)

    def test_rejects_empty_project(self) -> None:
        with self.assertRaises(ValueError):
            build_status_message("", "main", 1, 1)


if __name__ == "__main__":
    unittest.main()
