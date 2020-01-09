cypher = 0x44724776acf176c2ee3737882236602b5edd1000ec0aa1ef99fcf2fee38c757e919a95753c55488a955e9f440060fd5d4f7f635dfe2e43d8e1de83101993c11bd19e8fd7b0536fa8695ee9f8490a3727c0297683a78452788cc2930ba0c532db67507f549b72cdafe640f6ada7486831583a6bf8760e8b201a1d90e4e8924fe1
n = 0xa46811d2199660d96f9a3544d7907b70b8b5ddaf41bd1f89b9118f822209116440387a0eacb6e94720350edee55adf7306ebd56e84afd7cf0a9329c991a1982f04bbbd04eb8978d80d0052b77995c55707c92c4a9b67ccc809383462ee879552dcabcbb8f8aac06ceea27d79a6f6b62911c335fec31eed8c29f62c07359c7671
e = 0x10001
privatekeyd = 0x81710aaedfc47d4654cf1627b88d221352eaa5bac9c86c9f539dd6de7f8ba22ccb3f6c2247abcfa9575b4ef501a17592ac1d5c32a2b78bf39000e402b6ed82d226a8532a7ec26cab28c16769fb63375b113bc4b08fda9f7bd541d2c5cadee975517321c28c4becc73885ce3a69cc998a95504b9ad3fc2fdc0730e98b55c840cd

spiderC = 0x20fc03357ed99aa3b6dcd9b6ed1070f3a01924c1bc53927542408ed6ce453310c2e0226994c9247316b22f8f9a5400a45685f7da4f7fcfaf4eee16511378e680fee6cba32444d4f7aa3252e5d4b8069937e5711e115da81af9a3814fd8acfa5e4c46073c72963f58af6b499bf5af0b1a7f113363aee699e701c409605367947e
spiderE = 0x10001
spiderD = 0x4ad2f181d34960502b42f05559317ad56986c2b1538935c7a817cedff4844dbdef95f2cb27ae4a741dd86336ef6fadce5de553ec36c0b653e631e1bfdc297369cc3e9ad7a8151ef82a46c0497a09a9fce5ee70e231aa5daa1839010e9d566a192be9f380649dffef3933cc70666014b5135cc833b499ca2bd2a686bc49fac9c1
spiderN = 0x973e1e16a298a6a43dd4def179e83bff7f5da2d103d15cee35cbed95e4cb302c521d172aa5e60a4c92fd308b7d44de1abb74a4052b48839bf3618cd10738144ec142cd372c400e1d3aaae06afb9b6f82f45f6c5da9d95b4fe7c8cf98ba592cbbcb8807bda418ced816687eae93bd6f5840bef78d608a1d06b784c5ce0648d46d



def testDecript(cyphervar, privatekey, N):
    message = pow(cyphervar, privatekey, N)
    print "*******Test Decrypt**********"
    print "here are the values: "
    print "Cypher: "+str(cyphervar)
    print "privatekey: "+str(privatekey)
    print "N: "+str(N)
    print "Message (non-hex): "+str(message)
    print("decrypted (this is the value I need): " + str(hex(message)))

    testEncrypt(message, spiderE, N)


def testEncrypt(messagevar, evar, N):
    print "lets re-encrypt"
    print "========"
    message2 = pow(messagevar, evar, N)
    print "here is the re-encrypted cypher text:"
    print hex(message2)
    testCypher(spiderC, message2)

def testCypher(cypher, messagetest):
    if cypher == messagetest:
        print "Its the same"
    else:
        exit
#spiderman's tests
testDecript(spiderC, spiderD, spiderN)

#bryces tests
print "Here are bryces values:"
testDecript(cypher, privatekeyd, n)

