import numpy as np
from scipy.sparse import csr_matrix

class MatrixCalculator:
    def calculate(self, operation, matrix_a, matrix_b=None):
        try:
            if operation == "add":
                return matrix_a + matrix_b
            elif operation == "multiply":
                return np.dot(matrix_a, matrix_b)
            elif operation == "add_sparse":
                if isinstance(matrix_a, csr_matrix) and isinstance(matrix_b, csr_matrix):
                    return matrix_a + matrix_b
                else:
                    raise ValueError("Both matrices must be sparse.")
            else:
                raise ValueError(f"Unknown operation '{operation}'")
        except Exception as e:
            return str(e)



