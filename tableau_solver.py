class LogicTree:
    def __init__(self, proposition):
        self.proposition = proposition.strip()
        self.children = []

    def decompose(self):
        # Controllo semplice per evitare decomposizioni non necessarie
        if '->' in self.proposition:
            a, b = self.proposition.split('->', 1)
            # L'implicazione A -> B è equivalente a ¬A ∨ B
            new_prop = f"¬({a.strip()}) ∨ ({b.strip()})"
            self.children.append(LogicTree(new_prop))
        elif '∨' in self.proposition:
            # Assume che ci sia un solo ∨ al livello più esterno (esempi più complessi richiederebbero un parsing più sofisticato)
            a, b = self.proposition.split('∨', 1)
            self.children.append(LogicTree(a.strip()))
            self.children.append(LogicTree(b.strip()))
        elif '∧' in self.proposition:
            # Assume che ci sia un solo ∧ al livello più esterno
            a, b = self.proposition.split('∧', 1)
            self.children.append(LogicTree(f"({a.strip()})"))
            self.children.append(LogicTree(f"({b.strip()})"))
        elif self.proposition.startswith('¬(¬'):
            # Gestisce la doppia negazione
            self.children.append(LogicTree(self.proposition[3:-1].strip()))

    def generate_tree(self):
        self.decompose()
        for child in self.children:
            child.generate_tree()

    def print_tree(self, level=0):
        indent = '   ' * level
        print(f'{indent}{self.proposition}')
        for child in self.children:
            child.print_tree(level + 1)

# Esempio di utilizzo
if __name__ == "__main__":
    proposition = "(A ∨ B) -> B"
    logic_tree = LogicTree(proposition)
    logic_tree.generate_tree()
    print("Albero logico (Tableau):")
    logic_tree.print_tree()
