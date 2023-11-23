# Multi Line Linear Regression

![image](https://github.com/atharvagasheTAMU/MultiLineLinearRegression/assets/146036006/35c64381-93d8-4044-8592-e5b271c52ca0)

## Description of Problem:
The project tackles the challenge of fitting lines to data - a common problem in statistics and machine learning. Imagine having a scatter plot of points, and you want to draw a line that best captures the trend of these points. This isn't always straightforward, especially when the data has multiple trends. The goal is to draw as few lines as possible that still describe the data accurately, without overcomplicating the model.

## Algorithm:
The solution unfolds through a dynamic programming algorithm that meticulously computes the optimal arrangement of line segments to fit a given set of data points. To initiate the process, the algorithm calculates prefix sums of the x and y coordinates, their products, and their squares. These prefix sums serve as the foundation for efficiently computing the sum of squared errors for any segment of points without reiterating through the entire dataset.

Within the CALCULATE_COST function, the algorithm employs these prefix sums to determine the coefficients of the best-fit line and the corresponding error for any segment between points i and j. This is where the algorithm's efficiency shines — by reusing the calculated prefix sums, the computation of the line's parameters and error is significantly expedited.

The heart of the algorithm lies in the MULTI_LINE_FIT function. It initializes two-dimensional arrays to store the optimal partition points and the minimum cost associated with each segment. Starting from the first data point, the algorithm iteratively explores every possible partition to calculate the cost of fitting lines up to the current point. It does this by adding the cost of the new line segment to the optimal cost computed for the previous segment. By comparing the costs of different partitions, it selects the minimum cost option, which includes the penalty for adding a new line.

This iterative process continues, building upon the previously computed solutions, and stores the optimal cost and the cut points in the arrays. By induction, the algorithm ensures that the optimal solution for each point considers all possible previous solutions, leading to a globally optimized configuration of line segments.

The conclusion of the algorithm provides the minimum total cost to fit the data with multiple line segments, as well as the cut points for where each line segment begins and ends. This result exemplifies dynamic programming's capability to transform a potentially onerous computational task into a tractable one, yielding optimal solutions efficiently and elegantly.

## Conclusion:
The result is a balanced model that captures the essential patterns in the data with just the right number of lines - not too few that we miss out on important trends, and not too many that the model becomes too complex. This technique not only provides a clearer understanding of the data but also does so in an efficient and scalable way. Whether for economic forecasting, scientific measurements, or any other data-intensive analysis, this approach offers a smart way to make sense of complex patterns.






