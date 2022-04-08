from numpy.core.fromnumeric import mean
from modules.conector import Interface_db
import numpy as np
from datetime import datetime as dt

dt.now()
conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "netflix")
dados = conexao.selecionar("SELECT * FROM vendas")
test = np.asarray(dados)
print("media", test[2][3])