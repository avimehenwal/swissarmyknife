"""
1. Codecoverage
2. Run tests
3. Build and publish on pypi
4. Run pylint
5. Build docs / website
6. clean directories
7. Spell checker

init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
"""

def task_hello():
    """hello"""

    def python_hello(targets):
        with open(targets[0], "a") as output:
            output.write("Python says Hello World!!!\n")

    return {
        'actions': [python_hello],
        'targets': ["hello.txt"],
        }

