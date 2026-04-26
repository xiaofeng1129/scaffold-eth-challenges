def select_strategy(regime):
    if regime == "TREND":
        return "trend"
    if regime == "RANGE":
        return "mean"
    return "breakout"
