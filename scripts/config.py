from pathlib import Path
from dataclasses import dataclass

@dataclass
class Paths:
    project_root: Path
    src_dir: Path
    metadata_dir: Path
    metadata_scripts_dir: Path
    schemas_dir: Path
    scripts_dir: Path
    site_src_dir: Path
    site_dir: Path
    template_path: Path

    @classmethod
    def from_project_root(cls, root: Path):
        return cls(
            project_root=root,
            src_dir=root / "src",
            metadata_dir=root / "metadata",
            metadata_scripts_dir=root / "metadata" / "scripts",
            schemas_dir=root / "metadata" / "schemas",
            scripts_dir=root / "scripts",
            site_src_dir=root / "site_src",
            site_dir=root / "site",
            template_path=root / "site_src" / "template_page.html"
        )

@dataclass
class BuildConfig:
    paths: Paths
    verbose: bool = False
    continue_on_error: bool = False
    skip_validation: bool = False
    with_assets: bool = False
