import importlib
from unittest.mock import Mock, patch

import pytest

import depenv


def test_default():
    from examples.birds import Bird

    assert Bird().speak() == "chirp"


def test_direct_instantiation():
    from examples.birds import Duck

    assert Duck().speak() == "quack"


def test_injectable_case_insensitive(monkeypatch):
    from examples.birds import Bird, Duck

    class BIRD(depenv.Injectable):
        def speak(self):
            return "chirp"

    monkeypatch.setenv("DEPENV_BIRD", "Duck")

    assert Bird().speak() == "quack"
    assert BIRD().speak() == "quack"


def test_injectable_case_sensitive(monkeypatch):
    from examples.birds import Bird, Duck

    class BIRD(depenv.Injectable):
        def speak(self):
            return "chirp"

    monkeypatch.setenv("DEPENV_Bird", "Duck")

    assert Bird().speak() == "quack"
    assert BIRD().speak() == "chirp"


def test_injectable_isnt_inherited(monkeypatch):
    from examples.birds import Duck, Parrot

    assert issubclass(Duck, depenv.Injectable)

    monkeypatch.setenv("DEPENV_DUCK", "Parrot")

    assert Duck().speak() == "quack"


def test_injected_invalid_module(monkeypatch):
    from examples.birds import Bird

    monkeypatch.setenv("DEPENV_BIRD", "examples.bad_birds.Duck")

    with pytest.raises(ModuleNotFoundError):
        Bird()


def test_injected_module_prefix(monkeypatch):
    from examples.birds import Bird

    monkeypatch.setenv("DEPENV_BIRD", "examples.birds.Duck")

    assert Bird().speak() == "quack"


def test_injected_moduled_prefix_memoized(monkeypatch):
    spy = Mock(wraps=importlib.import_module)

    class Bird(depenv.Injectable):
        def speak(self):
            return "chirp"

    monkeypatch.setenv("DEPENV_BIRD", "examples.birds.Duck")
    with patch("sys.modules", {}), patch("importlib.import_module", spy):
        assert Bird().speak() == "quack"
        assert spy.call_count == 1
        assert Bird().speak() == "quack"
        assert spy.call_count == 1


def test_injected_no_class(monkeypatch):
    from examples.birds import Bird

    monkeypatch.setenv("DEPENV_BIRD", "BadBird")

    with pytest.raises(AttributeError):
        Bird()


def test_injected_init_args(monkeypatch):
    from examples.birds import Bird, Parrot

    monkeypatch.setenv("DEPENV_BIRD", "Parrot")

    polly = Parrot("Polly")
    assert polly.speak() == "Polly wanna cracker?"


def test_injected_init_kwargs(monkeypatch):
    from examples.birds import Bird, Parrot

    monkeypatch.setenv("DEPENV_BIRD", "Parrot")

    polly = Parrot(name="Polly")
    assert polly.speak() == "Polly wanna cracker?"


def test_multiple_bases_parent(monkeypatch):
    class Mixin:
        pass

    class Bird(Mixin, depenv.Injectable):
        def speak(self):
            return "chirp"

    class Duck(Bird):
        def speak(self):
            return "quack"

    monkeypatch.setenv("DEPENV_BIRD", "Duck")

    assert Bird().speak() == "quack"


def test_multiple_bases_child(monkeypatch):
    from examples.birds import Bird

    class Mixin:
        pass

    class Duck(Mixin, Bird):
        def speak(self):
            return "quack"

    monkeypatch.setenv("DEPENV_BIRD", "Duck")

    assert Bird().speak() == "quack"


def test_local_name_collision(monkeypatch):
    from examples.birds import Bird

    class Duck(Bird):
        def speak(self):
            return "quack quack"

    monkeypatch.setenv("DEPENV_BIRD", "examples.birds.Duck")

    assert Bird().speak() == "quack"

    monkeypatch.setenv("DEPENV_BIRD", "Duck")

    assert Bird().speak() == "quack quack"
