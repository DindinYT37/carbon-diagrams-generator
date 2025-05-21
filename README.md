# Carbon Diagrams Generator

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python-based tool for generating visual representations of carbon isotopes and their properties.

## Features

- Generates transparent atomic diagrams for Carbon-12, Carbon-13, and Carbon-14
- Creates a beautiful HTML table with isotope information
- Exports the table as a PNG image with white background

## Requirements

- Python 3.11+
- Chrome/Chromium browser
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dindinyt37/carbon-diagrams-generator.git
cd carbon-diagrams-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Generate atomic diagrams:
```bash
python carbon-diagrams/diagram-generator.py
```

2. Generate the final table image:
```bash
python carbon-table/html2png.py
```

## Project Structure

```
carbon-diagrams-generator/
├── carbon-diagrams/    # Atomic diagram generation scripts
├── carbon-table/       # HTML table and image export utilities
├── requirements.txt    # Project dependencies
├── LICENSE             # MIT license
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.