import h5py
import pandas as pd

# Replace 'input.hdf5' with the path to your HDF5 file
input_hdf5_file = 'demo.hdf5'

# Open the HDF5 file for reading
with h5py.File(input_hdf5_file, 'r') as hdf5_file:
    # Assuming the dataset is named 'data' within the HDF5 file
    dataset = hdf5_file['data'][:]

# Convert the dataset to a Pandas DataFrame
df = pd.DataFrame(dataset)

# Replace 'output.csv' with the desired name for your CSV file
output_csv_file = 'output.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_csv_file, index=False)

print(f'CSV file saved as {output_csv_file}')
