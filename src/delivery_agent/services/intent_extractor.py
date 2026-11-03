"""
Módulo de Extração Semântica de Intenção (LLM Structured Output & Prompt Engineering).
Converte buscas em linguagem natural do usuário no contrato tipado `UserQueryIntent`.
"""

from delivery_agent.domain.models import UserDietaryProfile, UserQueryIntent

SYSTEM_PROMPT_INTENT_EXTRACTOR = """
Você é um Engenheiro de Segurança Alimentar e Especialista em Triagem de Pedidos de Delivery.
Sua tarefa é analisar o pedido em linguagem natural do usuário e extrair um objeto JSON
estritamente compatível com o schema `UserQueryIntent`.

### REGRAS CRÍTICAS DE SEGURANÇA (GUARDRAILS):
1. DETECÇÃO DE PERFIL DIETÉTICO (`detected_profile`):
   - Se o usuário mencionar "celíaco", "doença celíaca", "contaminação cruzada" ou "alergia severa a glúten", classifique OBRIGATORIAMENTE como `"celiac"`.
   - Se mencionar "intolerante a glúten" ou "sensibilidade", classifique como `"intolerant"`.
   - Se mencionar apenas dieta/preferência ("evito glúten", "fit"), classifique como `"lifestyle"`.
   - Caso contrário, utilize `"standard"`.

2. EXTRAÇÃO DE ALÉRGENOS (`allergies_to_avoid`):
   - Extraia todos os ingredientes ou famílias de alérgenos que o usuário não pode consumir (ex: ["amendoim", "castanha", "lactose", "leite", "camarão", "soja"]).
   - Na dúvida, priorize o falso-positivo protetor: inclua variações óbvias do ingrediente.

3. RESTRIÇÕES LOGÍSTICAS (`max_price`, `max_delivery_time_min`):
   - Extraia valores numéricos de orçamento máximo (R$) e tempo limite de entrega (minutos) apenas quando explicitados.

4. TERMO SEMÂNTICO (`semantic_term`):
   - Limpe as restrições médicas e logísticas, mantendo apenas o prato, culinária ou desejo gastronômico central para a busca vetorial.
""".strip()

FEW_SHOT_EXAMPLES = [
    {
        "user_input": "Sou celíaco severo e também tenho alergia a amendoim. Quero uma pizza até 65 reais que chegue em 40 min.",
        "expected_output": {
            "raw_query": "Sou celíaco severo e também tenho alergia a amendoim. Quero uma pizza até 65 reais que chegue em 40 min.",
            "semantic_term": "pizza artesanal",
            "detected_profile": UserDietaryProfile.CELIAC.value,
            "allergies_to_avoid": ["amendoim", "pasta de amendoim"],
            "max_price": 65.0,
            "max_delivery_time_min": 40,
            "preferred_cuisine": "italiana",
        },
    },
    {
        "user_input": "Quero pedir um hambúrguer artesanal rápido, no máximo 30 minutos, sem queijo porque sou intolerante a lactose.",
        "expected_output": {
            "raw_query": "Quero pedir um hambúrguer artesanal rápido, no máximo 30 minutos, sem queijo porque sou intolerante a lactose.",
            "semantic_term": "hambúrguer artesanal sem laticínios",
            "detected_profile": UserDietaryProfile.STANDARD.value,
            "allergies_to_avoid": ["lactose", "leite", "queijo", "manteiga"],
            "max_price": None,
            "max_delivery_time_min": 30,
            "preferred_cuisine": "hamburgueria",
        },
    },
]


def build_intent_prompt(user_query: str) -> list[dict[str, str]]:
    """
    Constrói o payload de mensagens estruturado (System + Few-Shot + User)
    pronto para chamada em APIs de LLMs (Gemini / OpenAI / Ollama) com Structured Outputs.
    """
    messages: list[dict[str, str]] = [
        {"role": "system", "content": SYSTEM_PROMPT_INTENT_EXTRACTOR}
    ]
    for example in FEW_SHOT_EXAMPLES:
        messages.append({"role": "user", "content": str(example["user_input"])})
        messages.append(
            {
                "role": "assistant",
                "content": UserQueryIntent(**example["expected_output"]).model_dump_json(),
            }
        )
    messages.append({"role": "user", "content": user_query})
    return messages
