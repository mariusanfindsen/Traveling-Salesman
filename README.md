# Traveling Salesman 
The traveling salesman problem is about finding the shortest possible route that visits each city exactly once and 
returns to the city of origin. A bruteforce approach with running a exhaustive search on all possible routes is not a 
solution because the search tree explodes exponentially as number of cities increase. This repo has a Genetic Algorithm approach. 
This approach reduce the search tree, but cant guarantee the best solution.

## CSV file format
|  &nbsp;   | Barcelona | Belgrade |  Berlin | Brussels | Bucharest | Budapest |
|:---------:|:---------:|:--------:|:-------:|:--------:|:---------:|:--------:|
| Barcelona |     0     |  1528.13 | 1497.61 |  1062.89 |  1968.42  |  1498.79 |
|  Belgrade |  1528.13  |     0    |  999.25 |  1372.59 |   447.34  |  316.41  |
|   Berlin  |  1497.61  |  999.25  |    0    |  651.62  |  1293.40  |  1293.40 |
|  Brussels |  1062.89  |  1372.59 |  651.62 |     0    |  1769.69  |  1131.52 |
| Bucharest |  1968.42  |  447.34  | 1293.40 |  1769.69 |     0     |  639.77  |
|  Budapest |  1498.79  |  316.41  | 1293.40 |  1131.52 |   639.77  |     0    |

