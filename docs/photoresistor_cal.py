from matplotlib import pyplot as plt

intensity = [1, 2, 3, 4, 5, 6, 7]
r2 = [165000, 108000, 12000, 4000, 2500, 900, 900]  # ohm, 64 m


# voltage divider conversion to resistance on r1, 15k ohm
# r1 = 15000
# v_in = 5  # v
# r2 = []
# v_out = [i / 1000 for i in v_out]
# for i, v in enumerate(v_out):
#     vt = v_in / v
#     r2 = [r1 * ((v_in / v) - 1) for v in v_out]


# r2 = [r1 * ((v_in / v) - 1) for v in v_out]
print(r2)

# plot
plt.plot(intensity, r2)
plt.xlabel("Intensity (unitless)")
plt.ylabel(r"$R_{PRes}$ ($\Omega$)")
plt.title("Photoresistor Calibration over arbitrary brightness. R1 = 15k.")
# plt.show()
plt.savefig("newcalibration.png")
