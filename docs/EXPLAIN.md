# PyCrypto Explanation [Back](index.md)

## How does it works

**First it will generate two pairs of key and save public key in server and save private key in file system. If you lost your key, you can't restore your message.**

Behind the scene it uses the RSA module. When you send message to someone it will collect the person's public key from server. When it get the key it will encrypt the data with the key. After this only private key holder can decrypt the message.
