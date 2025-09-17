this is the 8th problem in the machine learning series.
Implement Loss Functions
    • Task: Implement MAE and MSE.
    • Dataset: Small arrays: y_true=[3,5,7], y_pred=[2.5,5.5,6].
    • Hints: MAE = avg(|y-ŷ|), MSE = avg((y-ŷ)^2).
    • Expected outcome: Correct values (MAE=0.67, MSE=0.5 approx).
there are two scenarios where you use ine or3 the other
:
1. where you use the mean absolute error.
2. where you use the mean square error.

1) Intuition (quick, sharp)

MAE (Mean Absolute Error): average distance between true and predicted. Think: “how many metres off, on average?” Units = same as target.

MSE (Mean Squared Error): average squared distance. Think: “big mistakes hurt more” — squaring amplifies large errors. Units = (target unit)².

When to use which:

Use MAE if you want a robust, interpretable error (less sensitive to outliers).

Use MSE if you want smoother math (differentiable everywhere) and to penalize large errors (common in regression training).
