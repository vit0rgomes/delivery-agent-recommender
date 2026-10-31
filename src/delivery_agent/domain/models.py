from enum import Enum
from pydantic import BaseModel, Field


class GlutenSafetyLevel(str, Enum):
    CERTIFIED_FREE = "certified_free"
    TRACES_POSSIBLE = "traces_possible"
    CONTAINS_GLUTEN = "contains_gluten"


class UserDietaryProfile(str, Enum):
    CELIAC = "celiac"
    INTOLERANT = "intolerant"
    LIFESTYLE = "lifestyle"
    STANDARD = "standard"


class AllergySeverity(str, Enum):
    ANAPHYLACTIC = "anaphylactic"
    SEVERE = "severe"
    MILD = "mild"


class DietaryRequirement(BaseModel):
    allergen: str
    severity: AllergySeverity = AllergySeverity.SEVERE


class UserProfile(BaseModel):
    id: str
    dietary_profile: UserDietaryProfile = UserDietaryProfile.STANDARD
    dietary_requirements: list[DietaryRequirement] = Field(default_factory=list)
    max_budget: float | None = None
    max_distance_km: float | None = None
    max_delivery_time_min: int | None = None


class Restaurant(BaseModel):
    id: str
    name: str
    rating: float = Field(ge=0.0, le=5.0)
    delivery_time_min: int = Field(gt=0)
    delivery_fee: float = Field(ge=0.0)
    distance_km: float = Field(gt=0.0)
    is_open: bool = True
    is_dedicated_gluten_free: bool = False
    safety_protocols: str | None = None
    cuisine_type: list[str] = Field(default_factory=list)


class DishItem(BaseModel):
    id: str
    restaurant_id: str
    name: str
    description: str
    price: float = Field(gt=0.0)
    category: str
    is_available: bool = True
    gluten_safety: GlutenSafetyLevel
    cross_contamination_note: str | None = None
    ingredients: list[str] = Field(default_factory=list)
    allergens: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


class UserQueryIntent(BaseModel):
    raw_query: str
    semantic_term: str = Field(description="Termo limpo para busca semântica de pratos")
    detected_profile: UserDietaryProfile = UserDietaryProfile.STANDARD
    allergies_to_avoid: list[str] = Field(default_factory=list)
    max_price: float | None = None
    max_delivery_time_min: int | None = None
    preferred_cuisine: str | None = None


class RecommendationResult(BaseModel):
    dish: DishItem
    restaurant: Restaurant
    final_score: float = Field(ge=0.0, le=1.0)
    safety_verdict: str
    explanation: str
