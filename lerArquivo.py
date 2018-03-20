# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def lerArquivo():
    arquivo = open('/home/osmir/Imagens/ncbi-blast-2.7.1+/bin/respostaExecucao.xml')
    ler = arquivo.read()
    
    arquivoXml = ET.parse('/home/osmir/Imagens/ncbi-blast-2.7.1+/bin/respostaExecucao.xml')
    xml = arquivoXml.getroot()
    print(arquivoXml)

    for Hit_hsps in xml.iter('Hit_hsps'):
        print ('Entrou')
        #score = int(Hit_hsps.find('Hsp_score').text)
        #lerT =  int(Hsp_score.text)
        #print(score)
        # Hsp_score = Hit_hsps.find('Hsp_score').text
        # Hsp_evalue = Hit_hsps.find('Hsp_evalue')
        #print Hsp_score, Hsp_evalue

    arquivo.close()
    


if __name__=="__main__":
    lerArquivo()