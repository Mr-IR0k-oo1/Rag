# Configuration README

Hi team, Anvin here. This file explains how we'll manage configuration for the Skyron project.

## Objective

As our project grows, we'll have more and more configuration settings to manage. This includes things like:
- Model parameters
- Database connection strings
- File paths
- Hyperparameters for training

Instead of hard-coding these values in our scripts, we'll store them in a centralized location. This will make it easier to manage our configuration and to switch between different settings (e.g., for development, testing, and production).

## Implementation Plan

We'll use a simple and flexible approach for managing our configuration:

1.  **YAML Files:** We'll use YAML files to store our configuration settings. YAML is a human-readable data serialization format that is easy to use and to parse.
2.  **A Single Configuration File:** We'll start with a single configuration file, `config/config.yaml`. This file will contain all the configuration settings for our project.
3.  **A Configuration Module:** We'll create a Python module, `src/config.py`, to load our configuration file and make the settings available to the rest of the application. This module will:
    - Load the `config.yaml` file.
    - Provide a simple interface for accessing the configuration settings (e.g., `config.get('database.host')`).

## How to Contribute

- **Develop the `config.py` module:** Create the initial version of the module with the functionality described above.
- **Help define the configuration structure:** As we develop the project, we'll need to decide on a clear and consistent structure for our configuration file.

By managing our configuration properly, we'll make our project more robust, more flexible, and easier to maintain.
