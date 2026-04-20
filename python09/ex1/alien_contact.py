from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional, Self


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        ..., min_length=5, max_length=15, description="contact_id")
    timestamp: datetime = Field(
        ..., description="timestamp")
    location: str = Field(
        ..., min_length=3, max_length=100, description="location")
    contact_type: ContactType = Field(
        ..., description="contact_type")
    signal_strength: float = Field(
        ..., ge=0.0, le=10.0, description="signal_strength")
    duration_minutes: int = Field(
        ..., ge=1, le=1440, description="duration_minutes")
    witness_count: int = Field(
        ..., ge=1, le=100, description="witness_count")
    message_received: Optional[str] = Field(
        default=None, max_length=500, description="message_received")
    is_verified: bool = Field(default=False, description="is_verified")

    def __str__(self) -> str:
        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type.value}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: '{
                self.message_received if self.message_received else 'None'}'"
        )

    @model_validator(mode="after")
    def validate_business_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")

        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (>7.0) must include a message")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2024-01-01T10:00:00"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print(contact)

    except Exception as e:
        print("Unexpected error in valid case:", e)

    print("\n" + "=" * 40)

    try:
        AlienContact(
            contact_id="AC_XX_2024_001",
            timestamp=datetime.fromisoformat("2024-01-01T10:00:00"),
            location="Test Location",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,
            message_received=None
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
