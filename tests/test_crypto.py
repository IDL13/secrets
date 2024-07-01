from tooling.crypto import MD5, check

def test_crypto():
    # given  
    passphrase = "test"
    
    passphrase_test = MD5(passphrase).encrypt()

    result_test_1 = check("test", passphrase_test)
    result_test_2 = check("test2", passphrase_test)
    
    assert(True == result_test_1)
    assert(False == result_test_2)
    
    
    