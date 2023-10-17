# Get the diagonal elements
matrix= [['10', '20', '30'], ['40', '50', '60'], ['70', '80', '90']]
daigs = []
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        if i == j:
            daigs.append(matrix[i][j])

print(f"Given Matrix: {matrix}")
print(f"Diagnoal elements: {daigs}")
            
