# Clustering


## types
well-seperated
center-based : calculate enter first, and compare distance from centroid to each group
contiguity-based
conceptual
density-based

## algorithms


## partition-based clustering

heuristic :
k-means : represent by the center of cluster
k-medoids (when full of outliers)

### K-means
partition k groups
compute centroids for k groups
relocate, back to step 2

#### Details
centroids
closeness
converge very fast

pros.
efficient, accept local optimum

cons.
applicable ? 
need to specify k
unable to handle noisy, outliers

variants of k-means

#### Problem with selecting k-means initial points

initial point in diff groups prob at k=10 : 0.00036

size problem
density problem
non-globular problem

sol: use many k and merge

### K-medoid

instead using mean value, we find the actual point closest to mean

not get affect by outliers

## Hierchical clustering

agglomerative clustering
proximity matrix


## Divisive clustering
build minimum spanning tree
cut the longest edge

