import sys

if __name__ == "__main__":
    try:
        print("=== Player Score Analytics ===")
        if len(sys.argv) > 1:
            arguments: list[int] = []
            for arg in sys.argv[1:]:
                arguments += [int(arg)]
            lenght: int = len(arguments)
            print(f"Scores processed: {arguments}")
            print(f"Total players: {lenght}")
            print(f"Total score: {sum(arguments)}")
            print(f"Average score: {sum(arguments) / lenght}")
            print(f"High score: {max(arguments)}")
            print(f"Low score: {min(arguments)}")
            print(f"Score range: {max(arguments) - min(arguments)}\n")
        else:
            print("No scores provided. Usage: python3 ft_score_analytics.py",
                  "<score1> <score2> ...")
    except Exception as e:
        print(e)
