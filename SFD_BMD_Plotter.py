import pandas as pd
import matplotlib.pyplot as plt

# Reading Excel File
df = pd.read_excel('data/SFS_Screening_SFDBMD.xlsx') 

print(df.head())

# To cross-check the column name from the Excel file
x = df['Distance (m)']
shear_force = df['SF (kN)']
bending_moment = df['BM (kN-m)']

# For Creating plots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# For Plotting Shear Force Diagram (SFD)
axs[0].plot(x, shear_force, color='blue', label='Shear Force')
axs[0].set_title('Shear Force Diagram')
axs[0].set_xlabel('Distance (m)')
axs[0].set_ylabel('Shear Force (kN)')
axs[0].grid(True)

# For Plotting Bending Moment Diagram (BMD)
axs[1].plot(x, bending_moment, color='green', label='Bending Moment')
axs[1].set_title('Bending Moment Diagram')
axs[1].set_xlabel('Distance (m)')
axs[1].set_ylabel('Bending Moment (kNm)')
axs[1].grid(True)

plt.tight_layout()
plt.show()
