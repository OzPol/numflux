# NumFlux

**A Numerical Dynamics Engine for Simulating Pattern-Constrained Number Systems**

NumFlux is a modular simulation and feature modeling framework designed to explore structured behaviors in constrained numeric domains. 
It supports feature-rich analysis, influence-based modeling, external signal integration, and dynamic sampling under synthetic or empirical configurations.

Whether used as a sandbox for evolving numeric patterns or a structured generator conditioned on prior data, NumFlux provides a flexible backbone for numeric simulation, statistical learning, and domain-agnostic research.

Designed to explore both intrinsic numeric properties and environmental interactions, NumFlux is suitable for:

- Generative numeric modeling
- Influence-aware number space exploration
- Cross-domain structural simulations
- Feature engineering toolkits for ML systems

---

### 🔍 Capabilities

- Generate synthetic numeric datasets with controllable structure
- Learn and adapt generation behavior based on input data
- Extract deep structural features from number spaces (digit class, parity, prime status, sequence theory, etc.)
- Model influence fields over time, location, and external variables
- Perform weighted, feature-informed sampling based on evolving logic

---

### 🔧 Key Modules

- **NumField**: Models intrinsic number characteristics (parity, primality, entropy, 3N+1)
    NumField includes, and can be extended to support, features such as:
    - **Parity**: Even vs. Odd

    - **Digit Class**: Total digit count (e.g., Single-digit vs. double-digit) 

    - **Digit Sum**: Sum of digits (e.g., 42 → 4 + 2 = 6)

    - **Primality**: Is the number a prime?

    - **Perfect Square**: Is the number a square (e.g., 1, 4, 9, 16)?

    - **3N+1 Membership**: Does the number appear in a Collatz (3n+1) sequence?

    - **Factor Count**: Number of positive divisors

    - **Is Power of 2 / 3 / 10**: Detect exponential structure

    - **Modulo Class**: Number modulo small bases (e.g., mod 3, mod 5)

    - **Relative Magnitude Class**: Quartile or percentile class within the candidate pool

    - **Sequence Membership**: Belongs to known sequences (e.g., Fibonacci, Triangular, etc.)

    - **Digit Pattern**:
        - Repeating digits (e.g., 11, 22)
        - Palindromic (e.g., 121)
        - Ascending digits (e.g., 12, 345)
        - Descending digits (e.g., 43, 321)

    - **Entropy Proxy**: Shannon-style approximation based on digit uniqueness or spread

    - **Position-Weighted Encoding**: Apply positional context weight (e.g., if number is first in a row)

- **LumaField**: Represents external energy/light influence fields (e.g., lunar cycle, solar index, sun, moon, EM flux)
- **DrawContext**: Centralized interface carrying candidate pool, prior history, timestamp, and location
- **SimulationEngine**: Composes fields, merges influence models, and generates weighted samples
- **RandomGenerator**: Creates initial numeric datasets; can optionally adapt to past data patterns
- **Sphinx Docs**: Full documentation, usage examples, and API explorer   


---

### 🛠️ Getting Started

```bash
    pip install -r requirements.txt
    python -m numflux.core.engine
```


### 📈 Dataset Simulation with `RandomGenerator`

NumFlux includes a flexible numeric data generator for creating synthetic datasets with structured constraints. This generator can be used to:

- Simulate numeric patterns over custom ranges and dimensions
- Create placeholder datasets for feature analysis and testing
- Emulate numeric behavior in structured domains
- Optionally adapt to real-world datasets and evolve over time

---

#### ⚙️ Configuration Structure

The dataset can be defined using a list of column configurations:

Each column is a dictionary with the following keys:

| Key     | Type    | Description                             |
|---------|---------|-----------------------------------------|
| `name`  | str     | Name of the column                      |
| `min`   | int     | Minimum value for random generation     |
| `max`   | int     | Maximum value for random generation     |

A hard limit of 100 columns is enforced by default to avoid runaway or infinite configurations.
This limit can be manually adjusted using the `max_columns` parameter in the `RandomGenerator`

