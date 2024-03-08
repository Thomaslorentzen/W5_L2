This project is developed on VS code, and this guide assumes you are using the same.

Python version 3.9 was used, and it is thus expected that you will use the same version for compatibility

To create a python virtual environment, run the following command:

# Create a Virtual Environment
python -m venv myenv (arbitrary name for the virtual environment)

This assumes you are already in the correct terminal in the IDE

# Activate the Virtual Environment
source myenv/bin/activate  # For Unix/macOS
myenv\Scripts\activate      # For Windows

# Install Dependencies
pip install -r requirements.txt

The requirements.txt file is already included in the source code. If it does not recognize, try and move it to the venv folder you just created
