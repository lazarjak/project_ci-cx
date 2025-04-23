import pytest
from io import StringIO
import sys
<<<<<<< HEAD
<<<<<<< HEAD
from projekat.main import main   #Importujemo funkciju main() iz main.py
=======
from core.main import main   #Importujemo funkciju main() iz main.py
>>>>>>> c06e92b (Test for main.py)
=======
from main import main   #Importujemo funkciju main() iz main.py
>>>>>>> e55bcb1 (Initial commit)

def test_main():

	captured_output = StringIO()
	sys.stdout = captured_output

	main()

	sys.stdout = sys.__stdout__

	assert captured_output.getvalue().strip() == "Hello from dummy service!"

