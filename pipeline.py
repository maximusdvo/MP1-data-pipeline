""" data pipeline"""

import argparse
import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(
        level = level,
        format = "%(asctime)s %(levelname)-8s %(message)s",
        datefmt = "%H:%M:%S"
     #for the format, we could add -8s if we want visually to match/ We could also optionally addthe year and date
    )


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description = "Data Processing Pipeline")

    parser.add_argument("--input", "-i",
                        required = True,
                        help = "Path to the input file")
    parser.add_argument("--output", "-o",
                        required = True,
                        help = "Path to the output file")

    parser.add_argument("--format",
                        choices= ["csv", "json"],
                        default = "csv",
                        help = "Output format: csv or json (default:csv)" )

    parser.add_argument("--verbose", "-v",
                        action = "store_true",
                        help = "Enable Verbose logging")
    #Verbose is the flag that automatically controls how much detail is logged when the script is ran

    return parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if Path(filepath).is_file():
        logger.info(f"Input file validates: {filepath}")
        return True
    else:
        logger.error(f"Input File not found: {filepath}")
        return False


def main():
    """Main pipeline function."""
    args = parse_arguments()

    setup_logging(args.verbose)

    logger.debug(f"Arguments parsed: input={args.input}, output={args.output}, format={args.format}")

    is_valid = validate_input(args.input)

    if not is_valid:
        sys.exit(1)

    logger.info("Pipeline setup complete. Ready to process.")


if __name__ == "__main__":
    main()
