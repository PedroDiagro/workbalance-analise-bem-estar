Workbalance: análise de jornada e bem-estar

Script em Python que coleta dados da jornada de trabalho de colaboradores e gera um relatório com estatísticas e alertas de sobrecarga.

Projeto desenvolvido na Global Solution da FIAP (curso de Inteligência Artificial).

O que o script faz:

1- Coleta, para 5 colaboradores: nome, departamento, horas trabalhadas, pausas, nível de estresse (1 a 5) e tarefas concluídas.

2- Valida cada entrada: campos vazios, números negativos e estresse fora da faixa são recusados, e o script pede apenas aquele campo de novo.

3- Calcula com NumPy a média e o desvio padrão das horas e a média de estresse.

4- Identifica o colaborador mais estressado, quem concluiu 5 ou mais tarefas e quem está em alerta (estresse 4 ou mais com no máximo 1 pausa).

5- Mostra o relatório na tela, salva em relatorio_workbalance.txt e dá um feedback individual para cada pessoa.
