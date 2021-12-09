# DNS Mock

[![CodeQL](https://github.com/imjoseangel/dnsmock/workflows/CodeQL/badge.svg)](https://github.com/imjoseangel/dnsmock/security/code-scanning) [![codecov](https://codecov.io/gh/imjoseangel/dnsmock/branch/devel/graph/badge.svg)](https://codecov.io/gh/imjoseangel/dnsmock) [![Python package](https://github.com/imjoseangel/dnsmock/workflows/Python%20package/badge.svg)](https://pypi.org/project/dnsmock)

Python DNS Mock to bypass current DNS resolution. Emulates /etc/hosts inside a container.

## Requirements

The dnsmock segment requires the standard library module [socket][3]. It provides access to the BSD socket interface.

## Installation

### Using pip

```bash
pip install dnsmock
```

## Usage example

```python
import dnsmock
import requests

dnsmock.bind_ip('www.example.com', 443, '127.0.0.1')
response = requests.get('https://www.example.com', verify=True)

print(response.text)
```

## Authors

Originally created by [@imjoseangel](http://github.com/imjoseangel)

## License

Licensed under [the MIT License][2].

[1]: https://imjoseangel.eu
[2]: https://github.com/imjoseangel/dnsmock/blob/devel/LICENSE
[3]: https://docs.python.org/3/library/socket.html
