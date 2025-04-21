import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ابعاد اتاق (متر)
طول_اتاق = 7
عرض_اتاق = 3

# ایجاد شکل و محور
fig, ax = plt.subplots(figsize=(10, 5))

# رسم اتاق
اتاق = patches.Rectangle((0, 0), طول_اتاق, عرض_اتاق, linewidth=2, edgecolor='black', facecolor='lightgrey')
ax.add_patch(اتاق)

# رسم قفسه‌ها
قفسه_۱ = patches.Rectangle((0.5, 0), 6, 1, linewidth=1, edgecolor='blue', facecolor='skyblue')
قفسه_۲ = patches.Rectangle((1.5, 0), 5, 1, linewidth=1, edgecolor='red', facecolor='salmon')
ax.add_patch(قفسه_۱)
ax.add_patch(قفسه_۲)

# تنظیمات نمایش
ax.set_xlim(0, طول_اتاق)
ax.set_ylim(0, عرض_اتاق)
ax.set_aspect('equal')
plt.grid(True)
plt.title('نمای افقی اتاق با دو قفسه')
plt.xlabel('طول (متر)')
plt.ylabel('عرض (متر)')
plt.show()