import numpy as np
import matplotlib.pyplot as plt

# Konstanta
g = 9.8  # percepatan gravitasi (m/s^2)
v0 = 0   # kecepatan awal (m/s)
h0 = 5 # ketinggian awal (m)

# Menghitung waktu jatuh
t_fall = np.sqrt(2 * h0 / g)
print("Waktu yang diperlukan benda untuk mencapai tanah = ", t_fall, " s")

# Menghitung kecepatan saat mencapai tanah
v_final = g * t_fall
print("Kecepatan saat mencapai tanah = ", v_final, " m/s")

# Menghitung ketinggian akhir (seharusnya 0 karena benda mencapai tanah)
h_final = h0 - 0.5 * g * t_fall**2
print("Ketinggian Akhir = ", h_final, " m")

# Membuat array waktu dari 0 hingga waktu jatuh
t = np.linspace(0, t_fall, 1000)

# Menghitung kecepatan sebagai fungsi waktu
v = g * t

# Menghitung ketinggian sebagai fungsi waktu
h = h0 - 0.5 * g * t**2

# Plot kecepatan terhadap waktu
fig, ax2 = plt.subplots()
ax2.plot(t, v)
ax2.set(xlabel='t (s)', ylabel='v (m/s)', title='Grafik Kecepatan terhadap Waktu')
ax2.grid()

# Plot ketinggian terhadap waktu
fig, ax1 = plt.subplots()
ax1.plot(t, h)
ax1.set(xlabel='t (s)', ylabel='h (m)', title='Grafik Ketinggian terhadap Waktu')
ax1.grid()

plt.show()
