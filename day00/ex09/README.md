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

## Usage
```python
from ft_package.core import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
```

