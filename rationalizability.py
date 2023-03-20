import numpy as np

# Define the parameters
beta_1_j = 2.00
beta_2_j = 1.00
beta_1_i = 2.00
beta_2_i = 1.50
T = 0.25
N_j = 0.5
N_i = 0.00
alpha = 0.60
steps = 4

# weigh
w_j = beta_1_j + beta_2_j + alpha**2
w_i = beta_1_i + beta_2_i + (1 - alpha) ** 2


# Define the best reply functions
def x_i_best_reply(x_j):
    K = beta_1_i + beta_2_i + ((1 - alpha) ** 2)
    n_i = beta_1_i * T + beta_2_i * N_i
    return (
        (beta_1_i * T + beta_2_i * N_i + alpha * (1 - alpha) * x_j)
        / K
        * np.ones_like(x_j)
    )


def x_j_best_reply(x_i):
    L = beta_1_j + beta_2_j + (alpha**2)
    return (
        (beta_1_j * T + beta_2_j * N_j + alpha * (1 - alpha) * x_i)
        / L
        * np.ones_like(x_i)
    )


# Define the rationalizability sets
# Initialize the rationalizability sets
rational_i = np.array([+0.5])
rational_j = np.array([+0.5])


# Update the rationalizability sets using the best reply functions

# Update the rationalizability sets using the best reply functions
# step 1
n = 10
for count in range(n):
    rational_i = np.append(rational_i, x_i_best_reply(rational_j[count]))
    rational_j = np.append(rational_j, x_j_best_reply(rational_i[count]))

# Print the updated rationalizability sets
print("Rationalizability set of agent i after n step:")
print(rational_i)
print("\nRationalizability set of agent j after n step:")
print(rational_j)
