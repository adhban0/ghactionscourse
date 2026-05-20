"""Small CLI-friendly helper for CI/CD practice."""

from __future__ import annotations

import argparse


def build_status_message(project: str, branch: str, passed_checks: int, total_checks: int) -> str:
    """Build a short status message for a CI run."""
    if not project.strip():
        raise ValueError("project must not be empty")
    if not branch.strip():
        raise ValueError("branch must not be empty")
    if passed_checks < 0:
        raise ValueError("passed_checks must be non-negative")
    if total_checks <= 0:
        raise ValueError("total_checks must be positive")
    if passed_checks > total_checks:
        raise ValueError("passed_checks cannot exceed total_checks")

    return (
        f"{project} on {branch}: "
        f"{passed_checks}/{total_checks} checks passed"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a simple CI status message.")
    parser.add_argument("project", help="Project name")
    parser.add_argument("branch", help="Branch name")
    parser.add_argument("passed_checks", type=int, help="Number of passing checks")
    parser.add_argument("total_checks", type=int, help="Total number of checks")
    args = parser.parse_args()

    print(
        build_status_message(
            args.project,
            args.branch,
            args.passed_checks,
            args.total_checks,
        )
    )


if __name__ == "__main__":
    main()
