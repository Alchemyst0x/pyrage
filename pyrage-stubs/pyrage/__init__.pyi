from io import BufferedIOBase
from typing import Sequence, Union

from pyrage import passphrase, plugin, ssh, x25519

__all__ = (
    "ssh",
    "x25519",
    "passphrase",
    "plugin",
    "Identity",
    "Recipient",
    "encrypt",
    "encrypt_file",
    "encrypt_io",
    "decrypt",
    "decrypt_file",
    "decrypt_io",
    "RecipientError",
    "IdentityError",
)

Identity: Union[ssh.Identity, x25519.Identity, plugin.IdentityPluginV1]
Recipient: Union[ssh.Recipient, x25519.Recipient, plugin.RecipientPluginV1]

class RecipientError(Exception): ...
class IdentityError(Exception): ...

def encrypt(
    plaintext: bytes,
    recipients: Sequence[
        Union[ssh.Recipient, x25519.Recipient, plugin.RecipientPluginV1]
    ],
) -> bytes: ...
def encrypt_file(
    infile: str,
    outfile: str,
    recipients: Sequence[
        Union[ssh.Recipient, x25519.Recipient, plugin.RecipientPluginV1]
    ],
) -> None: ...
def encrypt_io(
    in_io: BufferedIOBase,
    recipients: Sequence[
        Union[ssh.Recipient, x25519.Recipient, plugin.RecipientPluginV1]
    ],
) -> bytes: ...
def decrypt(
    ciphertext: bytes,
    identities: Sequence[Union[ssh.Identity, x25519.Identity, plugin.IdentityPluginV1]],
) -> bytes: ...
def decrypt_file(
    infile: str,
    outfile: str,
    identities: Sequence[Union[ssh.Identity, x25519.Identity, plugin.IdentityPluginV1]],
) -> None: ...
def decrypt_io(
    in_io: BufferedIOBase,
    out_io: BufferedIOBase,
    recipient: Sequence[Union[ssh.Identity, x25519.Identity, plugin.IdentityPluginV1]],
) -> None: ...
