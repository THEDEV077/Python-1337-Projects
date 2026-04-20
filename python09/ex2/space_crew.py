from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(
        ..., min_length=3, max_length=10, description="member_id")
    name: str = Field(
        ..., min_length=2, max_length=50, description="name")
    rank: Rank = Field(
        ..., description="rank")
    age: int = Field(
        ..., ge=18, le=80, description="age")
    specialization: str = Field(
        ..., min_length=3, max_length=30, description="specialization")
    years_experience: int = Field(
        ..., ge=0, le=50, description="years_experience")
    is_active: bool = Field(
        default=True, description="is_active")

    def __str__(self) -> str:
        return (
            f"  - {self.name} ({self.rank.value})"
            f" — {self.specialization}"
        )


class SpaceMission(BaseModel):
    mission_id: str = Field(
        ..., min_length=5, max_length=15, description="mission_id")
    mission_name: str = Field(
        ..., min_length=3, max_length=100, description="mission_name")
    destination: str = Field(
        ..., min_length=3, max_length=50, description="destination")
    launch_date: datetime = Field(
        ..., description="launch_date")
    duration_days: int = Field(
        ..., ge=1, le=3650, description="duration_days")
    crew: list[CrewMember] = Field(
        ..., min_length=1, max_length=12, description="crew")
    mission_status: str = Field(
        default="planned", description="mission_status")
    budget_millions: float = Field(
        ..., ge=1.0, le=10000.0, description="budget_millions")

    def __str__(self) -> str:
        crew_lines = "\n".join(str(member) for member in self.crew)
        return (
            f"Mission:     {self.mission_name}\n"
            f"ID:          {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration:    {self.duration_days} days\n"
            f"Budget:      ${self.budget_millions}M\n"
            f"Crew size:   {len(self.crew)}\n"
            f"Crew members:\n{crew_lines}"
        )

    @model_validator(mode="after")
    def validate_mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        senior_ranks = {Rank.commander, Rank.captain}
        if not any(member.rank in senior_ranks for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) / len(self.crew) < 0.5:
                raise ValueError(
                    "Missions longer than 365 days require at least "
                    "50% of the crew to have 5+ years of experience")

        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                f"All crew members must be active. "
                f"Inactive: {', '.join(inactive)}")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 45)

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-09-01T08:00:00"),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=42,
                    specialization="Mission Command",
                    years_experience=18,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=29,
                    specialization="Engineering",
                    years_experience=6,
                ),
            ],
        )

        print("Valid mission created:")
        print(mission)

    except Exception as e:
        print("Unexpected error in valid case:", e)

    print("\n" + "=" * 45)

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Expedition",
            destination="Pluto",
            launch_date=datetime.fromisoformat("2024-10-01T00:00:00"),
            duration_days=50,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM010",
                    name="Bob Rookie",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Science",
                    years_experience=1,
                ),
            ],
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
