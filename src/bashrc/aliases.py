#!/usr/bin/python3

import argparse
from pathlib import Path
from typing import List, Union

BASHRC_DEFAULT_PATH = Path.home().joinpath(".bashrc")


def add_alias_to_bashrc(
    cmd: Union[str, List], alias_name: Union[str, List], path_bashrc: Path = BASHRC_DEFAULT_PATH
) -> None:

    if not path_bashrc.is_file():
        raise RuntimeError(f"path_bashrc must lead to a valid file")

    if isinstance(cmd, str):
        cmd = [cmd]

    if isinstance(alias_name, str):
        alias_name = [alias_name]

    with open(path_bashrc, "a") as bashrc:
        for alias, command in zip(alias_name, cmd):
            bashrc.write(f"alias {alias}='{command}'\n")


def get_aliases(path_bashrc: Path = BASHRC_DEFAULT_PATH, flag_print: bool = True) -> List[str]:
    with open(path_bashrc, "r") as bashrc:
        lines = bashrc.readlines()

    aliases = []

    for line in lines:
        if line.startswith("alias "):
            aliases.append(line)
            if flag_print:
                print(line.replace("\n", ""))

    if flag_print:
        print(f"\nFound {len(aliases)} aliases in total.")
    return aliases


def sanity_check(path_bashrc: Path = BASHRC_DEFAULT_PATH):
    aliases = get_aliases(path_bashrc=path_bashrc, flag_print=False)

    alias_names = []

    for alias in aliases:
        if not alias in alias_names:
            alias_names.append(alias)
        else:
            print("The following alias is defined twice!")
            print(alias)


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Flag to indicate to set all aliases.")
    parser.add_argument("--show", action="store_true", help="Shows all defined aliases.")
    parser.add_argument("--sanity-check", "--sc", action="store_true", help="Checks that no alias is defined twice.")
    parser.add_argument("-python-version", "-pv", default="3.7", help="Flag to indicate to set all aliases.")

    args = parser.parse_args()

    pyversion = f"python{args.python_version}"

    if args.all:
        cmd = [
            f"{pyversion} -m venv venv && source venv/bin/activate && pip install -U pip",
            f"source venv/bin/activate",
        ]

        alias_names = [
            "cvenv",
            "avenv",
        ]

        add_alias_to_bashrc(cmd=cmd, alias_name=alias_names)
        return

    if args.show:
        get_aliases()

    if args.sanity_check:
        sanity_check()


if __name__ == "__main__":
    main()
