from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(
        ..., min_length=3, max_length=10, description="station_id")
    name: str = Field(
        ..., min_length=1, max_length=50, description="name")
    crew_size: int = Field(
        ..., ge=1, le=20, description="crew_size")
    power_level: float = Field(
        ..., ge=0.0, le=100.0, description="power_level")
    oxygen_level: float = Field(
        ..., ge=0.0, le=100.0, description="oxygen_level")
    last_maintenance: datetime = Field(
        ..., description="last_maintenance")
    is_operational: bool = Field(
        default=True, description="is_operational")
    notes: Optional[str] = Field(
        default=None, max_length=200, description="notes")

    def __str__(self) -> str:
        status = "Operational" if self.is_operational else "Non-operational"
        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: {status}"
        )


def main() -> None:
    try:
        print("Space Station Data Validation")
        print("=" * 40)

        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2024-01-01T10:00:00")
        )

        print("Valid station created:")
        print(station)
    except Exception as e:
        print(e)
    print("\n" + "=" * 40)
    try:
        SpaceStation(
            station_id="BAD001",
            name="Bad Station",
            crew_size=50,
            power_level=90,
            oxygen_level=90,
            last_maintenance=datetime.fromisoformat("2024-01-01")
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
