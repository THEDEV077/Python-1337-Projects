def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    return f"{ingredients} - VALID" if any(
        a in ingredients.lower() for a in allowed
        ) else f"{ingredients} - INVALID"
