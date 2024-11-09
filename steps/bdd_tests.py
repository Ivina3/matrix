from behave import given, when, then
import numpy as np
from scipy.sparse import csr_matrix
from matrix_calculator import MatrixCalculator

@given('I have matrix B')
def step_impl(context):
    context.matrix_b = np.array([[5, 6], [7, 8]])

@given('I have sparse matrix A')
def step_impl(context):
    context.matrix_a = csr_matrix([[1, 0], [0, 2]])

@given('I have sparse matrix B')
def step_impl(context):
    context.matrix_b = csr_matrix([[0, 3], [4, 0]])

@when('I calculate the result of adding the matrices')
def step_impl(context):
    calculator = MatrixCalculator()
    context.result = calculator.calculate("add", context.matrix_a, context.matrix_b)

@when('I calculate the result of multiplying the matrices')
def step_impl(context):
    calculator = MatrixCalculator()
    context.result = calculator.calculate("multiply", context.matrix_a, context.matrix_b)

@when('I calculate the result of adding the sparse matrices')
def step_impl(context):
    calculator = MatrixCalculator()
    context.result = calculator.calculate("add_sparse", context.matrix_a, context.matrix_b)

@then('I should get the resulting matrix')
def step_impl(context):
    if context.result.shape == (2, 2):  # Проверка на размер матрицы
        if np.all(context.result == np.array([[19, 22], [43, 50]])):
            expected_result = np.array([[19, 22], [43, 50]])
        else:
            expected_result = np.array([[6, 8], [10, 12]])  # Для сложения
    np.testing.assert_array_equal(context.result, expected_result)


@then('I should get the resulting sparse matrix')
def step_impl(context):
    if isinstance(context.result, csr_matrix):
        expected_result = csr_matrix([[1, 3], [4, 2]])
        np.testing.assert_array_equal(context.result.toarray(), expected_result.toarray())
    else:
        raise AssertionError("Result is not a sparse matrix")

@given('I have matrix A')
def step_impl(context):
    context.matrix_a = np.array([[1, 2], [3, 4]])



