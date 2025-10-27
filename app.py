from repo import LeadRepository
from stages import Lead, VipLead

class CRMApp:
    """Classe principal do sistema Mini CRM."""

    def __init__(self):
        self.repo = LeadRepository()

    def add_lead(self):
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()

        if not name or not email or "@" not in email:
            print("Nome e e-mail válido são obrigatórios.")
            return

        lead = Lead(name, company, email)
        self.repo.create_lead(lead)
        print("Lead adicionado.")
        print(lead)

    def add_vip_lead(self):
        name = input("Nome (VIP): ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()

        if not name or not email or "@" not in email:
            print("Nome e e-mail válido são obrigatórios.")
            return

        vip = VipLead(name, company, email)
        self.repo.create_lead(vip)
        print("Lead VIP adicionado com sucesso!")
        print(vip)

    def list_leads(self):
        leads = self.repo.read_leads()
        if not leads:
            print("Nenhum lead ainda.")
            return
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in enumerate(leads):
            print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

    def search_leads(self):
        q = input("Buscar por: ").strip().lower()
        if not q:
            print("Consulta vazia.")
            return
        leads = self.repo.read_leads()
        results = []
        for i, l in enumerate(leads):
            blob = f"{l.name} {l.company} {l.email}".lower()
            if q in blob:
                results.append((i, l))
        if not results:
            print("Nada encontrado.")
            return
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in results:
            print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

    def export_leads(self):
        path = self.repo.export_csv()
        if path is None:
            print("Não consegui escrever o CSV. Feche o arquivo se estiver aberto e tente novamente.")
        else:
            print(f"Exportado para: {path}")

    def advance_lead_stage(self):
        leads = self.repo.read_leads()
        if not leads:
            print("Nenhum lead para atualizar.")
            return

        self.list_leads()
        try:
            idx = int(input("Digite o número do lead para avançar o estágio: "))
            lead = leads[idx]
            lead.avançar_stage()
            print(f"✅ Estágio de '{lead.name}' atualizado para: {lead.stage}")
            self.repo._save(leads)
        except (ValueError, IndexError):
            print("Entrada inválida.")

    def print_menu(self):
        print("[1] Adicionar lead")
        print("[2] Adicionar lead VIP")
        print("[3] Listar leads")
        print("[4] Buscar (nome/empresa/e-mail)")
        print("[5] Avançar estágio do lead")
        print("[6] Exportar CSV")
        print("[0] Sair")

    def run(self):
        while True:
            self.print_menu()
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_lead()
            elif op == "2":
                self.add_vip_lead()
            elif op == "3":
                self.list_leads()
            elif op == "4":
                self.search_leads()
            elif op == "5":
                self.advance_lead_stage()
            elif op == "6":
                self.export_leads()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    app = CRMApp()
    app.run()
