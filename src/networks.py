# Main network and testnet3 definitions

# AXE src/chainparams.cpp
params = {
    'axe_main': {
        'pubkey_address': 55, #L120
        'script_address': 16, #L122
        'genesis_hash': '00000c33631ca6f2f61368991ce2dc03306b5bb50bf7cede5cfbba6db38e52e6' #L110
    },
    'axe_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #L210
    }
}
