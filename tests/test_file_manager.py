# test_file_manager.py
# Unit tests for file_manager.py

import tempfile
import unittest
from pathlib import Path

from game.file_manager import FileManager


class TestFileManager(unittest.TestCase):
    # Tests the FileManager class

    def setUp(self) -> None:
        # Creates a temporary directory before each test

        self.temp_directory = (
            tempfile.TemporaryDirectory()
        )
        self.test_directory = Path(
            self.temp_directory.name
        )
        self.test_file = (
            self.test_directory
            / "test.json"
        )

    def tearDown(self) -> None:
        # Removes the temporary directory

        self.temp_directory.cleanup()

    def test_ensure_directory_exists(self) -> None:
        # Tests directory creation

        new_directory = (
            self.test_directory
            / "new_directory"
        )
        self.assertFalse(
            new_directory.exists()
        )
        FileManager.ensure_directory_exists(
            new_directory,
        )
        self.assertTrue(
            new_directory.exists()
        )
        self.assertTrue(
            new_directory.is_dir()
        )

    def test_create_file_if_missing(self) -> None:
        # Tests creating a new JSON file

        default_data = {
            "name": "Player",
        }
        FileManager.create_file_if_missing(
            self.test_file,
            default_data,
        )
        self.assertTrue(
            self.test_file.exists()
        )
        loaded_data = (
            FileManager.load_json(
                self.test_file,
            )
        )
        self.assertEqual(
            loaded_data,
            default_data,
        )

    def test_create_file_if_missing_existing_file(self) -> None:
        # Tests that an existing file is not overwritten

        FileManager.save_json(
            self.test_file,
            {
                "score": 10,
            },
        )
        FileManager.create_file_if_missing(
            self.test_file,
            {
                "score": 0,
            },
        )
        self.assertEqual(
            FileManager.load_json(
                self.test_file,
            ),
            {
                "score": 10,
            },
        )

    def test_save_json(self) -> None:
        # Tests saving JSON data

        data = {
            "player": "Alice",
            "wins": 4,
        }
        FileManager.save_json(
            self.test_file,
            data,
        )
        loaded_data = (
            FileManager.load_json(
                self.test_file,
            )
        )
        self.assertEqual(
            loaded_data,
            data,
        )

    def test_load_json(self) -> None:
        # Tests loading JSON data

        expected_data = {
            "difficulty": "Hard",
        }
        FileManager.save_json(
            self.test_file,
            expected_data,
        )
        actual_data = (
            FileManager.load_json(
                self.test_file,
            )
        )
        self.assertEqual(
            actual_data,
            expected_data,
        )

    def test_load_invalid_json(self) -> None:
        # Tests loading an invalid JSON file

        self.test_file.write_text(
            "{ invalid json }",
            encoding="utf-8",
        )
        with self.assertRaises(
            ValueError,
        ):
            FileManager.load_json(
                self.test_file,
            )

    def test_load_missing_file(self) -> None:
        # Tests loading a missing file

        with self.assertRaises(
            FileNotFoundError,
        ):
            FileManager.load_json(
                self.test_file,
            )

    def test_reset_json(self) -> None:
        # Tests resetting a JSON file

        FileManager.save_json(
            self.test_file,
            {
                "score": 50,
            },
        )
        FileManager.reset_json(
            self.test_file,
            {
                "score": 0,
            },
        )
        self.assertEqual(
            FileManager.load_json(
                self.test_file,
            ),
            {
                "score": 0,
            },
        )

    def test_file_exists(self) -> None:
        # Tests file existence detection

        self.assertFalse(
            FileManager.file_exists(
                self.test_file,
            )
        )
        FileManager.save_json(
            self.test_file,
            {},
        )
        self.assertTrue(
            FileManager.file_exists(
                self.test_file,
            )
        )

    def test_delete_file(self) -> None:
        # Tests deleting a file

        FileManager.save_json(
            self.test_file,
            {},
        )
        self.assertTrue(
            self.test_file.exists()
        )
        FileManager.delete_file(
            self.test_file,
        )
        self.assertFalse(
            self.test_file.exists()
        )

    def test_delete_missing_file(self) -> None:
        # Tests deleting a file that does not exist

        FileManager.delete_file(
            self.test_file,
        )
        self.assertFalse(
            self.test_file.exists()
        )


__all__ = [
    "TestFileManager",
]

if __name__ == "__main__":
    unittest.main() 

