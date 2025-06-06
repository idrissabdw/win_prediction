import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from dotenv import load_dotenv
import os

# API Key setting
load_dotenv("api.env")
API_KEY = os.getenv("API_KEY")
headers = {"X-Riot-Token": API_KEY}

