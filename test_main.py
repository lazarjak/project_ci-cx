import pytest
from io import StringIO
import sys
from main import main   #Importujemo funkciju main() iz main.py

def test_main():

	captured_output = StringIO()
	sys.stdout = captured_output

	main()

	sys.stdout = sys.__stdout__

	assert captured_output.getvalue().strip() == "Hello from dummy service!"

