import unittest


def run():
    loader = unittest.TestLoader()

    # Discover all test cases in the current directory
    suite = loader.discover(start_dir=".", pattern="*.py")

    # Create a test runner
    runner = unittest.TextTestRunner(verbosity=2)

    # Run the test suite
    runner.run(suite)

