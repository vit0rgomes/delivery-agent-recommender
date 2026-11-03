# 🛵 Delivery Agent Recommender — Agente de IA & Recomendação com Segurança Alimentar

Sistema híbrido de recomendação para plataformas de delivery de alimentos que combina **Engenharia de Prompt Estruturada (LLMs + Structured Outputs)** para interpretação de intenção em linguagem natural com um **Funil Determinístico de Segurança Alimentar (*Hard Constraints*)** para restrições médicas severas (Doença Celíaca, Alergias Anafiláticas e Intolerâncias) e logística (Orçamento e SLA).

---

## 🎯 Problema de Negócio

Sistemas de recomendação puramente probabilísticos ou baseados apenas em similaridade semântica podem sugerir pratos com risco de **contaminação cruzada** ou **alérgenos ocultos** na lista de ingredientes — uma falha inaceitável para usuários celíacos ou anafiláticos.

Este projeto resolve o problema separando a arquitetura em dois estágios complementares:
1. **Compreensão Semântica (LLM + Prompt Estruturado + Few-Shot):** Extrai restrições explícitas e implícitas da busca em linguagem natural para um contrato rigoroso (`UserQueryIntent`).
2. **Filtragem Determinística (*Hard Constraints*):** Elimina 100% dos candidatos inseguros ou fora de SLA antes da etapa de ranqueamento.

---

## 🏗️ Arquitetura do Projeto

```text
src/delivery_agent/
├── data/
│   └── catalog.py            # Catálogo estruturado de restaurantes, protocolos e pratos
├── domain/
│   └── models.py             # Contratos de dados e validação tipada (Pydantic)
└── services/
    ├── intent_extractor.py   # Engenharia de Prompt (System Prompt, Guardrails e Few-Shot)
    └── safety_filter.py      # Funil determinístico de segurança alimentar e logística
```

---

## 🧠 Engenharia de Prompt & Experimentação com LLMs (`intent_extractor.py`)

Para evitar alucinações na interpretação do pedido do usuário, o agente utiliza **Structured Outputs** validados via `Pydantic` combinados com **Guardrails de Segurança** e **Few-Shot Prompting**:

### System Prompt & Guardrails
```text
Você é um Engenheiro de Segurança Alimentar e Especialista em Triagem de Pedidos de Delivery.
Sua tarefa é analisar o pedido em linguagem natural do usuário e extrair um objeto JSON
estritamente compatível com o schema `UserQueryIntent`.

REGRAS CRÍTICAS DE SEGURANÇA (GUARDRAILS):
1. DETECÇÃO DE PERFIL DIETÉTICO (`detected_profile`):
   - Se o usuário mencionar "celíaco", "doença celíaca", "contaminação cruzada" ou "alergia severa a glúten", classifique OBRIGATORIAMENTE como "celiac".
   - Se mencionar "intolerante a glúten" ou "sensibilidade", classifique como "intolerant".
2. EXTRAÇÃO DE ALÉRGENOS (`allergies_to_avoid`):
   - Extraia todos os ingredientes ou famílias de alérgenos que o usuário não pode consumir.
   - Na dúvida, priorize o falso-positivo protetor: inclua variações óbvias do ingrediente.
3. RESTRIÇÕES LOGÍSTICAS (`max_price`, `max_delivery_time_min`):
   - Extraia valores numéricos de orçamento máximo (R$) e tempo limite de entrega (minutos).
4. TERMO SEMÂNTICO (`semantic_term`):
   - Limpe as restrições médicas e logísticas, mantendo apenas o desejo gastronômico central.
```

### Exemplo de Transformação (Few-Shot)
- **Entrada do Usuário:**  
  `"Sou celíaco severo e também tenho alergia a amendoim. Quero uma pizza até 65 reais que chegue em 40 min."`
- **Saída Estruturada (`UserQueryIntent`):**
```json
{
  "raw_query": "Sou celíaco severo e também tenho alergia a amendoim. Quero uma pizza até 65 reais que chegue em 40 min.",
  "semantic_term": "pizza artesanal",
  "detected_profile": "celiac",
  "allergies_to_avoid": ["amendoim", "pasta de amendoim"],
  "max_price": 65.0,
  "max_delivery_time_min": 40,
  "preferred_cuisine": "italiana"
}
```

---

## 🛡️ Filtro Determinístico de Segurança (`safety_filter.py`)

- **Validação Operacional (`is_operation_valid`):** Garante apenas restaurantes abertos e pratos disponíveis em estoque.
- **Trava Anti-Contaminação Cruzada (`is_gluten_safe`):** Para perfis `CELIAC`, exige simultaneamente prato `CERTIFIED_FREE` **e** cozinha 100% dedicada (`is_dedicated_gluten_free = True`).
- **Varredura Dupla de Alérgenos (`is_allergen_safe`):** Inspeciona tanto os alérgenos declarados quanto a lista bruta de ingredientes para bloquear alérgenos ocultos (ex.: *"pasta de amendoim"* em molhos asiáticos).
- **Filtro Logístico (`matches_logistics`):** Respeita tetos de orçamento (`max_price`) e SLA máximo de entrega (`max_delivery_time_min`).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pydantic** (Structured Outputs, validação de contratos de domínio e serialização JSON)
- **Prompt Engineering** (System Prompts com Guardrails de domínio e Few-Shot Learning)
