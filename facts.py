from experta import Fact, Field


class Additive(Fact):
    code = Field(str, mandatory=True)


class Warning(Fact):
    message = Field(str)
