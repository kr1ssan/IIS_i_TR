from experta import KnowledgeEngine, Rule, MATCH, TEST
from facts import Additive, Warning
from constants import *


class AdditiveExpert(KnowledgeEngine):

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in BANNED))
    def banned(self, code):
        self.declare(Warning(message=f"Добавка {code} запрещена к использованию."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in VERY_DANGEROUS))
    def very_dangerous(self, code):
        self.declare(Warning(message=f"Добавка {code} признана очень опасной."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in DANGEROUS))
    def dangerous(self, code):
        self.declare(Warning(message=f"Добавка {code} признана опасной."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in DANGEROUS_FOR_CHILDREN))
    def dangerous_for_children(self, code):
        self.declare(Warning(message=f"Добавка {code} признана опасной для детей."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in SUSPICIOUS))
    def suspicious(self, code):
        self.declare(Warning(message=f"Добавка {code} имеет подозрительное воздействие."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in CARCINOGENIC))
    def carcinogenic(self, code):
        self.declare(Warning(message=f"Добавка {code} может быть канцерогенной."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in STOMACH_DISORDER))
    def stomach_disorder(self, code):
        self.declare(Warning(message=f"Добавка {code} может вызвать расстройство желудка."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in INTESTINAL_DISORDER))
    def intestinal_disorder(self, code):
        self.declare(Warning(message=f"Добавка {code} может вызвать расстройство кишечника."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in SKIN_DISEASE))
    def skin_disease(self, code):
        self.declare(Warning(message=f"Добавка {code} может вызывать кожные заболевания или аллергические реакции."))

    @Rule(Additive(code=MATCH.code), TEST(lambda code: code in PRESSURE_EFFECTS))
    def pressure_effects(self, code):
        self.declare(Warning(message=f"Добавка {code} может повышать давление."))
