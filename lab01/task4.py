def calculate_statistics(*args):
    if len(args) == 0:
        return {"count": len(args), "sum": sum(args), "average": None,
                "min": None, "max": None}
    return {"count": len(args), "sum": sum(args), "average": sum(args) / len(args),
            "min": min(args), "max": max(args)}


print(calculate_statistics(3, 4, 5))
print(calculate_statistics(11))
print(calculate_statistics())
