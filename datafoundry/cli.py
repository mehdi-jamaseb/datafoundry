import argparse
import sys
from datafoundry.datasets.reorganizer import DatasetReorganizer

def main():
    parser = argparse.ArgumentParser(
        prog="datafoundry",
        description="DataFoundry CLI: manage and reorganize AI datasets."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: reorganize
    reorganize_parser = subparsers.add_parser(
        "reorganize",
        help="Reorganize dataset folder structure"
    )
    reorganize_parser.add_argument(
        "--source", "-s",
        required=True,
        help="Path to the source dataset directory"
    )
    reorganize_parser.add_argument(
        "--target", "-t",
        required=True,
        help="Path to the target dataset directory"
    )
    reorganize_parser.add_argument(
        "--structure",
        default="train/class/samples",
        help="Target folder structure (default: train/class/samples)"
    )
    reorganize_parser.add_argument(
        "--copy-mode",
        choices=["copy", "symlink"],
        default="symlink",
        help="Copy mode: copy files or create symlinks (default: symlink)"
    )

    args = parser.parse_args()

    if args.command == "reorganize":
        reorganizer = DatasetReorganizer(
            source_dir=args.source,
            target_dir=args.target,
            structure=args.structure,
            copy_mode=args.copy_mode
        )
        reorganizer.run()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
