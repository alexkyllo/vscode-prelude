import subprocess
from typing import List
from loguru import logger as LOG

def list_extensions() -> List[str]:
    """List the currently installed extensions."""
    result = subprocess.run(["code", "--list-extensions"], text=True, capture_output=True)
    lines = result.stdout.splitlines()
    if len(lines) > 0 and lines[0].startswith("Extensions installed"):
        lines = lines[1:]
    LOG.info("Extensions currently installed: {num}", num=len(lines))
    return lines

def install_extensions(extensions: List[str], dry_run:bool=False) -> None:
    """Install a list of extension names."""
    existing_extensions = list_extensions()
    for ext in extensions:
        if ext in existing_extensions:
            LOG.info("Extension already installed: {ext}", ext=ext)
        else:
            LOG.info("Installing extension: {ext}", ext=ext)
            if not dry_run:
                subprocess.run(["code", "--install-extension", ext])
