from delivery_agent.domain.models import DishItem, GlutenSafetyLevel, Restaurant


RESTAURANTS: list[Restaurant] = [
    Restaurant(
        id="rest_01",
        name="Raiz Livre - Cozinha 100% Sem Glúten",
        rating=4.9,
        delivery_time_min=30,
        delivery_fee=6.90,
        distance_km=2.4,
        is_open=True,
        is_dedicated_gluten_free=True,
        safety_protocols=(
            "Cozinha 100% exclusiva e certificada livre de glúten. "
            "Nenhum insumo com trigo, cevada ou centeio entra no estabelecimento. "
            "Embalagens lacradas contra contaminação no transporte."
        ),
        cuisine_type=["Saudável", "Brasileira", "Sem Glúten"],
    ),
    Restaurant(
        id="rest_02",
        name="Brasa & Burger Artesanal",
        rating=4.7,
        delivery_time_min=25,
        delivery_fee=5.50,
        distance_km=1.8,
        is_open=True,
        is_dedicated_gluten_free=False,
        safety_protocols=(
            "Oferecemos pão sem glúten, porém utilizamos a mesma chapa e fritadeira "
            "para pães tradicionais e empanados. Não recomendado para celíacos severos."
        ),
        cuisine_type=["Hamburgueria", "Lanches", "Americana"],
    ),
    Restaurant(
        id="rest_03",
        name="Bento & Bowl - Poke e Culinária Asiática",
        rating=4.8,
        delivery_time_min=35,
        delivery_fee=7.90,
        distance_km=3.2,
        is_open=True,
        is_dedicated_gluten_free=False,
        safety_protocols=(
            "Possuímos utensílios higienizados separadamente e opção de molho Tamari "
            "(shoyu sem glúten), mas a cozinha manipula massas de trigo para yakisoba."
        ),
        cuisine_type=["Japonesa", "Havaiana", "Poke", "Asiática"],
    ),
    Restaurant(
        id="rest_04",
        name="Verde Vivo - Plant-Based & Gluten Free",
        rating=4.9,
        delivery_time_min=40,
        delivery_fee=8.00,
        distance_km=4.1,
        is_open=True,
        is_dedicated_gluten_free=True,
        safety_protocols=(
            "Cozinha 100% vegana e 100% livre de glúten e lactose. "
            "Atenção para alérgicos a oleaginosas: manipulamos castanhas e amendoim."
        ),
        cuisine_type=["Vegana", "Vegetariana", "Saudável", "Sem Glúten"],
    ),
    Restaurant(
        id="rest_05",
        name="Nonna Mia Trattoria",
        rating=4.6,
        delivery_time_min=45,
        delivery_fee=9.90,
        distance_km=5.1,
        is_open=True,
        is_dedicated_gluten_free=False,
        safety_protocols=(
            "Cozinhamos massas sem glúten importadas em panela separada, mas nossa "
            "cozinha produz massas frescas de trigo artesanalmente (farinha em suspensão)."
        ),
        cuisine_type=["Italiana", "Massas"],
    ),
    Restaurant(
        id="rest_06",
        name="Empório Celíaco Gourmet",
        rating=5.0,
        delivery_time_min=55,
        delivery_fee=14.90,
        distance_km=9.5,
        is_open=True,
        is_dedicated_gluten_free=True,
        safety_protocols=(
            "Alta gastronomia 100% dedicada para celíacos. Laudo laboratorial de "
            "ausência de glúten (< 5 ppm) em todos os pratos."
        ),
        cuisine_type=["Contemporânea", "Frutos do Mar", "Sem Glúten", "Gourmet"],
    ),
    Restaurant(
        id="rest_07",
        name="Fit Express Marmitaria",
        rating=4.5,
        delivery_time_min=20,
        delivery_fee=0.00,
        distance_km=1.2,
        is_open=True,
        is_dedicated_gluten_free=False,
        safety_protocols=(
            "Alimentos naturais preparados no vapor e grelha. Não usamos farinha de trigo "
            "nas marmitas fit, mas compartilhamos o forno com tortas integrais."
        ),
        cuisine_type=["Marmita", "Fitness", "Brasileira", "Saudável"],
    ),
    Restaurant(
        id="rest_08",
        name="Forno D'Oro - Pizzaria Sem Glúten",
        rating=4.9,
        delivery_time_min=35,
        delivery_fee=6.00,
        distance_km=3.0,
        is_open=False,
        is_dedicated_gluten_free=True,
        safety_protocols="Pizzaria exclusiva sem glúten e sem lactose. Forno dedicado.",
        cuisine_type=["Pizzaria", "Italiana", "Sem Glúten"],
    ),
]


