import h5py, numpy as np, matplotlib.pyplot as plt

ruta2 = "Data Set Para entrenamiento\\anetnna_dataset\\train_test_split_S11.h5"

with h5py.File(ruta2, "r") as f:

    s11 = f["S11_combine_train"]
    params = f["final_params_combine_train"]
    pattern = f["pattern_combine_train"]

    # --- S11 (curva)
    plt.figure()
    plt.plot(s11[0])
    plt.title("S11 (train[0])")
    plt.xlabel("Frecuencia (índice)")
    plt.ylabel("Magnitud")
    plt.grid()
    plt.show()

    # --- Parámetros
    plt.figure()
    plt.bar(range(8), params[0])
    plt.title("Parámetros (train[0])")
    plt.show()

    # --- Patrón
    plt.figure()
    plt.imshow(pattern[0], cmap="jet")
    plt.colorbar()
    plt.title("Pattern (train[0])")
    plt.show()

    # --- Relación rápida S11 vs patrón (misma muestra)
    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.plot(s11[0])
    plt.title("S11")

    plt.subplot(1,2,2)
    plt.imshow(pattern[0], cmap="jet")
    plt.title("Pattern")

    plt.show()