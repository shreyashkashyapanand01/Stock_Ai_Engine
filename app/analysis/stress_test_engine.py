def run_stress_test(metrics):
    total_value = metrics.get("totalValue", 0)

    market_crash = total_value * 0.85
    interest_rate = total_value * 0.95

    return {
        "marketCrashImpact": f"{round(((market_crash - total_value)/total_value)*100, 2)}%",
        "interestRateImpact": f"{round(((interest_rate - total_value)/total_value)*100, 2)}%"
    }