from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief("Shardul - 2.jpeg")
dominant_color = ct.get_color(quality=1)

plt.imshow([[dominant_color]])
plt.show()

palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

