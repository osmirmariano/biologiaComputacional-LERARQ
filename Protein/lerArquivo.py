# -*- coding: utf-8 -*-
import xml.etree.cElementTree as et


def lerArquivo():
    arquivoXml = et.parse('resultado.xml')
    xml = arquivoXml.getroot()
    resultadoScore = ''
    resultadoEvalue = ''
    for Hit_hsps in xml.iter('Hsp'):
        Hsp = dict((attr.tag, attr.text) for attr in Hit_hsps)
        if resultadoScore < Hsp['Hsp_score']:
            resultadoScore = Hsp['Hsp_score']

        if resultadoEvalue < Hsp['Hsp_evalue']:
            resultadoEvalue = Hsp['Hsp_evalue']
    print 'SCORE: ', resultadoScore
    print 'E-VALUE: ', resultadoEvalue 


if __name__=="__main__":
    lerArquivo()