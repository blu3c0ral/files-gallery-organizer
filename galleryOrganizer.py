import argparse

from main import main


def process_command_line_args():
    parser = argparse.ArgumentParser(description="Process optional command line arguments.")

    # Define the flags for each argument
    parser.add_argument('--directory', type=str, help='The base directory to scan.')
    parser.add_argument('--keep-original-directory', action='store_true', help='Keep the original directory structure.')
    parser.add_argument('--dest-base-dir', type=str, help='Specify the base directory for destination.')
    parser.add_argument('--group-to-years', action='store_true', help='Group files into year-based directories.')
    parser.add_argument('--separator', type=str, default='_', help='Specify the separator for file renaming.')
    parser.add_argument('--flipped', action='store_true', help='Flip the file names.')
    parser.add_argument('--move-files', action='store_true', help='Move the files instead of copying.')
    parser.add_argument('--file-extensions', nargs='+', type=str, help='Specify the file extensions to process.')

    # Parse the command line arguments
    args = parser.parse_args()

    # Return the parsed arguments
    return args


if __name__ == '__main__':
    # Process the command line arguments
    args = process_command_line_args()

    # Set the settings based on the command line arguments
    if not args.directory:
        raise ValueError("The directory argument is required.")
    if not args.dest_base_dir:
        raise ValueError("The dest-base-dir argument is required.")

    # Run the main function
    main(args.directory, args)
