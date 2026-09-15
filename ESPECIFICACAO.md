
- o sistema deverá ter dois tipos de usuários:
    - servidor
    - aluno

- o sistema deverá permtir que servidores e alunos enviem documentos necessários para colação de grau de alunos:
    - rg
    - cpf
    - diploma de conclusão do ensino fundamental
    - histórico

- se os documentos forem aneviados por um aluno, então os mesmo deverão ser verificados e aprovados por um servidor


- dados dos registros:
    - aluno
        - nome
        - curso
        - matricula
        - turma

    - servidor
        - nome
        - matricula/código

    - arquivos
        - aluno
        - tipo
            - rg
            - cpf
            - diploma de conclusão do ensino fundamental
            - histórico
        - status
            - aguardando validação/verificação
            - validado/aprovado
        - data de envio
        - data de aprovacao
        - aprovado por quem
