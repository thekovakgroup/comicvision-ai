# Milestone 05 — Cluster Interpretation

## Method

K-means grouped 16 training covers using 12 features per cover: mean red,
green, and blue in each of four image quadrants. Four holdout covers were
reserved for later evaluation. PCA projected the training features onto
two axes for visualization, capturing 62.4% of feature variation.

## Results

| Clusters | Training silhouette | Group sizes |
|---|---:|---|
| 2 | 0.249 | 11, 5 |
| 3 | 0.260 | 5, 6, 5 |
| 4 | 0.275 | 1, 5, 6, 4 |
| 5 | 0.285 | 6, 4, 4, 1, 1 |

Three clusters were retained for interpretation because each group
contained several covers to compare. Five clusters had the highest
silhouette score among the tested settings and produced two groups
containing one cover each.

- **Cluster 0:** Higher average RGB values in the lower half.
- **Cluster 1:** Highest average RGB values in the top right within
  the cluster. This group includes CV0003 and its three nearest
  quadrant RGB matches from Milestone 04.
- **Cluster 2:** Generally lower average RGB values in the lower half.

## Limitations and verification

The three-cluster silhouette score of 0.260 suggests modest separation
on the training set. The groups describe coarse color placement in this
small pilot. Photo lighting may also affect the RGB averages.

A fresh kernel run reproduced the group sizes, silhouette score, and
PCA variance. All 30 repository tests passed.