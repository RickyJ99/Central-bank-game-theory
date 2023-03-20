import numpy as np

# Define the parameters
beta1j = 2.00
beta2j = 1.00
beta1i = 2.00
beta2i = 1.50
T = 0.25
Nj = 0.5
Ni = 0.00
alpha = 0.60
steps = 4

# weigh
w_j = beta1j + beta2j + alpha**2
w_i = beta1i + beta2i + (1 - alpha) ** 2


# Define the best reply functions
def x_i_best_reply(x_j):
    q_j = beta1j * T + beta2j * Nj
    return float(q_j * w_i + (1 - alpha) * alpha * q_j) / (w_i * w_j - 1)


def x_j_best_reply(x_i):
    q_i = beta1i * T + beta2i * Ni
    return float(q_i * w_j + (1 - alpha) * alpha * q_i) / (w_i * w_j - 1)


# Define the rationalizability sets
# Initialize the rationalizability sets
rational_i = np.array([-0.5])
rational_j = np.array([-0.5])


# Update the rationalizability sets using the best reply functions

# Update the rationalizability sets using the best reply functions
# step 1
rational_i = np.append(rational_i, x_i_best_reply(rational_j[0]))
rational_j = np.append(rational_j, x_j_best_reply(rational_i[0]))

# step 2
rational_i = np.append(rational_i, x_i_best_reply(rational_j[1]))
rational_j = np.append(rational_j, x_j_best_reply(rational_i[1]))

# Print the updated rationalizability sets
print("Rationalizability set of agent i after 0 step:")
print(rational_i)
print("\nRationalizability set of agent j after 0 step:")
print(rational_j)
