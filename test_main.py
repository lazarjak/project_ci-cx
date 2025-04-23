import pytest
from io import StringIO
import sys
<<<<<<< HEAD
from projekat.main import main   #Importujemo funkciju main() iz main.py
=======
from core.main import main   #Importujemo funkciju main() iz main.py
>>>>>>> c06e92b (Test for main.py)

def test_main():

	captured_output = StringIO()
	sys.stdout = captured_output

	main()

	sys.stdout = sys.__stdout__

	assert captured_output.getvalue().strip() == "Hello from dummy service!"

