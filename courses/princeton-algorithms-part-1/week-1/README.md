# Week - 1

## Dynamic connectivity problem - Union-Find

Given a set of N objects
1. `union()`: Connects two objects
2. `find()/connected()`: Is there a path connecting two objects?

### Applications of the algorithm

This algorithm can be used for manipulating objects like
- Pixels in a digital photo
- Computers in a network
- Friends in a social network
- Transistors in a computer chip etc.

### Modelling the connections

We assume that **is connected to** is an equivalence relation
- **Reflexive:** : `p` is connected to `p`.
- **Symmetric** : If `p` is connected to `q`, then `q` is connected to `p`.
- **Transitive** : If `p` is connected to `q` and `q` is connected to `r`, then `p` is connected to `r`.

### Union-find API
**Goal :** Design efficient data structure for union find
- Number of N can be huge.
- Number of operations can be huge.
- Find queries and union commands can be intermixed.

``` java
interface UnionFind{

    /** Adds connection between p and q
    */
    void union(int p, int q);

    /** Checks if there is a connection between p and q.
    */
    boolean isConnected(int p, int q);
}
```

### Quick-find (eager approach)

#### Data structure
- Integer array id[] of size N.
- We assume that `p` and `q` are connected if they have the same id.

#### Find operation.
Check if `id[p] == id[q]`.

#### Union operation
To merge components containing `p` and `q`, change all entries whose id equals `id[p]` to `id[q]`.

#### Complexity
- **Find:** O(1)
- **Union:** O(N)

