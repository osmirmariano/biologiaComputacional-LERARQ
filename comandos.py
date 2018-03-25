#Comando para compilar Proteina
#Comando para gerar o banco de dados
makeblastdb -dbtype prot -in protein.fa -out bancodados_db
#Comando para gerar a saida xml
blastp -query sequencia.fa -db bancodados_db -outfmt 5 > resultado.xml

#Comando para compilar nucleotideos
makeblastdb -dbtype nucl -in nucleotide.fa -out bancodados_db
#Comando para gerar a saida xml
blastn -query sequencia.fa -db bancodados_db -outfmt 5 > resultado.xml