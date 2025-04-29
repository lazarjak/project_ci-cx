from app import main
import sys
from io import StringIO
import pytest

def test_main():
	captured_output = StringIO()
	sys.stdout = captured_output  # Preusmeravaš stdout kako bi uhvatio ispis

	main()  # Pozivaš funkciju main() koju želiš da testiraš

	sys.stdout = sys.__stdout__  # Vraćaš stdout u originalno stanje

   	# Proveravaš da li je ispisano ono što očekuješ
	assert captured_output.getvalue().strip() == "Hello world"
