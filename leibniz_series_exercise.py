def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        if (i % 2) == 0:
            leibniz_series.append(1 / ((i * 2) + 1))
        else: 
            leibniz_series.append(-1 / ((i * 2) + 1))
    leibniz_series_sum = sum(leibniz_series)
    approximate_pi = leibniz_series_sum * 4 
    return approximate_pi
