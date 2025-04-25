from get_taas import get_taas # type: ignore


dast = 0
for taas in get_taas():
    print(taas)
    if dast > 5:
        break
    else:
        dast += 1