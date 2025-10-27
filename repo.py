from pathlib import Path
import json, csv
from stages import Lead

class LeadRepository:
    """Classe responsável por manipular os dados dos Leads (CRUD + CSV)."""

    def __init__(self):
        self.data_dir = Path(__file__).resolve().parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self):
        """Carrega os leads do arquivo JSON."""
        if not self.db_path.exists():
            return []
        try:
            data = json.loads(self.db_path.read_text(encoding="utf-8"))
            return [Lead(**lead) for lead in data]
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        """Salva a lista de leads no JSON."""
        data = [lead.to_dict() for lead in leads]
        self.db_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def create_lead(self, lead):
        leads = self._load()
        leads.append(lead)
        self._save(leads)

    def read_leads(self):
        return self._load()

    def export_csv(self):
        """Exporta os leads para CSV."""
        path = self.data_dir / "leads.csv"
        leads = self._load()
        try:
            with path.open('w', newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["name", "company", "email", "stage", "created"])
                w.writeheader()
                for lead in leads:
                    w.writerow(lead.to_dict())
            return path
        except PermissionError:
            return None
