def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    if hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!" if hey_bob.isupper() else "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."
