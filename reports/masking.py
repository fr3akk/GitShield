def mask_secret(secret):

    if len(secret) <= 8:
        return "*" * len(secret)

    return (
        secret[:4]
        + "*" * (len(secret) - 8)
        + secret[-4:]
    )