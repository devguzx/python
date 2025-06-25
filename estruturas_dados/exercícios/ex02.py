#Exercícios 02: Análise de Dados de Notas

qtd_alunos=int(input("Informe a quantidade de alunos: "))


media_alunos=[]
for i in range(qtd_alunos):
   
    medias={}
    nome = input("Digite o nome do aluno: ").strip()
    nota1 = float(input("Digite a 1o nota do aluno: "))
    nota2 = float(input("Digite a 2o nota do aluno: "))

    media=(nota1+nota2)/2
    medias["nome"]=nome
    medias["media"]=media

    media_alunos.append(medias)

    print(f"\nDados cadastrados:")
    print(f"Nome: {nome}")
    print(f"Notas: {nota1} e {nota2}")
    print(f"Média calculada: {media}\n")


#Média de cada aluno
for media in media_alunos:
    print(f"Média do(a) aluno(a) {media['nome']}: {media['media']}")

#Calculando a média geral da turma
media_auxiliar=[media["media"] for media in media_alunos]
media_geral=sum(media_auxiliar)/len(media_auxiliar)

alunos_acima_media=[aluno["nome"] for aluno in media_alunos if aluno["media"]>=media_geral]
print(f"Aluno(s) com média acima de {media_geral}: {', '.join(alunos_acima_media)}")

#Alunos com maior e menor média
media_max=max(media_auxiliar)
media_min=min(media_auxiliar)

maior_media=[media["nome"] for media in media_alunos if media["media"]==media_max]
menor_media=[media["nome"] for media in media_alunos if media["media"]==media_min]

print(f"""
Maior média = {media_max} 
Aluno(s) com a maior média: {', '.join(maior_media)}

Menor média = {media_min}
Aluno(s) com a menor média: {', '.join(menor_media)}
""")





















