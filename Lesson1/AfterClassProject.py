def squares(start, end):
    sv = [e**2 for e in range(start, end + 1)]
    even = [f for f in sv if f % 2 == 0]

    odd = [f for f in sv if f % 2 != 0]
    
    print(f"Range: {start} to {end} ---")
    print(f"All square values: {sv}")
    print(f"Odd square values: {odd}")
    print(f"Even square values: {even}")

squares(2, 6)
squares(1, 4)