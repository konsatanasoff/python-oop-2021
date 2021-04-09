from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("iMac", "Desktop", 100, 100)

    def test_attr_are_set(self):
        self.assertEqual("iMac", self.hardware.name)
        self.assertEqual("Desktop", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(100, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_has_no_memory_when_software_installed_raises(self):
        software = LightSoftware("Linux", 500, 500)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_equal_capacity_and_memory_software_installed(self):
        software = LightSoftware("Linux", 50, 200)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_if_software_is_installed(self):
        software = LightSoftware("Linux", 50, 200)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_un_existing_software(self):
        software = LightSoftware("Linux", 50, 200)
        self.assertEqual(0, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))

        # Test with installed software
        software = LightSoftware("Linux", 50, 200)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)

        win_software = LightSoftware("Windows", 50, 200)
        self.assertNotIn(win_software, self.hardware.software_components)

    def test_uninstall_software(self):
        software = LightSoftware("Linux", 50, 200)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))

        self.hardware.uninstall(software)
        self.assertNotIn(software, self.hardware.software_components)
        self.assertEqual(0, len(self.hardware.software_components))


if __name__ == '__main__':
    main()