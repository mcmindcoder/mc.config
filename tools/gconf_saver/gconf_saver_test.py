#!/usr/bin/python3

import unittest
import gconf_saver as gs


class TestGconfSaver(unittest.TestCase):
    def test_save_key(self):
        # gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-up
        res = gs.get_gconf_key('org.gnome.desktop.interface', 'automatic-mnemonics')
        self.assertEqual(res, "true")
        res = gs.get_gconf_key('org.gnome.desktop.interface', 'can-change-accels')
        self.assertEqual(res, "false")
        res = gs.get_gconf_key('org.gnome.desktop.interface', 'cursor-size')
        self.assertEqual(res, "24")
        res = gs.get_gconf_key('not', 'exists')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
