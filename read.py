import h5py

# Specify the path to the HDF5 file
hdf5_file_path = 'your_file.hdf5'

# Function to recursively print the contents of an HDF5 group
def print_hdf5_group(group, prefix=""):
    for key in group.keys():
        item = group[key]
        if isinstance(item, h5py.Group):
            print(f"Group: {prefix}/{key}")
            print_hdf5_group(item, prefix=f"{prefix}/{key}")
        elif isinstance(item, h5py.Dataset):
            print(f"Dataset: {prefix}/{key} (Shape: {item.shape}, Dtype: {item.dtype})")
        else:
            print(f"Unknown: {prefix}/{key} (Type: {type(item)})")

# Open the HDF5 file for reading
with h5py.File(hdf5_file_path, 'r') as hdf5_file:
    # Start with the root group '/'
    print_hdf5_group(hdf5_file, prefix="")
