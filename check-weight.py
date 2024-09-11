import h5py

with h5py.File('model_data/yolo_weights.h5', 'r') as f:
    for key in f.keys():
        print(key, f[key])