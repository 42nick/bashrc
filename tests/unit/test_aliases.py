import os
from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from bashrc.aliases import add_alias_to_bashrc


def test_add_alias_to_bashrc(tmpdir):
    tmpdir = Path(tmpdir)
    cmd = "echo moin"
    alias = "say_moin"

    with pytest.raises(RuntimeError):
        add_alias_to_bashrc(cmd=cmd, alias_name=alias, path_bashrc=Path())

    test_file = tmpdir.joinpath("tmpfile.txt")

    with open(test_file, "w") as _:
        pass

    add_alias_to_bashrc(cmd=cmd, alias_name=alias, path_bashrc=test_file)


def test_get_aliases():
    pass


def test_sanity_check():
    pass


def test_main():
    pass
