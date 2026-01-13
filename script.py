import matplotlib
matplotlib.use("Qt5Agg")


import os
import numpy as np
import matplotlib.pyplot as plt
import pims

# -------------------------------
# Function to load spectra
# -------------------------------
def load_spe_folder(folder_path, label):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".spe")]
    labeled_spectra = []
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            data = pims.open(file_path)
            spectrum = np.array(data[0])
            if spectrum.ndim > 1:
                spectrum = spectrum.flatten()
            labeled_spectra.append((spectrum, label))
        except Exception as e:
            print("Failed to load {file_name}: {e}")
    return labeled_spectra

# -------------------------------
# Function to compute mean/std
# -------------------------------
def compute_mean_std(spectra_array):
    mean_spectrum = np.mean(spectra_array, axis=0)
    std_spectrum = np.std(spectra_array, axis=0)
    return mean_spectrum, std_spectrum

# -------------------------------
# Base folders for all groups
# -------------------------------
base_folders = {
    "02": [
        "/Users/hai/Documents/SpecData/Experiment/Group_1/g1/02",
        "/Users/hai/Documents/SpecData/Experiment/Group_2/g2/02",
        "/Users/hai/Documents/SpecData/Experiment/Group_3/g3/02",
        "/Users/hai/Documents/SpecData/Experiment/Group_4/g4/02",
        "/Users/hai/Documents/SpecData/Experiment/Group_5/g5/02",
        "/Users/hai/Documents/SpecData/Experiment/Group_6/g6/02",
    ],
    "06": [
        "/Users/hai/Documents/SpecData/Experiment/Group_1/g1/06",
        "/Users/hai/Documents/SpecData/Experiment/Group_2/g2/06",
        "/Users/hai/Documents/SpecData/Experiment/Group_3/g3/06",
        "/Users/hai/Documents/SpecData/Experiment/Group_4/g4/06",
        "/Users/hai/Documents/SpecData/Experiment/Group_5/g5/06",
        "/Users/hai/Documents/SpecData/Experiment/Group_6/g6/06",
    ],
    "arbp": [
        "/Users/hai/Documents/SpecData/Experiment/Group_1/g1/arbp",
        "/Users/hai/Documents/SpecData/Experiment/Group_2/g2/arbp",
        "/Users/hai/Documents/SpecData/Experiment/Group_3/g3/arbp",
        "/Users/hai/Documents/SpecData/Experiment/Group_4/g4/arbp",
        "/Users/hai/Documents/SpecData/Experiment/Group_5/g5/arbp",
        "/Users/hai/Documents/SpecData/Experiment/Group_6/g6/arbp",
    ],
}

# -------------------------------
# Load and compute mean/std
# -------------------------------
results = {}
for label, folders in base_folders.items():
    all_labeled_spectra = []
    for folder in folders:
        all_labeled_spectra.extend(load_spe_folder(folder, label))
    if all_labeled_spectra:
        all_spectra = np.array([spec for spec, lbl in all_labeled_spectra])
        mean_spectrum, std_spectrum = compute_mean_std(all_spectra)
        results[label] = (mean_spectrum, std_spectrum)

# -------------------------------
# Ask user for pixel range
# -------------------------------
start = int(input("Enter start pixel: "))
end = int(input("Enter end pixel: "))

# -------------------------------
# Plot
# -------------------------------
plt.figure(figsize=(14,7))
colors = {"02": "blue", "06": "green", "arbp": "red"}

for label, (mean_spectrum, std_spectrum) in results.items():
    # Apply the pixel cut here
    x = np.arange(len(mean_spectrum))[start:end+1]
    mean_cut = mean_spectrum[start:end+1]
    std_cut = std_spectrum[start:end+1]

    plt.plot(x, mean_cut, color=colors[label], label=label)
    plt.fill_between(x,
                     mean_cut - std_cut,
                     mean_cut + std_cut,
                     color=colors[label], alpha=0.2)

plt.title(f"Mean ± Std Spectra ({start}–{end}) for 02, 06, and arbp")
plt.xlabel("Pixel")
plt.ylabel("Intensity")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
