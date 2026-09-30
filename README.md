# 🧪 A/B Testing Analysis with Python

A practical experimentation project demonstrating how A/B test results can be analysed and translated into a business decision.

## 🎯 Business Question

Does a new product experience significantly improve conversion compared with the existing experience?

## 📊 Experiment

| Group | Users | Conversions | Conversion Rate |
|---|---:|---:|---:|
| Control | 10,000 | 1,200 | 12.0% |
| Treatment | 10,000 | 1,320 | 13.2% |

**Absolute uplift:** +1.2 percentage points  
**Relative uplift:** +10.0%

## 🔬 Method

The analysis uses a two-proportion statistical test to determine whether the observed difference between Control and Treatment is statistically significant.

The project evaluates:

- Control vs Treatment conversion
- Absolute and relative uplift
- Statistical significance
- Confidence intervals
- Business interpretation

## 🐍 Python

```python
from statsmodels.stats.proportion import proportions_ztest

conversions = [1320, 1200]
users = [10000, 10000]

z_stat, p_value = proportions_ztest(conversions, users)

print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Statistically significant result")
else:
    print("Result is not statistically significant")
