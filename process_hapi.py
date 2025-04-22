import numpy as np
import pandas as pd
from py4cats import higstract

def read_hapi_data(header_file, data_file):
    """Read HAPI data from header and data files"""
    # Read header file to get metadata
    with open(header_file, 'r') as f:
        header_lines = f.readlines()
    
    # Read data file
    data = pd.read_csv(data_file, delim_whitespace=True, header=None)
    
    # Extract wavelength information from header
    wavelength = None
    for line in header_lines:
        if 'Wavelength' in line:
            wavelength = float(line.split()[1])
            break
    
    return wavelength, data

def prepare_for_higstract(wavelength, data):
    """Prepare data for higstract function"""
    # Assuming data contains intensity values
    # You might need to adjust this based on your actual data structure
    intensity = data.iloc[:, 0].values  # Adjust column index as needed
    
    # Create the input format expected by higstract
    # higstract expects: wavelength, intensity, [optional parameters]
    return wavelength, intensity

def main():
    # File paths
    header_file = 'data/CO.header'
    data_file = 'data/CO.data'
    
    # Read data
    wavelength, data = read_hapi_data(header_file, data_file)
    
    # Prepare data for higstract
    wavelength, intensity = prepare_for_higstract(wavelength, data)
    
    # Apply higstract
    # You can adjust parameters as needed
    result = higstract(wavelength, intensity)
    
    # Save or process the results
    print("Higstract processing completed")
    print("Results:", result)

if __name__ == "__main__":
    main() 