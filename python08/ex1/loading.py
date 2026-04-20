import importlib
from typing import Optional
from types import ModuleType


def package(name: str) -> Optional[ModuleType]:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version})")
        return module
    except ImportError:
        print(f"[MISSING] {name}")
        return None


def analysis(pd: ModuleType, np: ModuleType, plt: ModuleType) -> None:
    print("\nAnalyzing Matrix data...")

    data = np.random.normal(loc=50, scale=15, size=1000)

    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame(data, columns=["values"])
    df["moving_avg"] = df["values"].rolling(window=50).mean()

    print("Generating visualization...")
    plt.figure()
    plt.plot(df["values"], label="Raw Data")
    plt.plot(df["moving_avg"], label="Moving Average")
    plt.legend()
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

    pandas = package("pandas")
    numpy = package("numpy")
    matplotlib = package("matplotlib")
    plt = None
    if matplotlib is not None:
        matplotlib.use("Agg")
        plt = importlib.import_module("matplotlib.pyplot")
    if not (pandas and numpy and plt):
        print("\nSome dependencies are missing.")
        print("Install them using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        return

    analysis(pandas, numpy, plt)


if __name__ == "__main__":
    main()
