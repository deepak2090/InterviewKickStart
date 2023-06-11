import os
import pytest

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    conftest_path = root_dir
    pytest.main(["-v", "--confcutdir", root_dir, conftest_path])
