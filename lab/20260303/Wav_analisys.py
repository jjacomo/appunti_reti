import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# ---- 1. Generazione di un segnale di test ----
fs = 44100  # Frequenza di campionamento originale (Hz)
duration = 0.05  # 50 ms di segnale
t = np.linspace(0, duration, int(fs * duration),
                endpoint=False)  # Asse temporale
freq = 440  # Frequenza della sinusoide (Hz)
signal = 0.5 * np.sin(2 * np.pi * freq * t)  # Sinusoide

plt.figure(figsize=(10, 4))
plt.plot(t[:500], signal[:500], label="Segnale originale",
         marker='o', linestyle='-')
plt.xlabel("Tempo (s)")
plt.ylabel("Ampiezza")
plt.title("Segnale Sinusoidale Originale (440 Hz)")
plt.legend()
plt.grid(True)
plt.show()

# ---- 2. Campionamento a 8 kHz ----
fs_new = 8000  # Nuova frequenza di campionamento
t_new = np.linspace(0, duration, int(fs_new * duration), endpoint=False)
signal_sampled = 0.5 * np.sin(2 * np.pi * freq * t_new)

plt.figure(figsize=(10, 4))
plt.plot(t[:500], signal[:500], label="Segnale originale",
         linestyle='-', alpha=0.5)
plt.scatter(t_new[:100], signal_sampled[:100], color='r',
            label="Campioni (8 kHz)", zorder=3)
plt.xlabel("Tempo (s)")
plt.ylabel("Ampiezza")
plt.title("Effetto del Campionamento (da 44.1 kHz a 8 kHz)")
plt.legend()
plt.grid(True)
plt.show()

# ---- 3. Quantizzazione a 8 bit ----


def quantize(signal, bits):
    levels = 2**bits
    min_val, max_val = signal.min(), signal.max()
    signal_scaled = (signal - min_val) / (max_val -
                                          min_val)  # Normalizza tra 0 e 1
    signal_quantized = np.round(
        signal_scaled * (levels - 1)) / (levels - 1)  # Quantizza
    # Ritorna alla scala originale
    return signal_quantized * (max_val - min_val) + min_val


signal_quantized = quantize(signal_sampled, 8)

plt.figure(figsize=(10, 4))
plt.plot(t_new[:100], signal_sampled[:100], linestyle='-',
         alpha=0.5, label="Campionato (8 kHz)")
plt.scatter(t_new[:100], signal_quantized[:100], color='g',
            label="Quantizzato a 8 bit", zorder=3)
plt.xlabel("Tempo (s)")
plt.ylabel("Ampiezza")
plt.title("Effetto della Quantizzazione a 8 bit")
plt.legend()
plt.grid(True)
plt.show()

# ---- 4. Pacchettizzazione in blocchi da 10ms ----
packet_size = int(fs_new * 0.01)  # Blocchi da 10ms
num_packets = len(signal_quantized) // packet_size
packets = [signal_quantized[i *
                            packet_size:(i + 1) * packet_size] for i in range(num_packets)]

print(f"Segnale diviso in {len(packets)} pacchetti da {
      packet_size} campioni ciascuno.")

# ---- 5. Salvataggio del file audio quantizzato ----
sf.write("output_quantized.wav", signal_quantized, fs_new)
print("File audio quantizzato salvato come 'output_quantized.wav'.")
