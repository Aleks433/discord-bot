import discord
from discord.ext import commands
import playsound

def play_track(track:str):
    playsound.playsound(track + '.mp3')

