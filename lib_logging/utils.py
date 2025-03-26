from pathlib import Path

import toml


def get_app_version(pyproject_file: Path | str = 'pyproject.toml') -> str:
    with open(pyproject_file) as f:
        pyproject_data = toml.load(f)
    return pyproject_data['project']['version']
