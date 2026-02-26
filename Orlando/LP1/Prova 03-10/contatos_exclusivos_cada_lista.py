agenda_maria = [
  ("Ana", "1111-1111"), ("Bruno", "2222-2222"), ("Carla", "3333-3333"), ("Diego", "4444-4444"), ("Elisa", "5555-5555"), ("Felipe", "6666-6666"), ("Gabriela", "7777-7777"),
  ("Henrique", "8888-8888"), ("Igor", "9999-9999"), ("Julia", "1010-1010"), ("Lucas", "1212-1212"), ("Mariana", "1313-1313"), ("Nicolas", "1414-1414"), ("Olivia", "1515-1515"),
  ("Paulo", "1616-1616"), ("Renata", "1717-1717"), ("Sofia", "1818-1818"), ("Tiago", "1919-1919"), ("Ursula", "2020-2020"), ("Victor", "2121-2121")
]

agenda_ana = [
  ("Bruno", "2222-2222"), ("Carla", "3333-3333"), ("Xavier", "2323-2323"),
  ("Yara", "2424-2424"), ("Zeca", "2525-2525"), ("Igor", "9999-9999"),
  ("Julia", "1010-1010"), ("Alice", "2626-2626"), ("Beatriz", "2727-2727"),
  ("Clara", "2828-2828"), ("Daniel", "2929-2929"), ("Elisa", "5555-5555"),
  ("Fernando", "3030-3030"), ("Gustavo", "3131-3131"), ("Helena", "3232-3232"),
  ("Isabel", "3334-3334"), ("João", "3434-3434"), ("Katia", "3535-3535"),
  ("Leonardo", "3636-3636"), ("Maria", "3737-3737")
]

agenda_beatriz = [
  ("Carla", "3333-3333"), ("Igor", "9999-9999"), ("Julia", "1010-1010"),
  ("Mariana", "1313-1313"), ("Xavier", "2323-2323"), ("Yara", "2424-2424"),
  ("Pedro", "3838-3838"), ("Rafael", "3939-3939"), ("Simone", "4040-4040"),
  ("Tereza", "4141-4141")
]

set_maria = set(agenda_maria)
set_ana = set(agenda_ana)
set_beatriz = set(agenda_beatriz)

exclusivos_maria = set_maria - set_ana - set_beatriz

exclusivos_ana = set_ana - set_maria - set_beatriz

exclusivos_beatriz = set_beatriz - set_maria - set_ana

print("--- Contagem de Contatos Exclusivos ---")
print(f"Maria tem {len(exclusivos_maria)} contato(s) exclusivo(s).")
print(f"Ana tem {len(exclusivos_ana)} contato(s) exclusivo(s).")
print(f"Beatriz tem {len(exclusivos_beatriz)} contato(s) exclusivo(s).")