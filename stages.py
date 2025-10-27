from datetime import date

# Possíveis estágios do Lead
STAGES = ["novo", "em andamento", "avançado", "finalizado"]

class Lead:
    """Classe que representa um Lead (possível cliente)."""

    def __init__(self, name, company, email, stage="novo", created=None):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = created or date.today().isoformat()

    def to_dict(self):
        """Retorna os dados do lead em formato de dicionário."""
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created
        }

    def avançar_stage(self):
        """Avança o estágio do lead (novo → em andamento → avançado → finalizado)."""
        if self.stage not in STAGES:
            self.stage = "novo"
            return

        atual = STAGES.index(self.stage)
        if atual < len(STAGES) - 1:
            self.stage = STAGES[atual + 1]
        else:
            print(f"O lead '{self.name}' já está no estágio final: {self.stage}")

    def __str__(self):
        return f"{self.name} | {self.company} | {self.email} | {self.stage} | {self.created}"

class VipLead(Lead):
    def __init__(self, name, company, email, created=None):
        super().__init__(name, company, email, stage="vip", created=created)

    def __str__(self):
        return f"[VIP] {self.name} ({self.company}) - {self.email}"
