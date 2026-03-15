from dataclasses import dataclass, field


@dataclass
class StockAnalysisContext:

    symbol: str

    technical: dict = field(default_factory=dict)

    news: dict = field(default_factory=dict)

    fundamental: dict = field(default_factory=dict)

    summary: str = ""