DISHES: list[DishItem] = [
    DishItem(
        id="dish_01",
        restaurant_id="rest_01",
        name="Escondidinho de Mandioca com Carne de Sol",
        description=(
            "Purê cremoso de mandioca feito com leite vegetal de inhame, recheado "
            "com carne de sol desfiada acebolada. Totalmente livre de glúten e lactose."
        ),
        price=38.90,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["mandioca", "carne de sol", "leite de inhame", "azeite", "cebola", "alho", "cheiro-verde"],
        allergens=[],
        tags=["sem_gluten", "sem_lactose", "proteico", "jantar_leve", "brasileira"],
    ),
    DishItem(
        id="dish_02",
        restaurant_id="rest_01",
        name="Pizza Margherita em Massa de Fermentação Natural Sem Glúten",
        description=(
            "Massa artesanal de farinha de arroz, fécula de batata e psyllium. "
            "Coberta com molho de tomate pelati, muçarela zero lactose e manjericão fresco."
        ),
        price=48.00,
        category="Pizza",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["farinha de arroz", "fécula de batata", "psyllium", "tomate pelati", "queijo muçarela zero lactose", "manjericão"],
        allergens=["leite"],
        tags=["sem_gluten", "zero_lactose", "pizza", "vegetariano"],
    ),
    DishItem(
        id="dish_03",
        restaurant_id="rest_01",
        name="Tilápia Grelhada com Quinoa e Legumes ao Vapor",
        description="Filé de tilápia fresca grelhada no azeite de ervas com quinoa real e brócolis.",
        price=42.50,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["filé de tilápia", "quinoa", "brócolis", "cenoura", "azeite de oliva", "limão", "ervas finas"],
        allergens=["peixe"],
        tags=["sem_gluten", "sem_lactose", "jantar_leve", "low_carb", "saudavel"],
    ),
    DishItem(
        id="dish_04",
        restaurant_id="rest_02",
        name="Burger Artesanal no Pão Sem Glúten",
        description=(
            "Blend bovino 160g, queijo cheddar, alface e tomate servido em pão de batata sem glúten. "
            "Atenção: preparado na mesma chapa dos lanches tradicionais."
        ),
        price=36.00,
        category="Lanche",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.TRACES_POSSIBLE,
        cross_contamination_note="Pão sem glúten selado na mesma chapa onde são tostados pães de brioche com trigo.",
        ingredients=["carne bovina", "pão de batata sem glúten", "queijo cheddar", "alface", "tomate", "maionese da casa"],
        allergens=["leite", "ovo"],
        tags=["hamburguer", "lanche"],
    ),
    DishItem(
        id="dish_05",
        restaurant_id="rest_02",
        name="Porção de Batata Frita Rústica com Alecrim",
        description="Batatas cortadas artesanalmente e fritas com alecrim e alho.",
        price=22.00,
        category="Acompanhamento",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.TRACES_POSSIBLE,
        cross_contamination_note="Frita no mesmo óleo compartilhado com anéis de cebola empanados em farinha de trigo.",
        ingredients=["batata inglesa", "óleo vegetal", "alecrim", "alho", "sal"],
        allergens=[],
        tags=["porcao", "vegano", "sem_lactose"],
    ),
    DishItem(
        id="dish_06",
        restaurant_id="rest_02",
        name="Smash Burger Duplo Bacon no Brioche",
        description="Dois burgers 90g prensados na chapa, pão brioche amanteigado, cheddar duplo e bacon.",
        price=34.90,
        category="Lanche",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CONTAINS_GLUTEN,
        cross_contamination_note="Contém trigo diretamente na composição do pão.",
        ingredients=["pão brioche (farinha de trigo)", "carne bovina", "queijo cheddar", "bacon"],
        allergens=["glúten", "trigo", "leite", "ovo"],
        tags=["hamburguer", "bacon"],
    ),
    DishItem(
        id="dish_07",
        restaurant_id="rest_03",
        name="Poke Havaiano de Salmão (Com Tamari Sem Glúten)",
        description=(
            "Base de arroz japonês (gohan), salmão em cubos, abacate, pepino sunomono, "
            "manga e molho Tamari (shoyu de fermentação 100% soja, sem trigo)."
        ),
        price=44.90,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.TRACES_POSSIBLE,
        cross_contamination_note="Preparado em bancada higienizada, porém a cozinha manipula trigo em outros pratos.",
        ingredients=["arroz japonês", "salmão", "abacate", "pepino", "manga", "molho tamari sem glúten", "gergelim"],
        allergens=["peixe", "soja", "gergelim"],
        tags=["sem_lactose", "jantar_leve", "poke", "fresco", "saudavel"],
    ),
    DishItem(
        id="dish_08",
        restaurant_id="rest_03",
        name="Combinado Salmão 16 Peças com Shoyu Tradicional",
        description="Sashimis, niguiris e uramakis de salmão com cream cheese. Acompanha sachês de shoyu tradicional.",
        price=54.00,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CONTAINS_GLUTEN,
        cross_contamination_note="O molho shoyu tradicional contém trigo na fermentação.",
        ingredients=["arroz japonês", "salmão", "cream cheese", "alga nori", "molho shoyu tradicional (soja e trigo)"],
        allergens=["glúten", "trigo", "peixe", "leite", "soja"],
        tags=["japonesa", "sushi"],
    ),
    DishItem(
        id="dish_09",
        restaurant_id="rest_03",
        name="Yakisoba Tradicional de Frango e Legumes",
        description="Macarrão oriental frito com tiras de frango, brócolis, acelga e molho à base de shoyu.",
        price=39.90,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CONTAINS_GLUTEN,
        cross_contamination_note="Macarrão de farinha de trigo e molho shoyu com trigo.",
        ingredients=["macarrão para yakisoba (farinha de trigo)", "frango", "brócolis", "cenoura", "molho shoyu", "óleo de gergelim"],
        allergens=["glúten", "trigo", "soja", "gergelim"],
        tags=["japonesa", "massa"],
    ),
    DishItem(
        id="dish_10",
        restaurant_id="rest_04",
        name="Bowl Mediterrâneo de Grão-de-Bico, Quinoa e Tofu",
        description=(
            "Bowl nutritivo com quinoa, grão-de-bico assado com páprica, tofu grelhado, "
            "abóbora cabotiá e molho de ervas. 100% livre de glúten e lactose."
        ),
        price=34.90,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["quinoa", "grão-de-bico", "tofu", "abóbora cabotiá", "espinafre", "azeite", "páprica"],
        allergens=["soja"],
        tags=["sem_gluten", "sem_lactose", "vegano", "jantar_leve", "barato", "saudavel"],
    ),
    DishItem(
        id="dish_11",
        restaurant_id="rest_04",
        name="Pad Thai Vegano de Bifum (Macarrão de Arroz) com Amendoim",
        description=(
            "Macarrão de arroz salteado na wok com legumes, broto de feijão, tofu, "
            "molho de tamarindo e generosa cobertura de amendoim torrado e pasta de amendoim."
        ),
        price=41.00,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["macarrão de arroz (bifum)", "tofu", "pasta de amendoim", "amendoim torrado", "tamarindo", "broto de feijão", "cenoura"],
        allergens=["amendoim", "soja"],
        tags=["sem_gluten", "sem_lactose", "vegano", "asiatica"],
    ),
    DishItem(
        id="dish_12",
        restaurant_id="rest_04",
        name="Moqueca Vegana de Banana-da-Terra com Creme de Castanha",
        description="Moqueca baiana feita com banana-da-terra, pimentões, leite de coco e creme de castanha-de-caju.",
        price=43.90,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["banana-da-terra", "leite de coco", "castanha-de-caju", "arroz integral", "azeite de dendê", "coentro"],
        allergens=["castanhas", "oleaginosas"],
        tags=["sem_gluten", "sem_lactose", "vegano", "brasileira"],
    ),
    DishItem(
        id="dish_13",
        restaurant_id="rest_05",
        name="Penne Sem Glúten Importado ao Molho Pomodoro e Manjericão",
        description="Massa italiana de milho e arroz sem glúten ao molho de tomates frescos.",
        price=46.00,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.TRACES_POSSIBLE,
        cross_contamination_note=(
            "Embora a massa seja certificada sem glúten e cozida em água exclusiva, "
            "o ambiente possui farinha de trigo em suspensão devido à produção de massas frescas."
        ),
        ingredients=["penne de milho e arroz", "tomate italiano", "alho", "manjericão", "azeite"],
        allergens=[],
        tags=["italiana", "sem_lactose", "vegano"],
    ),
    DishItem(
        id="dish_14",
        restaurant_id="rest_05",
        name="Lasanha Artesanal à Bolonhesa",
        description="Massa fresca de trigo com ragu de carne bovina, molho bechamel e queijo parmesão gratinado.",
        price=52.00,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CONTAINS_GLUTEN,
        cross_contamination_note="Contém farinha de trigo na massa e no molho bechamel.",
        ingredients=["farinha de trigo", "ovos", "carne bovina", "leite", "manteiga", "queijo parmesão", "molho de tomate"],
        allergens=["glúten", "trigo", "leite", "ovo"],
        tags=["italiana", "massa"],
    ),
    DishItem(
        id="dish_15",
        restaurant_id="rest_06",
        name="Risoto de Camarão Rosa com Açafrão e Limão Siciliano",
        description="Arroz arbóreo cremoso com camarões rosa grelhados, manteiga sem lactose e toque cítrico.",
        price=78.00,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["arroz arbóreo", "camarão rosa", "manteiga zero lactose", "açafrão", "limão siciliano", "caldo de legumes caseiro"],
        allergens=["camarão", "frutos do mar", "crustáceos", "leite"],
        tags=["sem_gluten", "zero_lactose", "gourmet", "jantar_especial"],
    ),
    DishItem(
        id="dish_16",
        restaurant_id="rest_06",
        name="Nhoque de Mandioquinha ao Ragu de Costela (Zero Glúten e Zero Lactose)",
        description="Nhoque artesanal derretendo na boca feito com mandioquinha e farinha de arroz.",
        price=58.00,
        category="Prato Principal",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["mandioquinha", "farinha de arroz", "costela bovina", "tomate", "vinho tinto", "ervas"],
        allergens=[],
        tags=["sem_gluten", "sem_lactose", "gourmet"],
    ),
    DishItem(
        id="dish_17",
        restaurant_id="rest_07",
        name="Marmita Fit: Frango Grelhado, Batata-Doce e Brócolis",
        description="Peito de frango em cubos grelhado, batata-doce cozida e brócolis no vapor. Sem adição de farinhas.",
        price=25.90,
        category="Marmita",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.TRACES_POSSIBLE,
        cross_contamination_note="Ingredientes naturalmente livres de glúten, mas preparados em cozinha que manipula aveia e trigo.",
        ingredients=["peito de frango", "batata-doce", "brócolis", "azeite", "sal", "alho"],
        allergens=[],
        tags=["sem_lactose", "barato", "rapido", "fitness", "proteico", "jantar_leve"],
    ),
    DishItem(
        id="dish_18",
        restaurant_id="rest_07",
        name="Omelete Funcional de Claras com Espinafre e Tomate Seco",
        description="Omelete leve rica em proteínas sem farinha e sem lactose.",
        price=24.00,
        category="Prato Principal",
        is_available=False,
        gluten_safety=GlutenSafetyLevel.TRACES_POSSIBLE,
        cross_contamination_note="Preparado em cozinha compartilhada.",
        ingredients=["clara de ovo", "espinafre", "tomate seco", "orégano"],
        allergens=["ovo"],
        tags=["sem_lactose", "low_carb", "jantar_leve", "barato"],
    ),
    DishItem(
        id="dish_19",
        restaurant_id="rest_08",
        name="Pizza Calabresa Artesanal Sem Glúten e Sem Lactose",
        description="Massa crocante sem glúten com calabresa artesanal defumada, cebola roxa e queijo vegano.",
        price=49.90,
        category="Pizza",
        is_available=True,
        gluten_safety=GlutenSafetyLevel.CERTIFIED_FREE,
        cross_contamination_note=None,
        ingredients=["mix de farinhas sem glúten", "calabresa artesanal", "cebola roxa", "queijo de castanha", "molho de tomate"],
        allergens=["castanhas"],
        tags=["sem_gluten", "sem_lactose", "pizza"],
    ),
]

RESTAURANT_MAP: dict[str, Restaurant] = {rest.id: rest for rest in RESTAURANTS}


def get_restaurant_by_id(restaurant_id: str) -> Restaurant | None:
    return RESTAURANT_MAP.get(restaurant_id)
