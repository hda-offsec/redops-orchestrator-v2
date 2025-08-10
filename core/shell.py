import resource
import subprocess
from pathlib import Path
from typing import Sequence


def run(cmd: Sequence[str], cwd: Path, timeout: int = 60) -> subprocess.CompletedProcess:
    def set_limits():
        resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout))
        resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    return subprocess.run(
        list(cmd),
        cwd=cwd,
        timeout=timeout,
        capture_output=True,
        text=True,
        preexec_fn=set_limits,
    )
