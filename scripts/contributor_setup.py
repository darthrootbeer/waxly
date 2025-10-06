#!/usr/bin/env python3
"""
Contributor setup script for the Vinyl Lexicon project.
Helps new contributors get started with the development environment.
"""

import os
import subprocess
import sys
from pathlib import Path

import click


def run_command(cmd, description, check=True):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, check=check, capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed:")
            print(result.stderr)
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required, found {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} is compatible")
    return True


def check_git():
    """Check if git is available."""
    if run_command("git --version", "Checking Git installation", check=False):
        return True
    print("❌ Git is required but not found. Please install Git first.")
    return False


def setup_virtual_environment():
    """Set up Python virtual environment."""
    venv_path = Path("venv")

    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True

    if run_command("python -m venv venv", "Creating virtual environment"):
        print("✅ Virtual environment created")
        return True
    return False


def install_dependencies():
    """Install Python dependencies."""
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False

    # Determine the correct pip command based on OS
    if os.name == "nt":  # Windows
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix-like
        pip_cmd = "venv/bin/pip"

    if run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies"):
        return True
    return False


def validate_setup():
    """Validate the setup by running validation scripts."""
    # Determine the correct python command based on OS
    if os.name == "nt":  # Windows
        python_cmd = "venv\\Scripts\\python"
    else:  # Unix-like
        python_cmd = "venv/bin/python"

    if run_command(
        f"{python_cmd} scripts/validate_terms.py", "Validating term files", check=False
    ):
        print("✅ Validation completed (warnings are normal for new setups)")
        return True
    return False


def test_mkdocs():
    """Test MkDocs installation and build."""
    # Determine the correct mkdocs command based on OS
    if os.name == "nt":  # Windows
        mkdocs_cmd = "venv\\Scripts\\mkdocs"
    else:  # Unix-like
        mkdocs_cmd = "venv/bin/mkdocs"

    if run_command(f"{mkdocs_cmd} build --quiet", "Testing MkDocs build", check=False):
        print("✅ MkDocs build successful")
        return True
    return False


@click.command()
@click.option("--skip-validation", is_flag=True, help="Skip validation steps")
@click.option("--skip-mkdocs", is_flag=True, help="Skip MkDocs testing")
def main(skip_validation, skip_mkdocs):
    """Set up the Vinyl Lexicon development environment."""
    print("🚀 Setting up Vinyl Lexicon development environment")
    print("=" * 50)

    # Check prerequisites
    if not check_python_version():
        return 1

    if not check_git():
        return 1

    # Set up virtual environment
    if not setup_virtual_environment():
        return 1

    # Install dependencies
    if not install_dependencies():
        return 1

    # Validate setup
    if not skip_validation:
        if not validate_setup():
            print("⚠️  Validation had issues, but setup can continue")

    # Test MkDocs
    if not skip_mkdocs:
        if not test_mkdocs():
            print("⚠️  MkDocs test had issues, but setup can continue")

    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate the virtual environment:")
    if os.name == "nt":  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix-like
        print("   source venv/bin/activate")
    print("2. Start the development server:")
    print("   mkdocs serve")
    print("3. Open http://127.0.0.1:8000 in your browser")
    print("\nFor more information, see docs/contribute.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
