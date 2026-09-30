from statsmodels.stats.proportion import proportions_ztest

# Experiment data
control_users = 10000
control_conversions = 1200

treatment_users = 10000
treatment_conversions = 1320

# Calculate conversion rates
control_rate = control_conversions / control_users
treatment_rate = treatment_conversions / treatment_users

# Calculate uplift
absolute_uplift = treatment_rate - control_rate
relative_uplift = (treatment_rate / control_rate) - 1

# Run two-proportion z-test
conversions = [treatment_conversions, control_conversions]
users = [treatment_users, control_users]

z_stat, p_value = proportions_ztest(conversions, users)

# Display results
print(f"Control conversion rate: {control_rate:.2%}")
print(f"Treatment conversion rate: {treatment_rate:.2%}")
print(f"Absolute uplift: {absolute_uplift:.2%}")
print(f"Relative uplift: {relative_uplift:.2%}")
print(f"P-value: {p_value:.4f}")

# Interpret experiment
if p_value < 0.05:
    print("Result: Statistically significant")
else:
    print("Result: Not statistically significant")
