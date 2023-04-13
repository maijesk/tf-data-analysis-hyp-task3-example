import pandas as pd
import numpy as np
from statsmodels. stats.weightstats import ztest as ztest


chat_id = 763683015 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.02
    z, pvalue = ztest(x,  value=500, alternative='smaller')
    return pvalue < alpha