---

#### Example: Dataset

```python
from numflux.generator.random_generator import RandomGenerator

columns = [{"name": f"N{i+1}", "min": 1, "max": 69} for i in range(5)] + [{"name": "B", "min": 1, "max": 26}]
gen = RandomGenerator(n_rows=1000, columns=columns)
gen.to_csv("data/random_generated.csv")
```

Resulting CSV:

```csv
    N1,N2,N3,N4,N5,B
    12,45,5,33,68,17
    4,21,8,60,13,3
```

Example: Custom Structure

```python
    columns = [
        {"name": "SensorA", "min": 100, "max": 999},
        {"name": "Channel1", "min": 0, "max": 10},
        {"name": "Temp", "min": -20, "max": 50}
    ]

    gen = RandomGenerator(n_rows=500, columns=columns)
    gen.to_csv("data/custom_simulated.csv")
```

Example:
```python
    gen = RandomGenerator(
        n_rows=1000,
        columns=[
            {"name": "A", "min": 1, "max": 10},
            {"name": "B", "min": 100, "max": 999},
            {"name": "C", "min": 0, "max": 1},
            {"name": "Z", "min": 1, "max": 26},
            {"name": "Alpha", "min": 0, "max": 9},
            {"name": "Beta", "min": 100, "max": 1000},
            {"name": "Gamma", "min": -5, "max": 5}
        ]
    )
    gen.to_csv("data/advanced_custom.csv")
```

---

And internally, the generator enforces column limits to prevent excessive memory usage or accidental runaway configurations:

```python
    if len(columns) > self.max_columns:
        raise ValueError(f"Too many columns: {len(columns)} exceeds max_columns={self.max_columns}")
```


    NumFlux/
    ├── .github/
    │   └── workflows/
    │       └── docs.yml            # Auto-deploy Sphinx docs to GitHub Pages
    │
    ├── core/
    │   ├── engine.py               # Simulation engine (field orchestration, sampling, etc.)
    │   ├── pipeline.py             # Data flow, multi-stage simulation pipeline (future expansion)
    │   └── __init__.py
    │
    ├── context/
    │   ├── context.py              # Defines DrawContext object (timestamp, location, etc.)
    │   └── __init__.py
    │
    ├── data/
    │   └── sample_draws.csv        # Example datasets (Powerball or others)
    │
    ├── docs/                       # Sphinx documentation source
    │   ├── conf.py
    │   ├── index.rst
    │   ├── maintenance.md
    │   ├── modules/
    │   │   ├── engine.rst
    │   │   ├── numfield.rst
    │   │   └── context.rst
    │   └── _build/
    │
    ├── field/
    │   ├── README.md
    │   ├── basefield.py            # Abstract Field class (requires timestamp + location)
    │   ├── chrono.py               # (future) Temporal rhythm models (e.g., time-of-day, moon cycles)
    │   ├── geofield.py             # (future) Earth-related signals (EM flux, magnetic index)
    │   ├── lumafield.py            # External light/energy influence modeling (stub)
    │   ├── numfield.py             # Intrinsic digit/number-based feature modeling
    │   └── __init__.py
    │
    ├── generator/
    │   ├── output/
    │   ├── random_generator.py     # Flexible, column-based random data generator
    │   └── __init__.py
    │
    ├── models/                     # Trained models / saved artifacts (pickle, ONNX, etc.)
    │
    ├── notebooks/
    │   ├── 00_random_generator_dev.ipynb
    │   ├── 01_feature_extraction.ipynb
    │   ├── 02_field_testing.ipynb
    │   └── 03_simulation_runner.ipynb
    │
    ├── tests/
    │   ├── test_numfield.py
    │   ├── test_engine.py
    │   └── test_context.py
    │
    ├── CONTRIBUTING.md
    ├── README.md
    ├── requirements.txt
    ├── setup.py                    # setup for exposing this as a Python package
    └── LICENSE

---
