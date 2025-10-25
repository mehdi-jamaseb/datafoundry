import os
import shutil
from pathlib import Path
from datafoundry.core import BasePipeline

class DatasetReorganizer(BasePipeline):
    """
    Reorganize dataset folder structure.
    Supports copy or symlink mode.
    """

    def __init__(self, source_dir: str, target_dir: str, structure: str = "train/class/samples",
                 copy_mode: str = "symlink"):
        super().__init__(source_dir, target_dir)
        self.structure = structure
        if copy_mode not in ["copy", "symlink"]:
            raise ValueError("copy_mode must be either 'copy' or 'symlink'")
        self.copy_mode = copy_mode

    def run(self):
        self.log(f"Starting reorganization: {self.source_dir} -> {self.target_dir}")
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                src_file = Path(root) / file
                relative_path = src_file.relative_to(self.source_dir)
                # For now, simple copy preserving subdirectories
                dest_file = self.target_dir / relative_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)

                if self.copy_mode == "copy":
                    shutil.copy2(src_file, dest_file)
                elif self.copy_mode == "symlink":
                    if not dest_file.exists():
                        os.symlink(src_file, dest_file)
                self.log(f"Processed: {src_file} -> {dest_file}")

        self.log("Reorganization completed.")
