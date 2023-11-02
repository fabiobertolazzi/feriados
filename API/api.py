#Crie uma api que retorne os feriados do ano
import requests
import json
from datetime import date
from datetime import timedelta
from datetime import datetime
import pandas as pd

def get_feriados(ano):
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    response = requests.get(url)
    feriados = json.loads(response.text)
    return feriados

def get_feriados_ano(ano):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'diaSemana'])
    return df

def get_feriados_mes(ano, mes):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['diaSemana'])
    df = df[df['mes'] == mes]
    return df

def get_feriados_dia(ano, mes, dia):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['diaSemana'])
    df = df[(df['mes'] == mes) & (df['dia'] == dia)]
    return df

def get_feriados_semana(ano, mes, dia):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['diaSemana'] == dia]
    return df

def get_feriados_proximo(ano, mes, dia):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['diaSemana'] == dia]
    df = df.sort_values(by=['dia'])
    df = df.reset_index(drop=True)
    proximo = df.loc[0, 'dia']
    proximo = datetime(ano, mes, proximo)
    proximo = proximo + timedelta(days=1)
    proximo = proximo.strftime("%d/%m/%Y")
    return proximo

def get_feriados_anterior(ano, mes, dia):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['diaSemana'] == dia]
    df = df.sort_values(by=['dia'])
    df = df.reset_index(drop=True)
    anterior = df.loc[0, 'dia']
    anterior = datetime(ano, mes, anterior)
    anterior = anterior - timedelta(days=1)
    anterior = anterior.strftime("%d/%m/%Y")
    return anterior

def get_feriados_proximos(ano, mes, dia):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['diaSemana'] == dia]
    df = df.sort_values(by=['dia'])
    df = df.reset_index(drop=True)
    proximos = df.loc[0, 'dia']
    proximos = datetime(ano, mes, proximos)
    proximos = proximos + timedelta(days=7)
    proximos = proximos.strftime("%d/%m/%Y")
    return proximos

def get_feriados_anteriores(ano, mes, dia):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['diaSemana'] == dia]
    df = df.sort_values(by=['dia'])
    df = df.reset_index(drop=True)
    anteriores = df.loc[0, 'dia']
    anteriores = datetime(ano, mes, anteriores)
    anteriores = anteriores - timedelta(days=7)
    anteriores = anteriores.strftime("%d/%m/%Y")
    return anteriores

def get_feriados_proximos_mes(ano, mes):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['mes'] == mes]
    df = df.sort_values(by=['dia'])
    df = df.reset_index(drop=True)
    proximos = df.loc[0, 'dia']
    proximos = datetime(ano, mes, proximos)
    proximos = proximos + timedelta(days=7)
    proximos = proximos.strftime("%d/%m/%Y")
    return proximos

def get_feriados_anteriores_mes(ano, mes):
    feriados = get_feriados(ano)
    df = pd.DataFrame(feriados)
    df = df.drop(columns=['mes', 'dia'])
    df = df[df['mes'] == mes]
    df = df.sort_values(by=['dia'])
    df = df.reset_index(drop=True)
    anteriores = df.loc[0, 'dia']
    anteriores = datetime(ano, mes, anteriores)
    anteriores = anteriores - timedelta(days=7)
    anteriores = anteriores.strftime("%d/%m/%Y")
    return anteriores