if __name__ == "__main__":
    # 0 arguments → default triangle
    t1 = Triangle()
    print("t1 (default):", t1)

    # 1 argument → equilateral triangle
    t2 = Triangle(5)
    print("t2 (equilateral):", t2)

    # 2 arguments → isosceles triangle
    t3 = Triangle(4, 7)
    print("t3 (isosceles):", t3)

    # 3 arguments → scalene triangle
    t4 = Triangle(3, 4, 5)
    print("t4 (scalene):", t4)

    # Clone → copy of t4
    t5 = Triangle(t4)
    print("t5 (clone of t4):", t5)
