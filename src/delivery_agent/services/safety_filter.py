from delivery_agent.domain.models import (
    DishItem,
    GlutenSafetyLevel,
    Restaurant,
    UserDietaryProfile,
    UserQueryIntent,
)


def is_operation_valid(dish: DishItem, restaurant: Restaurant) -> bool:
    """Garante que apenas lojas abertas e itens em estoque entrem no funil."""
    return restaurant.is_open and dish.is_available


def is_gluten_safe(
    dish: DishItem,
    restaurant: Restaurant,
    profile: UserDietaryProfile,
) -> bool:
    """
    Aplica a trava de segurança de glúten conforme a severidade do perfil.
    Celíacos exigem tanto receita sem glúten quanto cozinha 100% dedicada (sem traços).
    """
    if profile == UserDietaryProfile.CELIAC:
        return (
            dish.gluten_safety == GlutenSafetyLevel.CERTIFIED_FREE
            and restaurant.is_dedicated_gluten_free
        )
    elif profile == UserDietaryProfile.INTOLERANT or profile == UserDietaryProfile.LIFESTYLE:
        return dish.gluten_safety != GlutenSafetyLevel.CONTAINS_GLUTEN
    return True


def is_allergen_safe(dish: DishItem, allergies_to_avoid: list[str]) -> bool:
    """
    Checa alérgenos declarados e também varre a lista de ingredientes
    para capturar alérgenos ocultos (ex: 'pasta de amendoim').
    """
    for a in allergies_to_avoid:
        for b in dish.allergens:
            if a.lower() in b.lower():
                return False
        for c in dish.ingredients:
            if a.lower() in c.lower():
                return False
    return True


def matches_logistics(
    dish: DishItem,
    restaurant: Restaurant,
    max_price: float | None = None,
    max_delivery_time_min: int | None = None,
) -> bool:
    """Filtra restrições de orçamento e SLA de entrega quando especificadas pelo usuário."""
    if max_price is not None and dish.price > max_price:
        return False
    if max_delivery_time_min is not None and restaurant.delivery_time_min > max_delivery_time_min:
        return False
    return True


def filter_safe_candidates(
    dishes: list[DishItem],
    restaurant_map: dict[str, Restaurant],
    intent: UserQueryIntent,
) -> list[tuple[DishItem, Restaurant]]:
    """
    Estágio 1 do Recomendador (Hard Constraints):
    Elimina deterministamente candidatos inválidos ou inseguros antes do ranking.
    """
    safe_candidates: list[tuple[DishItem, Restaurant]] = []
    for dish in dishes:
        restaurant = restaurant_map.get(dish.restaurant_id)
        if (
            restaurant is not None
            and is_operation_valid(dish, restaurant)
            and is_gluten_safe(dish, restaurant, intent.detected_profile)
            and is_allergen_safe(dish, intent.allergies_to_avoid)
            and matches_logistics(dish, restaurant, intent.max_price, intent.max_delivery_time_min)
        ):
            safe_candidates.append((dish, restaurant))
    return safe_candidates