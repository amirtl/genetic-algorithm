# genetic-algorithm
solving TSP with genetic algorithm
# explanation
- in parameters.txt there is an analysis for each parameter. 
- My analysis is also for hte bayg29. I ran the code for 1000 times and made average and best case for each parameter.
- you can change the cities if you like. but notice you have to change "size" too.
# executation
run the code with python 2.
# algorithm
1. We consider every path as gene like this : [0,1,3,2,0]
2. each gene starts from city 0 and come back to it at the end of the cycle. and between the two zeros we have every number from 1 to 20(the number of the cities.).
3. first we make 40 Genes randomly and sort them by their fitness and select the best 50% of them.
4. in each generation we make a mutation in every gene.
5. this is how the mutation work: it takes two random number between 1 and 20. if the numbers are different it swap the to indexes in the gene so that a new gene creates.
6. we will add each new gene to our population.
7. after the mutations we take the best N% genes sorted with their fitnesses.
8. we stop the algorithm when the best fitness doesn't change for 1000 times.
