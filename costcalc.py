"""Fabric Cost Calculator - works out the cost of one stitched piece."""


def fabric_cost(metres, rate_per_metre):
    """Cost of the fabric used for one piece."""
    return metres * rate_per_metre


def piece_cost(metres, rate_per_metre, stitching, overhead):
    """Total cost of one piece."""
    base = fabric_cost(metres, rate_per_metre) + stitching + overhead
    final_price = round(base * 0.90, 2)  # 10% wholesale discount
    return final_price


if __name__ == "__main__":
    metres = float(input("Fabric used (metres): "))
    rate = float(input("Rate per metre (Rs): "))
    stitching = float(input("Stitching charge (Rs): "))
    overhead = float(input("Overhead (Rs): "))
    print(f"Cost per piece: Rs {piece_cost(metres, rate, stitching, overhead):.2f}")
