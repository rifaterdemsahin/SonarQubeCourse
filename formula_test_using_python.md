pip install coverage pytest && \
coverage run -m pytest Symbols/tests/scanfiles_test.py && \
coverage xml

---

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ pip install coverage pytest && \
> coverage run -m pytest Symbols/tests/scanfiles_test.py && \
> coverage xml
Collecting coverage
  Downloading coverage-7.8.2-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.9 kB)
Collecting pytest
  Downloading pytest-8.3.5-py3-none-any.whl.metadata (7.6 kB)
Collecting iniconfig (from pytest)
  Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: packaging in /home/codespace/.local/lib/python3.12/site-packages (from pytest) (24.2)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Downloading coverage-7.8.2-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (245 kB)
Downloading pytest-8.3.5-py3-none-any.whl (343 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Installing collected packages: pluggy, iniconfig, coverage, pytest
Successfully installed coverage-7.8.2 iniconfig-2.1.0 pluggy-1.6.0 pytest-8.3.5

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python3 -m pip install --upgrade pip
=================== test session starts ====================
platform linux -- Python 3.12.1, pytest-8.3.5, pluggy-1.6.0
rootdir: /workspaces/SonarQubeCourse
plugins: anyio-4.9.0
collected 8 items                                          

Symbols/tests/scanfiles_test.py ........             [100%]

==================== 8 passed in 0.10s =====================
Wrote XML report to coverage.xml
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 