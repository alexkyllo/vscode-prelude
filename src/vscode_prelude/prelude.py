import subprocess

EXTENSIONS = [
    "arcticicestudio.nord-visual-studio-code",
    "ms-vscode-remote.remote-containers",
    "ms-vscode-remote.remote-ssh",
    "ms-vscode-remote.remote-ssh-edit",
    "ms-vscode-remote.remote-wsl",
    "ms-vscode-remote.vscode-remote-extensionpack",
    "tuttieee.emacs-mcx",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "james-yu.latex-workshop",
]

def list_extensions():
    result = subprocess.run(["code", "--list-extensions"], text=True, capture_output=True)
    lines = result.stdout.splitlines()
    if len(lines) > 0 and lines[0].startswith("Extensions installed"):
        lines = lines[1:]
    return lines

def install_extensions(extensions):
    existing_extensions = list_extensions()
    for ext in extensions:
        if ext not in existing_extensions:
            subprocess.run(["code", "--install-extension", ext])
