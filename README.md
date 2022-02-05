# Random-Isomorphic-Graph-Generator

In this project, random Isomorphic graph generation involves two steps:
1. Genearate Random Graphs.
2. Create Isomorphic Graphs (IG) from it.


## Random Graph Generation:
Random graphs are generated using `Erdős-Rényi- G(n, p)` random graph model, where n is the number of nodes of a graph and p is the probability of edge occurrence between two graphs.
Here, I used p = 0.40 so as to stay in between sparse and dense graphs. This value will produce a graph with enough amount of edges for isomorphic graph analysis.
The users of this repo can alter this value in case if they need to increase or decrease the graph density.

The projects converts a graph to its adjacency matrix which is then passed to the step-2.

## Isomorphic Graphs Generation:
Once the step-1 is complete, IGs (Isomorphic Graphs) are produced by the following formula:

  `IG(A) = P * A * P.T;`
  
 where A = Adjacency matrix of a graph G , P = Permutation matrix and P.T is the transpose of the Permutation matrix (P).
 
 By repeating the above formula with different P matrices, one can generate different IGs. The result of the above equation is an adjacency matrix of an IG and it will be stored in a file under the output folder.
 
 ## Input and Output:
 
 **Input:**
 
 1 -> By default, the project will generate 100 IGs for one graph from every group with |V|= [5, 10, 20, 30, ... , 80, 90, 100].
 
 2 -> p=0.40
 
 Altering the above inputs will have effect on the output.
 
 **Output:**
 
 _Folder structure:_

![Screenshot from 2022-02-05 13-40-15](https://user-images.githubusercontent.com/29046579/152634150-63ecf007-2618-4068-b10d-8fa636a46755.png)

 Every .txt file from the above folder structure contains the adjacency matrix of a graph which is essentially isomorphic to the rest of the adjacency matrix under the same folder.
      
 
