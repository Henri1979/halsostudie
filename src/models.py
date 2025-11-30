import numpy as np
from sklearn.linear_model import LinearRegression

class HealthAnalyzer:
    """Analys av hälsodata: sjukdom, bootstrap och regression."""

    def __init__(self, df):
        """Initierar med DataFrame df."""
        self.df = df

    def calculate_disease_proportion(self):
        """Returnerar andel personer med sjukdom."""
        return self.df["disease"].mean()

    def bootstrap_ci(self, column, n_iterations=1000, ci=95):
        """Returnerar bootstrap-konfidensintervall för medelvärde."""
        bootstrap_means = [np.random.choice(self.df[column], size=len(self.df), replace=True).mean()
                           for _ in range(n_iterations)]
        lower = np.percentile(bootstrap_means, (100-ci)/2)
        upper = np.percentile(bootstrap_means, 100-(100-ci)/2)
        return lower, upper

    def linear_regression(self, features, target):
        """Returnerar koefficienter och intercept från linjär regression."""
        X = self.df[features].values
        y = self.df[target].values
        model = LinearRegression().fit(X, y)
        return model.coef_, model.intercept_
