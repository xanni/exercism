def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    shouted = hey_bob.isupper()
    if hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!" if shouted else "Sure."

    if shouted:
        return "Whoa, chill out!"

    return "Whatever."
