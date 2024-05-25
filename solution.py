def solution(A):
    east_cars = 0
    passing_cars = 0

    for car in A:
        if car == 0:  # 東向きの車
            east_cars += 1
        else:  # 西向きの車
            passing_cars += east_cars

        if passing_cars > 1_000_000_000:
            return -1
    return passing_cars