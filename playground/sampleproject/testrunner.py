# test_runner.py im Hauptverzeichnis
import sys
import os
import unittest

# Pfad zum Hauptverzeichnis hinzufügen
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
# Oder zum src-Verzeichnis, falls dort die Module liegen
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src'))

# Tests laden und ausführen
test_loader = unittest.TestLoader()
test_suite = test_loader.discover('tests', pattern='test*.py')
# Oder direkt die Datei laden: unittest.TestLoader().loadTestsFromName('test_InputReader')

unittest.TextTestRunner().run(test_suite)