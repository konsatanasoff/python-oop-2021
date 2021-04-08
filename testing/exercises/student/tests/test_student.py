from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Test_student")

    def test_check_if_attr_set(self):
        self.assertEqual("Name", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_course_with_notes(self):
        result = self.student.enroll("OOP", ["SOLID", "Django"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_with_notes_without_saving(self):
        result = self.student.enroll("OOP", ["SOLID", "Django"], "N")
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(0, len(self.student.courses["OOP"]))
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_existing_course(self):
        result = self.student.enroll("OOP", ["SOLID", "Django"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        # Test if existing notes are appended to existing course
        result = self.student.enroll("OOP", ["Advanced", "Flask"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(4, len(self.student.courses["OOP"]))
        self.assertEqual("Course already added. Notes have been updated.", result)

        # Test with Y add_notes
        result = self.student.enroll("JAVA", ["Advanced", "Flask"], "Y")
        self.assertEqual(2, len(self.student.courses))
        self.assertEqual(4, len(self.student.courses["OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_to_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("OOP", ["1", "2"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_enroll_and_add_notes_to_existing_course(self):
        result = self.student.enroll("OOP", ["SOLID", "Django"])
        self.assertEqual(1, len(self.student.courses))
        self.assertEqual(2, len(self.student.courses["OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        # Test if notes are appended
        result = self.student.add_notes("OOP", "Testing")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(3, len(self.student.courses["OOP"]))
        self.assertIn("Testing", self.student.courses["OOP"])

    def test_if_un_existing_course_removal_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student.enroll("OOP", ["SOLID", "Django"])
        self.assertEqual(1, len(self.student.courses))

        # Try to leave course
        result = self.student.leave_course("OOP")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(0, len(self.student.courses))




if __name__ == '__main__':
    main()
