
import numpy as np
import pypoman
from scipy.optimize import line_search, linprog


class SAFW:
    def __init__(self, A, b, eta, x_prime):
        m, d = A.shape
        self.m = m
        self.d = d
        self.A = A
        self.b = b
        self.eta = eta
        self.x_prime = x_prime
    
    
    def ask_constraints(self, x):
        y = self.A @ x - self.b + np.random.normal(0, self.eta, self.m)
        return y
    
    def f(self, x):
        y = 0.5*np.linalg.norm(x - self.x_prime)**2
        return y
    
    def e_i(self, i, d):
        l = [0]*(i - 1) + [1] + [0]*(d - i)
        return np.array(l)
        
    def ask_gradient(self, x):
        y = x - self.x_prime
        return y
    
    def run(self, x_0, T, epsilon, delta, tau, N_t, n_t):
        self.trajectroy = [x_0]
        self.x_0 = x_0
        self.T = T
        self.epsilon = epsilon
        self.delta = delta
        self.tau = tau
        self.X = np.zeros([N_t, d])
        self.Y = np.zeros([N_t, m])
        self.x_t = np.zeros([d,n_t+1])
        self.x_t[:,0] = np.ones(d)*0.1
        self.x_t[:,0] = x_0
        self.atoms = [x_0]
        for i in range(t):

            x = self.trajectroy[-1]
            for j in range(d):
                x_measure_1 = x + self.e_i(j+1, d)*omega_0
                x_measure_2 = x - self.e_i(j+1, d)*omega_0
                for k in range(n_t//(2*d)):
                    self.X[i*n_t + j*2*(n_t//(2*d)) + k, :] = x_measure_1
                    self.Y[i*n_t + j*2*(n_t//(2*d)) + k, :] = self.ask_constraints(x_measure_1)

                    self.X[i*n_t + j*2*(n_t//(2*d)) + (n_t//(2*d)) + k, :] = x_measure_2
                    self.Y[i*n_t + j*2*(n_t//(2*d)) + (n_t//(2*d)) + k, :] = self.ask_constraints(x_measure_2) 

            X_bar = np.concatenate([self.X[0:(i + 1)*n_t,:], np.array([-1]*((i + 1)*n_t)).reshape(-1,1)], axis = 1)
            Y_bar = self.Y[0:(i + 1)*n_t,:] + tau
            beta_t = np.linalg.inv(X_bar.T @ X_bar) @ X_bar.T @ Y_bar
            A_hat = beta_t[0:d, :]
            b_hat = beta_t[-1, :]

            vertices = np.array(pypoman.compute_polytope_vertices(A_hat.T, b_hat))
            bounds2 = [[0, 1]]*vertices.shape[0]
            weights = linprog(np.array([1]*vertices.shape[0]), \
                              A_eq = np.concatenate([vertices.T, np.array([1]*vertices.shape[0]).reshape(1,vertices.shape[0])], axis = 0),\
                              b_eq = np.append(x - tau, 1) , bounds=bounds2).x
            atoms_with_positive_wight = vertices[weights > 0, :]

            for j in range(len(atoms_with_positive_wight) + 1):
                bounds2 = [[0, 1]]*vertices.shape[0]
                weights = linprog(np.array([1]*vertices.shape[0]), \
                              A_eq = np.concatenate([vertices.T, np.array([1]*vertices.shape[0]).reshape(1,vertices.shape[0])], axis = 0),\
                              b_eq = np.append(x - tau, 1) , bounds=bounds2).x
                atoms_with_positive_wight = vertices[weights > 0, :]
                grad = self.ask_gradient(x)
                res = linprog(grad, A_ub=A_hat.T, b_ub=b_hat )
                d_FW = res.x - x
                inner_product = atoms_with_positive_wight @ grad
                argmax = np.argmax(inner_product)
                v_t = atoms_with_positive_wight[argmax, :] 
                bounds2 = [[0, 1]]*atoms_with_positive_wight.shape[0]
                weights = linprog(np.array([1]*atoms_with_positive_wight.shape[0]), \
                                  A_eq = np.concatenate([atoms_with_positive_wight.T, \
                                  np.array([1]*atoms_with_positive_wight.shape[0]).reshape(1,atoms_with_positive_wight.shape[0])], axis = 0),
                                  b_eq = np.append(x - tau, 1), bounds=bounds2).x
                alpha_v_t = weights[argmax]
                d_A = x - v_t
                duality_gap = np.dot(-grad, d_FW)
                step_away = np.dot(-grad, d_A)

                if duality_gap <= self.epsilon:
                    break
                else:
                    if duality_gap >= step_away:
                        d_t = d_FW
                        gamma_max = 1 
                    else:
                        d_t = d_A
                        gamma_max = alpha_v_t/(1 - alpha_v_t)
                gamma_t = line_search(self.f, self.ask_gradient, x, d_t, amax = gamma_max)[0]
                if gamma_t == None:
                    gamma_t = gamma_max
                x_next = x + gamma_t*d_t
                self.trajectroy.append(x_next)

                x = x_next
                bounds2 = [[0, 1]]*vertices.shape[0]
                vertices = np.array(pypoman.compute_polytope_vertices(A_hat.T, b_hat))
                weights = linprog(np.array([1]*vertices.shape[0]), \
                                  A_eq = np.concatenate([vertices.T, np.array([1]*vertices.shape[0]).reshape(1,vertices.shape[0])], axis = 0),
                                  b_eq = np.append(x - tau, 1) , bounds=bounds2).x
                atoms_with_positive_wight = vertices[weights > 0, :]
                