def pythagorean_triplets(limit):
    side1 = 1
    side2 = 1
    side3 = 1
    for i in range(side1, limit):
        for j in range(side2, limit):
            for k in range(side3, limit):
                if (i * i) + (j * j) == k * k:
                    print(f"s1: {i}, s2: {j}, s3: {k}")


pythagorean_triplets(500)
