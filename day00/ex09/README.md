# ft_package

My first (and wonderful) package!

## Installation
### Using Pip
```bash
pip install ft_package
```

### Building the library
Ensure you have setuptools and wheel installed:
```bash
pip install setuptools wheel
```
Build the source distribution and the wheel:
```bash
python3 setup.py sdist bdist_wheel
```

Install from the `dist` folder:
```bash
pip install dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage
```python
from ft_package.core import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
```

