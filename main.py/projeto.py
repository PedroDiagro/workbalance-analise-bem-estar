import numpy as np

NUM_COLABORADORES = 5
ARQUIVO_RELATORIO = "relatorio_workbalance.txt"


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Pede um número inteiro até o usuário digitar um valor válido."""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                raise ValueError(f"o valor mínimo é {minimo}")
            if maximo is not None and valor > maximo:
                raise ValueError(f"o valor máximo é {maximo}")
            return valor
        except ValueError as e:
            print(f"Entrada inválida ({e}). Tente novamente.")


def ler_decimal(mensagem, minimo=0.0):
    """Pede um número decimal até o usuário digitar um valor válido."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < minimo:
                raise ValueError(f"o valor mínimo é {minimo}")
            return valor
        except ValueError as e:
            print(f"Entrada inválida ({e}). Tente novamente.")


def ler_texto(mensagem):
    """Pede um texto não vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Este campo não pode ficar vazio.")


def coletar_dados(quantidade=NUM_COLABORADORES):
    colaboradores = []
    for i in range(quantidade):
        print(f"\nColaborador {i + 1}:")
        colaboradores.append({
            "nome": ler_texto("Nome: "),
            "departamento": ler_texto("Departamento: "),
            "horas": ler_decimal("Horas trabalhadas no dia: "),
            "pausas": ler_inteiro("Pausas realizadas (quantidade): ", minimo=0),
            "estresse": ler_inteiro("Nível de estresse (1 a 5): ", minimo=1, maximo=5),
            "tarefas": ler_inteiro("Tarefas concluídas: ", minimo=0),
        })
    return colaboradores


def maior_estresse(lista):
    return max(lista, key=lambda c: c["estresse"])["nome"]


def colaboradores_produtivos(lista):
    return [c["nome"] for c in lista if c["tarefas"] >= 5]


def alerta_equilibrio(lista):
    return [c["nome"] for c in lista if c["estresse"] >= 4 and c["pausas"] <= 1]


def analises(lista):
    horas = np.array([c["horas"] for c in lista])
    estresse = np.array([c["estresse"] for c in lista])
    return {
        "media_horas": np.mean(horas),
        "desvio_horas": np.std(horas),
        "media_estresse": np.mean(estresse),
    }


def formatar_lista(nomes):
    return ", ".join(nomes) if nomes else "nenhum"


def montar_relatorio(lista):
    stats = analises(lista)
    linhas = [
        "RELATÓRIO WORKBALANCE",
        f"Média de horas trabalhadas: {stats['media_horas']:.1f}h",
        f"Desvio padrão de horas: {stats['desvio_horas']:.1f}",
        f"Média de estresse: {stats['media_estresse']:.1f}",
        f"Colaborador mais estressado: {maior_estresse(lista)}",
        f"Colaboradores com 5+ tarefas: {formatar_lista(colaboradores_produtivos(lista))}",
        f"Alerta de equilíbrio: {formatar_lista(alerta_equilibrio(lista))}",
    ]
    return "\n".join(linhas)


def gerar_relatorio(lista):
    relatorio = montar_relatorio(lista)
    print("\n" + relatorio)
    try:
        with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as f:
            f.write(relatorio + "\n")
        print(f"\nRelatório salvo em {ARQUIVO_RELATORIO}")
    except OSError as e:
        print(f"Erro ao salvar o arquivo: {e}")


def feedback(colaborador):
    nome = colaborador["nome"]
    if colaborador["estresse"] >= 4 and colaborador["pausas"] <= 1:
        return f"{nome}: alta carga e poucas pausas. Sugestão: reorganize suas tarefas."
    if colaborador["tarefas"] >= 5 and colaborador["estresse"] <= 3:
        return f"{nome}: ótimo desempenho! Continue equilibrando suas pausas."
    return f"{nome}: desempenho estável, mantenha o equilíbrio."


if __name__ == "__main__":
    colaboradores = coletar_dados()
    gerar_relatorio(colaboradores)

    print("\nFeedback individual:")
    for c in colaboradores:
        print(feedback(c))
