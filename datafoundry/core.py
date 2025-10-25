import os
from pathlib import Path
from typing import Optional

class BasePipeline:
    """
    Base class for dataset pipelines in DataFoundry.
    Provides utility methods for path handling and logging.
    """

    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir).resolve()
        self.target_dir = Path(target_dir).resolve()
        self._validate_dirs()

    def _validate_dirs(self):
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory does not exist: {self.source_dir}")
        if not self.target_dir.exists():
            self.target_dir.mkdir(parents=True, exist_ok=True)

    def log(self, message: str):
        print(f"[DataFoundry] {message}")

    def run(self):
        """Override this method in subclasses"""
        raise NotImplementedError("Subclasses must implement the run() method")
