# --------------
# Code starts here

import numpy as np

# Code starts here

# Adjacency matrix
adj_mat = np.array([[0,0,0,0,0,0,1/3,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                   [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                   [0,0,1/2,1/3,0,0,1/3,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2], [0,0,0,0,1/3,1,1/3,0]])

# Compute eigenvalues and eigencevectors
eigenvalues, eigencevectors = np.linalg.eig(adj_mat)
# print(eigenvalues)  
# print(eigencevectors) 
# Eigen vector corresponding to 1
a = abs(eigencevectors[:, 0])
print(a)
eigen_1 = abs(eigencevectors[:,0])/np.linalg.norm(eigencevectors[:,0], 1)

print(eigen_1) 

# most important page

# page = np.where(eigen_1 == max(eigen_1))
# print(page.index(eigen_1)) 
# for value in page: 
#     print(page)  
#  page.dtype 
# eigen_1.dtype

page = 8
print(page) 




# Code ends here


# --------------
# Code starts here

# Initialize stationary vector I
init_I = np.array([1,0,0,0,0,0,0,0])


# Perform iterations for power method
for i in range(10): 
    init_I = np.dot(adj_mat, init_I)
    init_I_norm = np.linalg.norm(init_I, 1) 
    init_I = init_I/init_I_norm 
    
power_page = np.where(np.max(init_I) == init_I)[0][0] + 1
print(power_page) 







# def power_iteration(A, num_simulations):
#     # Ideally choose a random vector
#     # To decrease the chance that our vector
#     # Is orthogonal to the eigenvector
#     b_k = np.random.rand(A.shape[1]) 
#     # print(b_k)
#     for _ in range(num_simulations):
#         # calculate the matrix-by-vector product Ab
        
#         b_k1 = np.dot(A, b_k)

#         # calculate the norm
#         b_k1_norm = np.linalg.norm(b_k1)

#         # re normalize the vector
#         b_k = b_k1 / b_k1_norm

    
#     # return b_k

#     print(b_k)

#     power_page = np.where(np.max(b_k) == b_k)[0][0] + 1
#     print(power_page) 

# power_iteration(adj_mat, 10)




# # Code ends here


# --------------
# Code starts here


# New Adjancency matrix


new_adj_mat = np.array([[0,0,0,0,0,0,0,0],
                   [1/2,0,1/2,1/3,0,0,0,0],
                  [1/2,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0],
                   [0,0,1/2,1/3,0,0,1/2,0],
                   [0,0,0,1/3,1/3,0,0,1/2],
                   [0,0,0,0,1/3,0,0,1/2],
                   [0,0,0,0,1/3,1,1/2,0]])

# Initialize stationary vector I
new_init_I = np.array([1,0,0,0,0,0,0,0]) 
# Perform iterations for power method
for _ in range(10):
    new_init_I = np.dot(new_adj_mat, new_init_I)
    new_init_I /= np.linalg.norm(new_init_I, 1)



# Code ends here


# --------------
# Alpha value
alpha = 0.85
new_adj_mat = np.array([[0,0,0,0,0,0,0,0],[1/2,0,1/2,1/3,0,0,0,0],
                    [1/2,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1/2,1/3,0,0,1/2,0],
                    [0,0,0,1/3,1/3,0,0,1/2],[0,0,0,0,1/3,0,0,1/2],[0,0,0,0,1/3,1,1/2,0]])

# Code starts here

# Modified adjancency matrix
G = (0.85*new_adj_mat) + (((np.ones(new_adj_mat.shape)) - 0.85) * (1/len(new_adj_mat))*np.ones(new_adj_mat.shape)) 
print(G) 

# Initialize stationary vector I
final_init_I = np.array([1,0,0,0,0,0,0,0])

# Perform iterations for power method
for _ in range(1000):
    final_init_I = np.dot(new_adj_mat, final_init_I) 
    final_init_I /= np.linalg.norm(final_init_I, 1)
    print(final_init_I) 




# Code ends here


