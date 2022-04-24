# orbitdb_ipfs_pubsub_poc_client_service
Proof of concept client side service. Regularly checks orbitdb instance for new hashes to pin.

the only non-standard library module this app requires is requests:
python -m pip install requests

you'll also need an ipfs node installed somewhere you can call to it

the code will need to be edited to ensure that the requests point to the orbitdb instance and to your ipfs node. 
comments in the code indicate where those changes need to be made.
