"""
Módulo de Domínio: Modelos e Schemas de Dados do Sistema de Recomendação de Delivery.
Focado em Segurança Alimentar, Alérgenos e Contaminação Cruzada (Celíacos / Intolerantes).

Organização em 4 escopos:
1. Enums e Taxonomia de Segurança
2. Perfil e Restrições do Usuário
3. Catálogo e Operação (Restaurante e Pratos)
4. Modelos de IA e Orquestração (LangGraph)
"""

from enum import Enum
from pydantic import BaseModel, Field


# ==============================================================================
# 1. ENUMS E TAXONOMIA DE SEGURANÇA ALIMENTAR
# ==============================================================================

class GlutenSafetyLevel(str, Enum):
    """
    Classificação estrita do nível de segurança em relação ao glúten.
    Diferencia cozinhas isoladas de cozinhas com manipulação compartilhada.
    """
    CERTIFIED_FREE = "certified_free"        # Cozinha 100% dedicada e sem glúten (Seguro para Celíacos)
    TRACES_POSSIBLE = "traces_possible"      # Ingredientes sem glúten, mas manipulado com risco de contaminação cruzada
    CONTAINS_GLUTEN = "contains_gluten"      # Contém glúten tradicional (trigo, centeio, cevada)


class UserDietaryProfile(str, Enum):
    """
    Define o perfil alimentar e o grau de rigor exigido pelo usuário.
    """
    CELIAC = "celiac"                        # Doença Celíaca: Tolerância ZERO a contaminação cruzada
    INTOLERANT = "intolerant"                # Intolerância / Hipersensibilidade: aceita traços com aviso explícito
    LIFESTYLE = "lifestyle"                  # Preferência pessoal ou dieta estética (ex: low-carb)
    STANDARD = "standard"                    # Usuário sem restrições alimentares declaradas


class AllergySeverity(str, Enum):
    """
    Gravidade médica de uma alergia alimentar.
    """
    ANAPHYLACTIC = "anaphylactic"            # Risco iminente de choque anafilático / risco de vida
    SEVERE = "severe"                        # Reação severa que exige medicação / hospital
    MILD = "mild"                            # Desconforto leve / moderado


# ==============================================================================
# 2. PERFIL E RESTRIÇÕES DO USUÁRIO (Dados do Cliente)
# ==============================================================================

class DietaryRequirement(BaseModel):
    """
    Representa uma restrição ou alergia alimentar específica do cliente e sua gravidade.
    Exemplo: Alergia a amendoim com gravidade anafilática.
    """
    allergen: str = Field(description="Nome do alérgeno (ex: glúten, lactose, amendoim, frutos do mar)")
    severity: AllergySeverity = Field(
        default=AllergySeverity.SEVERE,
        description="Gravidade médica da alergia"
    )


class UserProfile(BaseModel):
    """
    Perfil consolidado do cliente na plataforma.
    Usado para personalizar filtros, calcular distâncias e orçamentos máximos.
    """
    id: str = Field(description="Identificador único do usuário")
    dietary_profile: UserDietaryProfile = Field(
        default=UserDietaryProfile.STANDARD,
        description="Perfil base em relação ao glúten"
    )
    dietary_requirements: list[DietaryRequirement] = Field(
        default_factory=list,
        description="Lista detalhada de alergias e sensibilidades do cliente"
    )
    max_budget: float | None = Field(
        default=None, 
        description="Orçamento máximo médio preferido pelo usuário em R$"
    )
    max_distance_km: float | None = Field(
        default=None, 
        description="Raio máximo de entrega tolerado em km"
    )
    max_delivery_time_min: int | None = Field(
        default=None, 
        description="Tempo máximo tolerado de entrega em minutos"
    )


# ==============================================================================
# 3. CATÁLOGO E OPERAÇÃO (Restaurantes e Cardápio)
# ==============================================================================

