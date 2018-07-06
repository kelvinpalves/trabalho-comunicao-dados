import numpy
import matplotlib
import matplotlib.pyplot as grafico
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-t", "--text", dest="entradaTexto")
parser.add_argument("-f", "--frequencia", dest="frequencia")
parser.add_argument("-d", "--debug", dest="modoDebug", default=False)

args = parser.parse_args()

FILE_ASK     = 'tmp/grafico-ask.png'
FILE_NRZ     = 'tmp/grafico-nrz.png'
FILE_FFT     = 'tmp/grafico-fft.png'
FILE_IFFT    = 'tmp/grafico-ifft.png'
entradaTexto = args.entradaTexto
frequencia   = float(args.frequencia)
modoDebug    = args.modoDebug

binarioTexto = ' '.join(bin(ord(x))[2:].zfill(8) for x in entradaTexto)

binarioTextoAuxiliar = binarioTexto.replace(' ', '')

listaBits = []
for caracter in binarioTextoAuxiliar:
    listaBits.append(int(caracter))
    
if modoDebug:
    print 'Entrada............:', entradaTexto
    print 'Frequencia.........:', frequencia
    print 'Binario Texto......:', binarioTexto
    print 'Lista Bits.........:', listaBits

listaEixoX = list(numpy.repeat(range(len(listaBits)+1), 2))
listaEixoX = listaEixoX[1:]
listaNRZ   = []

for bit in listaBits:
    listaNRZ.append(1 if bit == 0 else -1)

listaEixoY       = list(numpy.repeat(listaNRZ, 2))
ultimoValorEixoY = listaEixoY[len(listaEixoY) - 1]
listaEixoY.append(1 if ultimoValorEixoY else 0)

if modoDebug:
    print 'Eixo X.............:', listaEixoX
    print 'Eixo Y.............:', listaEixoY
    print 'NRZ................:', listaNRZ

imagem = grafico.figure(figsize=(8, 2.5)) 

grafico.ylim(-2, 2)
grafico.plot(listaEixoX, listaEixoY)

imagem.savefig(FILE_NRZ)

for index in range(0, len(listaNRZ)):
    if (listaNRZ[index] == -1):
        listaNRZ[index] = 0

dimensao = 16 if len(listaBits) == 8 else len(listaNRZ)

listaASK = []

for bit in listaNRZ:
    listaASK = numpy.concatenate((listaASK, (numpy.ones(dimensao) * bit)))

dimensaoAuxiliar = len(listaASK)
listaTempo = numpy.linspace(0, len(listaNRZ), dimensaoAuxiliar)

if modoDebug:
    print 'Lista Bits - TEMPO: ', listaTempo

sinal = 2 * numpy.pi * frequencia * listaTempo
listaSinal = numpy.sin(sinal)

if modoDebug:
    print 'Sinal', listaSinal

sinalFinal = (listaASK * listaSinal)

imagem = grafico.figure(figsize=(8, 2.5)) 

grafico.ylim(-2, 2)
grafico.plot(listaTempo, sinalFinal)

imagem.savefig(FILE_ASK)

fft             = numpy.fft.fft(sinalFinal)
dimensaoSinal   = len(sinalFinal)
auxiliar        = dimensaoSinal / dimensao
listaFrequencia = numpy.arange(dimensaoSinal) / auxiliar
listaFFT        = fft / dimensaoSinal

imagem = grafico.figure(figsize=(8, 2.5)) 

grafico.plot(listaFrequencia,listaFFT.real)

imagem.savefig(FILE_FFT)

demodulacao = numpy.fft.ifft(fft)

imagem = grafico.figure(figsize=(8, 2.5)) 

grafico.plot(listaTempo, demodulacao.real)

imagem.savefig(FILE_IFFT)

inversor = (listaASK / demodulacao)

sinalChegada = []

salto = int(numpy.sqrt(len(demodulacao)))

if (len(listaBits) == 8):
    salto = dimensao

for i in range(0,len(demodulacao), salto):
    if inversor[i] > 0:
        sinalChegada.append(1)
    if inversor[i] < 0:
        sinalChegada.append(1)
    if inversor[i] == 0:
        sinalChegada.append(0)

for i in range(0,len(sinalChegada)):
    if(sinalChegada[i]==0):
        sinalChegada[i]=1
    else:
        sinalChegada[i]=0
        
aux=''
for i in range(0,len(sinalChegada)):
    aux=aux+str(sinalChegada[i])

xmin = 0 
xmax = 8
listaAuxiliar = []
for i in range(0, (len(aux)/8)):
    listaAuxiliar.append(aux[xmin:xmax])
    xmin = xmin + 8
    xmax = xmax + 8

mensagem=''
for i in range(0,len(listaAuxiliar)):
    mensagem=mensagem+(unichr(int(listaAuxiliar[i],2)))

print 'Mensagem recebida: ', mensagem