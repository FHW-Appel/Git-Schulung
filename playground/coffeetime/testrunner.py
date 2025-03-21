# test_runner.py im Hauptverzeichnis
import sys
import os
import unittest

# Pfad zum Hauptverzeichnis hinzufügen
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src'))

# Bestimme den absoluten Pfad zu 'tests/'
tests_dir = os.path.join(os.path.dirname(__file__), "test")

# Test-Suite mit absolutem Pfad laden
test_loader = unittest.TestLoader()
test_suite = test_loader.discover(start_dir=tests_dir, pattern="test*.py")

# Test-Runner mit verboseren Logs ausführen
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(test_suite)

# Exit mit Code 0 bei Erfolg, 1 bei Fehlern
sys.exit(not result.wasSuccessful())