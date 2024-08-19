#!/usr/bin/env python3

import argparse
import os
import subprocess


def get_committed_files(project_path, commit_count=1):
    """
    Retrieves the list of files committed in the specified project path for the given number of commits.

    Args:
        project_path (str): The path to the Git repository.
        commit_count (int, optional): The number of commits to check. Defaults to 1.

    Returns:
        list: A list of committed file names.
        Returns an empty list if an error occurs or no files are found.
    """
    try:
        # Change the directory to the specified project path
        os.chdir(project_path)

        # Run the git command to list committed files for the specified number of commits
        result = subprocess.run(
            [
                "git",
                "log",
                f"-{commit_count}",
                "--name-only",
                "--pretty=format:",
                "--diff-filter=AMDR",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )

        # Get the output and split by lines to get file names
        committed_files = result.stdout.strip().split("\n")

        # Filter out any empty strings
        committed_files = [file for file in committed_files if file]

        return committed_files

    except subprocess.CalledProcessError as e:
        print(
            f"An error occurred while trying to get committed files for {project_path}: {e}"
        )
        return []

    except FileNotFoundError:
        print(f"Project path '{project_path}' not found.")
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get committed files from a Git repository."
    )
    parser.add_argument(
        "-p", "--project_path", required=True, help="The path to the Git repository."
    )
    parser.add_argument(
        "-c",
        "--commits",
        type=int,
        default=1,
        help="The number of commits to check (default: 1).",
    )

    args = parser.parse_args()

    print(f"Checking project: {args.project_path}")
    files = get_committed_files(args.project_path, commit_count=args.commits)
    if files:
        print(
            f"Committed files in the last {args.commits} commit(s) for project '{args.project_path}':"
        )
        for file in files:
            print(file)
    else:
        print(
            f"No committed files found in the last {args.commits} commit(s) for project '{args.project_path}' or an error occurred."
        )