import subprocess

def upgrade_packages():
    packages = [
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "jupyter",
        "plotly",
        "xgboost",
        "catboost"
    ]

    for package in packages:
        subprocess.check_call(["pip", "install", "--upgrade", package])

if __name__ == "__main__":
    upgrade_packages()
    print("All packages have been upgraded successfully.")
