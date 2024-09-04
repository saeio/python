nome = input("qm é tu")
print(f"{nome}, tu quer faze oq? sair de casa ou ir dormir:")
resp = input()
if resp == "sair de casa" :
    print(f"{nome} saiu de casa.")
    q = input("agora tu quer fazer oq? ir pro parque ou pra lanchonete?")
    if q == "ir pro parque":
        print(f"{nome} foi pro parque e descansou")
    elif q == "ir pra lanchonete" or "pra lanchonete":
        print(f"{nome} foi pra lanconete come uns xtudo")
        print("tu comeu quantos?")
        quantos = input()
        print(f"carai, {quantos} xtudokkkkkkkkkkkkkkkk")
elif resp == "ir dormir":
    print(f"{nome} foi dormir.")
