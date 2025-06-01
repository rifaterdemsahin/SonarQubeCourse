The reason **SonarQube did not pick up the test file or improve the coverage** likely comes down to one or more of the following **common configuration or structural issues**:

---

### ✅ **1. The test file was not included in the test coverage run**

If SonarQube is relying on coverage reports (like from `coverage.py` or `pytest-cov`), then simply writing the test file isn't enough. You must:

* Run tests with coverage tracking enabled:

  ```bash
  coverage run -m unittest discover
  coverage xml  # or json, depending on how SonarQube is configured
  ```

* Ensure that your test file is discoverable by the test runner (`unittest`, `pytest`, etc.)

---

### ✅ **2. The test file is not located where SonarQube expects it**

SonarQube usually expects tests to live under a directory like `tests/`, `test/`, or be configured explicitly.

Check your `sonar-project.properties` or equivalent config and make sure you have:

```properties
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
```

If your test file is not under the expected `sonar.tests` path, it won't be counted.

---

### ✅ **3. The code under test runs on import**

From your comments:

> “Note: This is problematic because the original code runs immediately!”

If the code you’re testing runs as soon as it is imported (e.g., no `if __name__ == "__main__":` guard), it **can’t be easily isolated and covered** by tests, and may also crash or exit during coverage collection.

🛠️ **Solution:** Refactor the original code so that logic is wrapped in functions or a main guard:

```python
def main():
    # logic here

if __name__ == '__main__':
    main()
```

---

### ✅ **4. The code you’re testing is not imported or instrumented**

You're simulating the behavior manually in your test:

```python
# Simulate the function behavior
```

This **does not count as coverage** of the original file, because you're not calling the actual code under test. You're recreating logic, so the coverage tool **sees 0% lines covered** in the actual file.

🛠️ **Fix:**

* Import the actual functions/modules under test
* Mock what you need, but **call the real code**

---

### ✅ **5. The codebase uses globals or side-effects poorly**

As you highlighted:

> "globals make testing difficult"
> "original code lacks error handling"

If the original code is a script that runs on import, has global state, and prints directly to stdout, it’s difficult to test and **impossible to measure code coverage meaningfully**.

---

## ✅ How to verify SonarQube coverage integration works

1. **Generate Coverage Report**

   ```bash
   coverage run -m unittest discover
   coverage xml
   ```

2. **Check coverage output**

   ```bash
   coverage report
   ```

3. **Point SonarQube to report**

   ```properties
   sonar.python.coverage.reportPaths=coverage.xml
   ```

4. **Ensure actual code is invoked in the tests**

---

### 🔍 Quick checklist to debug this:

| Check                                                              | Status |
| ------------------------------------------------------------------ | ------ |
| Test file is in `sonar.tests` path                                 | ✅/❌    |
| Coverage report is generated and correct                           | ✅/❌    |
| Report is referenced in `sonar-project.properties`                 | ✅/❌    |
| The original file has logic guarded by `if __name__ == "__main__"` | ✅/❌    |
| Tests call the actual code (not simulate it)                       | ✅/❌    |
| No syntax errors or runtime crashes on import                      | ✅/❌    |

---

### ✅ Recommendation

If you're still stuck, you could share:

* Your SonarQube config file (`sonar-project.properties`)
* How you're running your test and coverage
* The structure of the original file under test (e.g., does it have a `main()` function?)

I'd be happy to diagnose further from there.
