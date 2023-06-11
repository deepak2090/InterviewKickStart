from logging import root
import os
import pytest

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    conftest_path = os.path.join(root_dir)
    pytest.main(["-v", "-s", "--confcutdir", root_dir, conftest_path])
