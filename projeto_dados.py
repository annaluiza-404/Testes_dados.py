import pandas as pd

#importando a base de dados - com extensão csv
tabela=pd.read_csv("student_exam_scores.csv")

#calcula a media de horas dormidas,horas estudadas, nota dos exames - respectivamente
media_dormir=tabela['sleep_hours'].mean()
print(f'Média das horas dormidas:{media_dormir}')

horas_estudos=tabela['hours_studied'].mean()
print(f'Média das horas estudadas:{horas_estudos}')

nota_exame=tabela['exam_score'].mean()
print(f'Média das notas dos exames:{nota_exame}')


#analisar as três juntas, comparar e formular uma hipótese
comparar=tabela[['hours_studied','sleep_hours','exam_score']].groupby(['hours_studied','sleep_hours']).sum()
print(comparar)


tabela.plot(kind='bar')


#os estudantes que estudaram mais horas, dormiram em uma média de 6 a 7 horas, tiveram uma nota melhor na prova



























#pega a linha sobre o estudante de id S003 e mostra aquelas duas colunas
#print(tabela_aluno.loc[tabela_aluno['student_id']=='S003', ['hours_studied','sleep_hours']])
