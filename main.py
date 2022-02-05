import os
import itertools
import networkx as nx
import numpy as np


def create_dir(folder):
    if not os.path.isdir('./output'):
        os.mkdir('./output')
    if not os.path.isdir('./output/' + folder):
        os.mkdir('./output/' + folder)
    else:
        print("Folder already exists. Hence, continuing with the existing folder.")
    return


def ensure_output_folder(folder):
    if os.path.isdir('./output/' + folder):
        return
    create_dir(folder)


def create_file(folder, file_n):
    ensure_output_folder(folder)
    return open('./output/' + folder + '/' + file_n, "w")


if __name__ == '__main__':
    nodes = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    folder_file_cnt_max = 100
    for node in nodes:
        folder_name = str(node) + '_nodes'

        g = nx.erdos_renyi_graph(node, 0.4)
        nx.draw(g, with_labels=True)
        A = nx.adjacency_matrix(g)
        adj_mat = A.todense()
        identity_mat = np.identity(node)

        i = 1
        for m in itertools.permutations(identity_mat):
            if i > folder_file_cnt_max:
                break

            # create isomorphic graph - P * A * P.T
            res = np.matmul(np.matmul(m, adj_mat), np.matrix(m).T)

            # convert to string
            res = np.char.mod('%d', res)
            res = [' '.join(i) for i in res]
            res = '\n'.join(res)

            # write to file
            file_name = str(i) + '.txt'
            file = create_file(folder_name, file_name)
            file.write(res)
            file.close()

            i = i + 1
