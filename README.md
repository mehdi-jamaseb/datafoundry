# DataFoundry

**DataFoundry** is a modular open-source framework for managing, transforming, and reorganizing data pipelines for AI and data analysis.  
It provides flexible tools to automatically **load**, **restructure**, and **prepare** datasets in hierarchical folder structures for machine learning workflows.

---

## Key Features
- **Recursive data loading** — easily handle deeply nested folder structures.
- **Dataset reorganization** — convert between directory formats like `train/class/samples` and `class/train/samples`.
- **Configurable pipelines** — define preprocessing steps declaratively.
- **Efficient processing** — stream large datasets with minimal memory usage.
- **CLI interface** — manage datasets directly from the command line.
- **Extensible API** — integrate into ML projects with minimal code.

---

## Installation
You can install DataFoundry directly from source:

```bash
git clone https://github.com/<yourusername>/DataFoundry.git
cd DataFoundry
pip install -e .
````

Or install from PyPI (coming soon):

```bash
pip install datafoundry
```

---

## Basic Usage Example

Here’s a minimal example showing how to reorganize a dataset:

```python
from datafoundry.datasets.reorganizer import DatasetReorganizer

reorg = DatasetReorganizer(
    source_dir="data/source_dataset",
    target_dir="data/reorganized_dataset",
    structure="train/class/samples"  # desired output structure
)

reorg.run()
```

Or directly from the command line:

```bash
datafoundry reorganize --source ./data/source_dataset --target ./data/reorganized_dataset --structure train/class/samples
```

---

## Project Structure

```
datafoundry/
├── core.py
├── cli.py
├── datasets/
│   ├── reorganizer.py
│   ├── splitter.py
│   ├── analyzer.py
│   └── metadata.py
└── utils/
    ├── io.py
    └── logging.py
```

---

## Tests

Run the test suite using `pytest`:

```bash
pytest -v
```

---

##  License

This project is licensed under the **MIT License** – see the [LICENSE](https://github.com/mehdi-jamaseb/datafoundry/blob/master/LICENSE) file for details.

---

## Contributing

Contributions are welcome!
Please open an issue or submit a pull request with improvements, bug fixes, or new features.

---

## Roadmap

* [ ] Dataset preview and summary statistics
* [ ] Parallel file operations for large datasets
* [ ] Built-in visualization for folder structures
* [ ] Integration with HuggingFace Datasets and PyTorch DataLoader

---

## Author

Developed and maintained by [Mehdi](https://github.com/mehdi-jamaseb).

