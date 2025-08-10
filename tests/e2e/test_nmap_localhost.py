import shutil
import subprocess

import pytest


@pytest.mark.skipif(shutil.which('nmap') is None, reason='nmap not installed')
def test_nmap_localhost():
    subprocess.run(['nmap', '127.0.0.1'], check=False)
