from typing import Union

from pyrage import plugin, ssh, x25519

__all__ = ("Identity", "Recipient")

Identity = Union[ssh.Identity, x25519.Identity, plugin.IdentityPluginV1]
Recipient = Union[ssh.Recipient, x25519.Recipient, plugin.RecipientPluginV1]
