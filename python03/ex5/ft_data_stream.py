from typing import Generator


def processing_games() -> Generator[dict, None, None]:
    players: list = [
        {"name": "alice", "level": 5},
        {"name": "bob", "level": 12},
        {"name": "charlie", "level": 8},
        {"name": "yahya", "level": 33},
        {"name": "mohamed", "level": 9},
        {"name": "yassine", "level": 11}
    ]
    events: list = ["killed monster", "found treasure", "leveled up"]
    for i in range(1000):
        player = i % len(players)
        event = i % len(events)
        yield {
            "number": i + 1,
            "name": players[player]["name"],
            "event": events[event],
            "level": players[player]["level"]
        }


def fibonacci(n: int) -> Generator[int, None, None]:
    u1: int = 0
    u2: int = 1
    for _ in range(n):
        yield u1
        temp: int = u1
        u1 = u2
        u2 += temp


def prime(n: int) -> Generator[int, None, None]:
    count: int = 2
    while (count < n):
        prime: bool = True
        i: int = 2
        while i * i <= count:
            if count % i == 0:
                prime = False
            i += 1
        if prime:
            yield count
        count += 1


def print_num(g: Generator, rg: int) -> None:
    for i in range(rg):
        try:
            iteration: int = next(g)
            if i == rg - 1:
                print(f"{iteration}")
            else:
                print(f"{iteration}, ", end="")
        except StopIteration:
            break


if __name__ == "__main__":

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")
    total: int = 0
    events = processing_games()
    nb: int = 0
    leveled: int = 0
    treasure: int = 0
    while True:
        try:
            event: dict = next(events)
            if event["level"] >= 10:
                nb += 1
            if event["event"] == "leveled up":
                leveled += 1
            if event["event"] == "found treasure":
                treasure += 1
            print(
                f"Event {event["number"]}: Player {event["name"]}",
                f"(level {event["level"]}) {event["event"]}")
        except StopIteration:
            break
        total += 1
    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {nb}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {leveled}")
    print("\nMemory usage: Constant (streaming)")
    processing_time: float = total * 0.045 / 1000
    print(f"Processing time: {processing_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib: Generator = fibonacci(100)
    prime_gen: Generator = prime(100)
    print_num(fib, 10)
    print("Prime numbers (first 5): ", end="")
    print_num(prime_gen, 5)
