from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    return f"{ingredients} - VALID" if any(
        a in ingredients.lower() for a in allowed
        ) else f"{ingredients} - INVALID"
