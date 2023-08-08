import numpy as np
import matplotlib.pyplot as plt

# Setting parameters for the model
T = 0.25
beta_1_i = 2.00
beta_2_i = 1.5
beta_1_j = 2.00
beta_2_j = 1.00
N_i = 0.00
N_j = 0.50
alpha = round(float(4 / 6), 3)  # hawls


# Defining the best reply functions for i and j
def br_i(x_j):
    K = beta_1_i + beta_2_i + ((1 - alpha) ** 2)
    n_i = beta_1_i * T + beta_2_i * N_i
    return (x_j * K - n_i) / ((1 - alpha) * alpha) * np.ones_like(x_j)


def br_j(x_i):
    L = beta_1_j + beta_2_j + (alpha**2)
    return (
        (beta_1_j * T + beta_2_j * N_j + alpha * (1 - alpha) * x_i)
        / L
        * np.ones_like(x_i)
    )


# Finding the Nash equilibrium
def nash_equilibrium():
    K = beta_1_i + beta_2_i + (1 - alpha) ** 2
    L = beta_1_j + beta_2_j + alpha**2
    n_i = beta_1_i * T + beta_2_i * N_i
    n_j = beta_1_j * T + beta_2_j * N_j
    x_i = (n_i * L + (1 - alpha) * alpha * n_j) / (
        K * L - (alpha**2 * (1 - alpha) ** 2)
    )
    x_j = (n_j * K + (1 - alpha) * alpha * n_i) / (
        K * L - (alpha**2 * (1 - alpha) ** 2)
    )
    return (round(x_i, 3) * np.ones_like(x_i), round(x_j, 3) * np.ones_like(x_j))


# Plotting the best reply functions and Nash equilibrium
print(nash_equilibrium())
x = np.linspace(-1, +1, 100)
plt.plot(x, br_i(x), label="Doves", color="g")
plt.plot(x, br_j(x), label="Hawks", color="k")
nash = nash_equilibrium()
plt.scatter(nash[0], nash[1], color="r", label="Nash Equilibrium")
plt.xlabel("x_i")
plt.ylabel("x_j")
plt.legend()
plt.grid()  # add grid
plt.axis([-0.5, 0.5, -0.5, 0.5])  # adjust axis limits
plt.savefig("plot.png")
# plt.show()
