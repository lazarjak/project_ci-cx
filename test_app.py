from frontend.app import main
import builtins
import io

def test_main_output(monkeypatch):
    # Pravimo lažni "stdout"
    fake_out = io.StringIO()
    monkeypatch.setattr(builtins, 'print', lambda msg: fake_out.write(msg))

    # Pokrećemo main funkciju
    main()

    # Dobijeni izlaz upoređujemo sa očekivanim
    assert fake_out.getvalue() == "Hello world"
