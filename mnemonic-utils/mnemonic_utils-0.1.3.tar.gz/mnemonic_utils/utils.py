import random, hashlib, binascii
from mnemonic_utils.constants import WORD2ID, WEB3


def is_valid_mnemonic(phrase):
    N = 0
    for word in phrase:
        N = (N<<11) + WORD2ID[word]
    nhex = format(N, '033x') # include leading zero if needed
    h = hashlib.sha256(binascii.unhexlify(nhex[:-1])).hexdigest()
    return h[0] == nhex[-1]


def generate_mnemonic(wordlist):
    mnemonic_init = random.sample(wordlist, 11)
    
    result = None
    for word in wordlist:
        phrase = mnemonic_init + [word]
        if is_valid_mnemonic(phrase):
            result = " ".join(phrase)

    if result is None:
        result = generate_mnemonic(wordlist)
    return result


def generate_addresses_from_mnemonic(mnemonic, N=10):
    return [WEB3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{i}").address for i in range(N)]


def generate_accounts_from_mnemonic(mnemonic, N=10):
    return [WEB3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{i}") for i in range(N)]