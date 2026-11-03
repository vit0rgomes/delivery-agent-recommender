# 🛵 Delivery Agent Recommender — Recomendação Contextual com Segurança Alimentar

Sistema de recomendação e filtragem inteligente para plataformas de delivery de alimentos, projetado com foco em **restrições alimentares críticas (Doença Celíaca, Alergias Severas e Intolerâncias)** e **restrições logísticas (Orçamento e SLA de Entrega)**.

---

## 🎯 Problema de Negócio

Sistemas de recomendação puramente probabilísticos ou baseados apenas em similaridade semântica podem sugerir pratos com risco de **contaminação cruzada** ou **alérgenos ocultos** na lista de ingredientes — uma falha inaceitável para usuários celíacos ou anafiláticos.

Este projeto implementa uma arquitetura em estágios onde **regras determinísticas de domínio (*Hard Constraints*)** atuam antes do ranqueamento, garantindo segurança alimentar 100% auditável.

---

## 🏗️ Arquitetura do Projeto

```text
src/delivery_agent/
├── data/
│   └── catalog.py         # Catálogo estruturado de restaurantes, protocolos e pratos
├── domain/
│   └── models.py          # Contratos de dados e validação tipada (Pydantic)
└── services/
    └── safety_filter.py   # Estágio 1: Funil determinístico de segurança e logística
```

### Principais Componentes
1. **Modelagem de Domínio (`domain/models.py`):**
   - Perfis dietéticos (`CELIAC`, `INTOLERANT`, `LIFESTYLE`, `STANDARD`) e níveis de segurança de glúten (`CERTIFIED_FREE`, `TRACES_POSSIBLE`, `CONTAINS_GLUTEN`).
   - Estruturação da intenção de busca do usuário (`UserQueryIntent`) e resultado explicável (`RecommendationResult`).
2. **Filtro Determinístico de Segurança (`services/safety_filter.py`):**
   - **Validação Operacional (`is_operation_valid`):** Garante apenas restaurantes abertos e pratos disponíveis em estoque.
   - **Trava Anti-Contaminação Cruzada (`is_gluten_safe`):** Para perfis celíacos, exige simultaneamente prato certificado sem glúten **e** cozinha 100% dedicada (`is_dedicated_gluten_free`).
   - **Varredura Dupla de Alérgenos (`is_allergen_safe`):** Inspeciona tanto os alérgenos declarados quanto a lista bruta de ingredientes para bloquear alérgenos ocultos.
   - **Filtro Logístico (`matches_logistics`):** Respeita tetos de orçamento (`max_price`) e tempo máximo de entrega (`max_delivery_time_min`).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pydantic** (Validação de dados, serialização e contratos de domínio)
