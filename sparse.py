def to_sparse(matrix):
    """Convert a normal 2D matrix into triplet (sparse) form."""
    rows = len(matrix)
    cols = len(matrix[0])

    sparse = [[rows, cols, 0]]      # header row
    count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
                count += 1

    sparse[0][2] = count            # update number of non-zero elements
    return sparse


def display_sparse(sparse):
    """Display the sparse matrix in triplet form."""
    print(f"{'Row':>4} {'Col':>4} {'Value':>6}")
    print("-" * 16)
    for r, c, v in sparse:
        print(f"{r:>4} {c:>4} {v:>6}")


def to_dense(sparse):
    """Rebuild the full matrix from triplet form."""
    rows, cols, _ = sparse[0]
    matrix = [[0] * cols for _ in range(rows)]
    for r, c, v in sparse[1:]:
        matrix[r][c] = v
    return matrix


def transpose(sparse):
    """Transpose a sparse matrix (swap row and column of each triplet)."""
    rows, cols, count = sparse[0]
    result = [[cols, rows, count]]
    terms = [[c, r, v] for r, c, v in sparse[1:]]
    terms.sort(key=lambda t: (t[0], t[1]))   # keep row-major order
    return result + terms


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    print("Enter the matrix elements row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    sparse = to_sparse(matrix)

    print("\nOriginal matrix:")
    for row in matrix:
        print(*row)

    print("\nSparse (triplet) representation:")
    display_sparse(sparse)

    print("\nTranspose in sparse form:")
    display_sparse(transpose(sparse))

    print("\nMatrix rebuilt from sparse form:")
    for row in to_dense(sparse):
        print(*row)

    total = rows * cols
    print(f"\nElements stored (normal): {total}")
    print(f"Elements stored (sparse): {len(sparse) * 3}")


if __name__ == "__main__":
    main()