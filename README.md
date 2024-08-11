# AuroraEditor Extension Manifest Model Generator

This repository contains a Python script to generate Swift model classes from a JSON schema. The generated Swift files are automatically created based on the schema and follow a specific format required by Aurora Editor.

## Requirements

To use this script, you'll need the following:

- Python 3.6 or higher
- The `Jinja2` templating engine for Python

## Setup

### 1. Install Python

Ensure you have Python 3.6 or higher installed. You can check your Python version with:

```bash
    python3 --version
```
If Python is not installed, you can download it from python.org.

## Setup

1. **Install Python:**  
   Ensure you have Python 3.6 or higher installed. You can check your Python version by running a version command in your terminal or command prompt.

2. **Create a Virtual Environment (Optional but Recommended):**  
   It is recommended to create a virtual environment to manage your dependencies.

   ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On macOS/Linux
    myenv\Scripts\activate  # On Windows
   ```

3. **Install Required Packages:**  
   Install the required Python packages using `pip`.
   ```bash
   pip install jinja2
   ```

4. **Run the Script:**  
   Place your JSON schema file (e.g., `ExtensionManifestScheme.json`) in the same directory as the script or specify the path in the script. 
   
   Run the script to generate Swift model files. 
   ```bash
   python3 generate_swift_models.py
   ```
   The generated Swift files will be saved in the `GeneratedSwiftModels` directory.

## Contributing

**We do not accept Pull Requests (PRs) on this repository.** Any changes to the schema or generator should be discussed before implementation. Please join the discussion at the following link:

[Discussion: Changes to Schema or Generator](https://github.com/orgs/AuroraEditor/discussions/769)

## License

This project is licensed under the MIT License.