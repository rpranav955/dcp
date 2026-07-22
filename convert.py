import numpy as np
import open3d as o3d
import h5py

def ply_to_h5(ply_path, h5_path):
    """
    Converts a .ply point cloud file into an .h5 file.
    Saves point coordinates and colors as separate datasets.
    """
    print(f"Reading PLY file from: {ply_path}...")
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(ply_path)
    
    # Convert points and colors to numpy arrays
    points = np.asarray(pcd.points)
    colors = np.asarray(pcd.colors)  # Normalized between 0.0 and 1.0
    
    print(f"Loaded {len(points)} points.")

    # Write to HDF5 format
    print(f"Writing to H5 file at: {h5_path}...")
    with h5py.File(h5_path, 'w') as h5_file:
        # Create dataset for point coordinates (N, 3)
        h5_file.create_dataset('data', data=points, compression='gzip', dtype='float32')
        
        # Create dataset for colors if they exist
        if colors.size > 0:
            h5_file.create_dataset('color', data=colors, compression='gzip', dtype='float32')
            
    print("Conversion completed successfully!")

if __name__ == "__main__":
    # Define your file paths here
    input_ply = "bun045.ply"
    output_h5 = "output_bun045.h5"
    
    ply_to_h5(input_ply, output_h5)