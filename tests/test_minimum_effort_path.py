from graphs.minimum_effort_path import *


def test_will_return_min_effort_path_for_first_example():
    # Arrange
    heights = [[1,2,2],[3,8,2],[5,3,5]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 2

def test_will_return_min_effort_for_second_example():
    # Arrange
    heights = [[1,2,3],[3,8,4],[5,3,5]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 1

def test_will_return_min_effort_for_third_example():
    # Arrange
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

    # Act
    answer = min_effort_path(heights)
    
    # Assert
    assert answer == 0

def test_will_return_zero_for_empty_graph():
    # Arrange
    heights = None

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 0


def test_will_return_min_effort_for_rectangular_grid():
    # Arrange
    heights = [[1,2,1,1,1,1],[1,2,1,2,1,2],[1,2,1,2,1,3],[1,2,1,2,1,3],[1,1,1,2,1,2]]

    # Act
    answer = min_effort_path(heights)
    
    # Assert
    assert answer == 1