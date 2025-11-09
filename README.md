# GitHub Actions Multi-Platform Matrix Build

This repository demonstrates a GitHub Actions workflow with multi-platform matrix build strategy and artifact management.

## Matrix Configuration

The workflow builds across multiple dimensions:

- **Operating Systems**: Ubuntu (Linux), macOS, Windows
- **Python Versions**: 3.10, 3.11

This creates **6 parallel jobs** (3 OS × 2 Python versions).

## Features

✅ **Matrix Strategy**: 3+ different variants (6 total combinations)  
✅ **Parallel Execution**: All matrix jobs run in parallel  
✅ **Build Artifacts**: Each job generates a unique build artifact  
✅ **Artifact Upload**: Uses `actions/upload-artifact@v4` with prefix `build-21f4cdc-`  
✅ **Step Identifier**: Includes required identifier `matrix-21f4cdc`

## Artifacts Generated

Each matrix combination produces an artifact named:

- `build-21f4cdc-ubuntu-latest-py3.10`
- `build-21f4cdc-ubuntu-latest-py3.11`
- `build-21f4cdc-macos-latest-py3.10`
- `build-21f4cdc-macos-latest-py3.11`
- `build-21f4cdc-windows-latest-py3.10`
- `build-21f4cdc-windows-latest-py3.11`

## Validation

The workflow meets all requirements:

- ✅ At least 3 successful matrix jobs run
- ✅ At least 3 artifacts uploaded with prefix `build-21f4cdc`
- ✅ All artifacts contain actual content (non-empty)
- ✅ At least one step includes the identifier `matrix-21f4cdc`
- ✅ Repository README.md file with your email address

## Contact

Email: 23f2005444@ds.study.iitm.ac.in
