from browser import document, alert
from FingerCipher import encrypt, decrypt
from FingerCipher import *
def encr(event):
    if set(deftable) != set(document["alpha"].value):
        document["alphaError"].innerHTML = "Make sure to include exactly 100 characters, including the ones you use."
    try:
        document["eresult"].innerHTML = encrypt(document["ezone"].value,document["ezone2"].value,document["alpha"].value)
    except ValueError:
        document["eresult"].innerHTML = "There seems to be a problem with your alphabet."
document["ebutton"].bind("click", encr)
def decr(event):
    try:
        document["dresult"].innerHTML = decrypt(document["dzone"].value,document["dzone2"].value,document["alpha"].value)
    except ValueError:
        document["dresult"].innerHTML = "There seems to be a problem with your alphabet."
document["dbutton"].bind("click", decr)
document["alpha"].innerHTML = ''.join(deftable)
def resetAlph(event):
    document["alpha"].value = ''.join(deftable)
document["resetTable"].bind("click", resetAlph)

