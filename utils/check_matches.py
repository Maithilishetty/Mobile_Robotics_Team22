import numpy as np
import matplotlib.pyplot as plt

vals_u = []
sum = 0
with open("Matches.txt") as f:
    lines = f.readlines()
    for line in lines:
        if "Matches found: " in line:
            loc = line.index("Matches found: ")
            loc_val = loc + len("Matches found: ")
            val = float(line[loc_val:])
            sum += val
            vals_u.append(val)
avg_u = sum / len(vals_u)
print("Unenhanced: ", avg_u)

vals_e = []
vals_ten = []
sum = 0
with open("Matches_simple.txt") as f:
    lines = f.readlines()
    for line in lines:
        if "Matches found: " in line and len(vals_e) <= len(vals_u):
            loc = line.index("Matches found: ")
            loc_val = loc + len("Matches found: ")
            val = float(line[loc_val:])
            sum += val
            vals_e.append(val)
            vals_ten.append(15)
avg_e = sum / len(vals_e)
print("Enhanced: ", avg_e)

plt.plot(vals_e, 'g', label="Enhanced")
plt.plot(vals_u, 'r', label="Unenhanced")
plt.plot(vals_ten, 'b')
plt.xlabel("Frames")
plt.ylabel("Number of Matches")
plt.title("ORB_SLAM3 Sequence 1 Match Rate")
plt.legend()
plt.show()
