import numpy as np


def initialiser(cachee=0, graine=42):
    rng = np.random.default_rng(graine)
    if cachee == 0:
        return {"W": rng.normal(0, 0.01, (64, 10)), "b": np.zeros(10)}
    return {
        "W1": rng.normal(0, np.sqrt(2 / 64), (64, cachee)),
        "b1": np.zeros(cachee),
        "W2": rng.normal(0, np.sqrt(2 / cachee), (cachee, 10)),
        "b2": np.zeros(10),
    }


def softmax(scores):
    decales = scores - scores.max(axis=1, keepdims=True)
    e = np.exp(decales)
    return e / e.sum(axis=1, keepdims=True)


def passage(X, p):
    if "W" in p:
        return X @ p["W"] + p["b"], None
    h = np.maximum(0, X @ p["W1"] + p["b1"])
    return h @ p["W2"] + p["b2"], h


def probabilites(X, p):
    scores, _ = passage(X, p)
    return softmax(scores)


def perte_gradient(X, y, p):
    scores, h = passage(X, p)
    decales = scores - scores.max(axis=1, keepdims=True)
    log_p = decales - np.log(np.exp(decales).sum(axis=1, keepdims=True))
    perte = -log_p[np.arange(len(y)), y].mean()
    d = np.exp(log_p)
    d[np.arange(len(y)), y] -= 1
    d /= len(y)
    if h is None:
        gradients = {"W": X.T @ d, "b": d.sum(axis=0)}
    else:
        dh = (d @ p["W2"].T) * (h > 0)
        gradients = {"W1": X.T @ dh, "b1": dh.sum(axis=0),
                     "W2": h.T @ d, "b2": d.sum(axis=0)}
    return float(perte), gradients


def bilan(X, y, p):
    perte, _ = perte_gradient(X, y, p)
    exactitude = np.mean(probabilites(X, p).argmax(axis=1) == y)
    return perte, float(exactitude)
