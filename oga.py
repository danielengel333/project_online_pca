import numpy as np
import numpy.linalg as nl
import scipy.linalg as sl


def regret(current_regret_sum, x_t, ):
    pass

def payoff(w_t, x_t):
    return np.power(w_t.dot(x_t), 2)

def oga():
    pass

def adv_next():
    pass

def oga_next(w_t, nu, x_t):
    nom = w_t + nu * x_t * x_t.dot(w_t)
    dom = np.linalg.norm(nom)
    return nom / dom



def main():
    d = 10
    T = 10000

    adversary_vectors = [np.random.rand(d) for _ in range(T)]
    algorithm_vectors = []

    nu = 10

    w_1 = np.random.normal(size=d)
    w_1 = w_1 / np.linalg.norm(w_1)

    current_payoff_sum = 0
    current_adversary_matrix = np.zeros((d,d))

    w_t = w_1
    x_t = np.random.normal(size=d)
    for i in range(T):
        #x_t = np.random.normal(size=d)
        p = payoff(w_t, x_t)
        current_payoff_sum += p
        current_adversary_matrix += np.outer(x_t, x_t)
        regret = nl.eig(current_adversary_matrix)[0][0] - current_payoff_sum
        average_regret = regret / T
        print(average_regret)

        w_t = oga_next(w_t, nu, x_t)


if __name__ == '__main__':
    main()