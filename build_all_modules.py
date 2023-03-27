"""
Creates a all_modules.json file containing a list of all modules across all micropython boards and ports
this is build by running this script from the root of the micropython-stubs repository and it parses the  modules.json files of all the published packages in the repository
"""

import json
import os
import sys
from pathlib import Path

try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore


def mod_record(pkg_path:Path, mod_name: str, mod_type: str = "") -> tuple:
    
    
    return (pkg_name, pkg_version, mod_name, mod_type)

def main(output_file="all_modules.json", input_dir="publish"):
    all_modules = []
    for pkg_path in Path(input_dir).rglob("pyproject.toml"):
        pkg_name = pkg_path.parts[-2]
        # pkg_version = pkg_name.split('-')[1] if '-' in pkg_name else "0.0.0"
        try:
            with open(pkg_path, 'rb') as f:
                # read modules from pyproject.toml
                pyproject = tomllib.load(f)
                pkg_version = pyproject["tool"]["poetry"]["version"]

                familiy = port = board = ""
                modules = pyproject["tool"]["poetry"]["packages"]
                try:
                    familiy = pyproject["tool"]["poetry"]["name"].split("-")[0]
                    port = pyproject["tool"]["poetry"]["name"].split("-")[1]
                    board = pyproject["tool"]["poetry"]["name"].split("-")[2] 
                except (KeyError, IndexError):
                    pass

                for mod in modules:
                    # get module name
                    mod_name  = mod["include"].split(".")[0]
                    row = {
                            "mod_name": mod_name,
                            "family": familiy,
                            "port": port,
                            "board": board,
                            "package":  pyproject["tool"]["poetry"]["name"], 
                            "version": pkg_version,
                    }
                    all_modules.append(row)
        except KeyError as e:
            continue
    with open("all_modules.json", "w") as f:
        json.dump(all_modules, f, indent=4)

if __name__ == "__main__":
    main()