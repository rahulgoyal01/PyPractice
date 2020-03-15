def div_by(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print("Please divide by something greater than Zero.")

print(div_by(2))
print(div_by(14))
print(div_by(0))
print(div_by(1))
