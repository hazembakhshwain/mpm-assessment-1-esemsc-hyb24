# acsefunctions

This repository contains a custom Python package called `acsefunctions`, which implements various mathematical functions such as exponential, hyperbolic functions, factorial, gamma, and Bessel functions. The package also provides a comprehensive comparison against NumPy and SciPy implementations, with a focus on both performance and accuracy.

## Features

- Implements commonly used transcendental and special functions.
- Includes `exp`, `sinh`, `cosh`, `tanh`, `fact`, `gamma`, and `bessel` functions.
- Provides a comparison of execution times and errors versus NumPy/SciPy functions.
- Jupyter notebook with illustrative examples and detailed comparison plots.
- GitHub Actions workflow to validate the notebook automatically.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Follow the steps below to clone the repository, set up the environment, and install the package.

### Step 1: Clone the Repository

To get started, clone the repository using the following command:

```bash
git clone https://github.com/ese-ada-lovelace-2024/mpm-assessment-1-esemsc-hyb24.git
cd mpm-assessment-1-esemsc-hyb24
```

### Step 2: Set Up the Environment

This project uses Conda for managing the environment. If you don't have Conda installed, follow the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to install it.

Once Conda is installed, create the environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate acsefunctions-env
```

Alternatively, if you prefer using `pip`, you can install the dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Install the Package

After setting up the environment, install the `acsefunctions` package in editable mode:

```bash
pip install -e .
```

---

## Usage

### Importing the Package

Once the package is installed, you can import and use the implemented functions like so:

```python
from acsefunctions import exp, sinh, cosh, tanh, fact, gamma, bessel

# Example usage
print(exp(1))      # Exponential function
print(sinh(2))     # Hyperbolic sine function
print(gamma(5))    # Gamma function
```

### Running the Jupyter Notebook

To explore the package’s functions and see detailed comparisons with NumPy/SciPy, you can run the provided Jupyter notebook. Make sure you have activated the environment and have Jupyter installed:

```bash
jupyter notebook
```

Open the `documentation.ipynbb` notebook to see usage examples, comparisons, and plots.

---

## Testing

### Running Unit Tests

You can run the test suite to ensure everything works as expected. The tests are located in the `tests/` directory. Use `pytest` to run the tests:

```bash
pytest tests/
```

This will test all the functions, including comparisons to NumPy/SciPy counterparts, as well as verify the accuracy of the implementations.

### Testing the Jupyter Notebook

We have set up a GitHub Actions workflow that automatically tests the Jupyter notebook upon each commit or pull request. You can also manually test the notebook using `nbconvert`:

```bash
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 documentation.ipynbb
```

---

## Documentation

Detailed documentation for each function is available via Sphinx. You can build the documentation locally by running the following command:

```bash
make html
```

Once built, open `docs/_build/html/index.html` in your browser to view the documentation.

### Assessment PDF

For more context on this project, you can find the original assessment in the repository. [Click here to view the assessment PDF](./assessment.pdf).

---

## Contributing

Contributions are welcome! If you’d like to contribute, please follow the guidelines below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
