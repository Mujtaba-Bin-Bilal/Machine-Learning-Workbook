15. Polynomial Overfitting
    • Task: Fit polynomial regressions of degree 1–10.
    • Dataset: Noisy sine curve.
    • Hints: Use NumPy polyfit.
    • Expected outcome: Degree 1 underfits, degree 10 overfits.
##the chief task of this problem is to manage the coeffecients of a polynomial so that we are able to closely mimic a function and we do that the same as linear regression except now we hve multiple variables. we achieve the values of multiple coeffecients ai by minimizing the actual and predicted values from the function. the principle is same. take a particular range and in that range mimic as much as possible, not too much as the function will also mimic noise(overfitting)
and not too little as it will not even cover the basic function we are trying to cover(underfitting)