class Restaurant(BaseModel):
    """
    Entidade de negócio do restaurante parceiro.
    Carrega tanto informações operacionais (SLA, distância) quanto sanitárias.
    """
    id: str = Field(description="Identificador único do restaurante")
    name: str = Field(description="Nome comercial do restaurante")
    rating: float = Field(ge=0.0, le=5.0, description="Nota média de avaliação dos clientes (0.0 a 5.0)")
    delivery_time_min: int = Field(gt=0, description="Tempo estimado de entrega em minutos")
    delivery_fee: float = Field(ge=0.0, description="Taxa de entrega cobrada em R$")
    distance_km: float = Field(gt=0.0, description="Distância física do restaurante até o cliente em km")
    is_open: bool = Field(default=True, description="Indica se a cozinha está recebendo pedidos no momento")
    is_dedicated_gluten_free: bool = Field(
        default=False,
        description="Indica se o estabelecimento é 100% livre de glúten (sem farinha no ambiente)"
    )
    safety_protocols: str | None = Field(
        default=None,
        description="Descrição formal dos protocolos de prevenção de contaminação cruzada"
    )
    cuisine_type: list[str] = Field(
        default_factory=list,
        description="Tipos de culinária atendidos (ex: ['Pizzaria', 'Saudável', 'Marmita'])"
    )


class DishItem(BaseModel):
    """
    Item individual do cardápio.
    Possui detalhamento de ingredientes para auditoria automatizada por IA.
    """
    id: str = Field(description="Identificador único do prato")
    restaurant_id: str = Field(description="ID do restaurante que produz o prato")
    name: str = Field(description="Nome comercial do prato")
    description: str = Field(description="Descrição detalhada visível no cardápio")
    price: float = Field(gt=0.0, description="Preço unitário em R$")
    category: str = Field(description="Categoria do item (ex: Prato Principal, Sobremesa, Entrada)")
    is_available: bool = Field(default=True, description="Indica se o prato possui estoque para venda")
    gluten_safety: GlutenSafetyLevel = Field(
        description="Status de segurança do prato em relação ao glúten"
    )
    cross_contamination_note: str | None = Field(
        default=None,
        description="Aviso específico sobre manipulação (ex: frito na mesma fritadeira de salgados)"
    )
    ingredients: list[str] = Field(
        default_factory=list,
        description="Lista detalhada de ingredientes usada pela IA para auditoria de segurança"
    )
    allergens: list[str] = Field(
        default_factory=list,
        description="Lista explícita de alérgenos contidos no prato"
    )
    tags: list[str] = Field(
        default_factory=list,
        description="Tags de contexto e busca (ex: ['sem_lactose', 'vegano', 'low_carb'])"
    )


# ==============================================================================
# 4. MODELOS DE IA E ORQUESTRAÇÃO (LangGraph & Recommender)
# ==============================================================================

class UserQueryIntent(BaseModel):
    """
    Estrutura de saída do nó de compreensão de linguagem natural (NLU).
    Extrai as entidades e intenções da mensagem livre enviada pelo usuário no chat.
    """
    raw_query: str = Field(description="A mensagem de texto original digitada pelo usuário")
    semantic_term: str = Field(
        description="Termo purificado e sem ruídos para a busca vetorial (ex: 'jantar leve saudável')"
    )
    detected_profile: UserDietaryProfile = Field(
        default=UserDietaryProfile.STANDARD,
        description="Perfil alimentar inferido da mensagem do usuário"
    )
    allergies_to_avoid: list[str] = Field(
        default_factory=list,
        description="Lista de alérgenos que devem ser rigorosamente excluídos da recomendação"
    )
    max_price: float | None = Field(
        default=None,
        description="Teto de preço especificado pelo usuário na mensagem"
    )
    max_delivery_time_min: int | None = Field(
        default=None,
        description="Tempo máximo de espera aceito pelo usuário na mensagem"
    )
    preferred_cuisine: str | None = Field(
        default=None,
        description="Culinária solicitada especificamente (ex: 'japonesa', 'pizza')"
    )


class RecommendationResult(BaseModel):
    """
    Contrato final do recomendador após passar pelas etapas de:
    Retrieval -> Safety Guardrail -> Multi-Objective Re-ranking -> NLG Explanation.
    """
    dish: DishItem = Field(description="O prato recomendado")
    restaurant: Restaurant = Field(description="O restaurante fornecedor")
    final_score: float = Field(
        ge=0.0, le=1.0,
        description="Score normalizado combinando relevância semântica e critérios de negócio"
    )
    safety_verdict: str = Field(
        description="Selo explícito de segurança (ex: '100% SEGURO PARA CELÍACOS' ou 'ALERTA DE CONTAMINAÇÃO')"
    )
    explanation: str = Field(
        description="Justificativa em linguagem natural amigável explicando por que o prato foi recomendado"
    )
