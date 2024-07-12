import os.path

MAX_GAS_CHARGE = {
    'avalanche'     : 1,
    'polygon'       : 0.5,
    'ethereum'      : 7,
    'bsc'           : 0.3,
    'arbitrum'      : 3,
    'optimism'      : 1.5,
    'fantom'        : 0.5,
    'zksync'        : 1,
    'nova'          : 0.1,
    'gnosis'        : 0.1,
    'celo'          : 0.1,
    'polygon_zkevm' : 0.5,
    'core'          : 0.1,
    'harmony'       : 0.1,
    'base'          : 0.5,
    'scroll'        : 0.5,
    'zora'          : 0.5,
    'moonbeam'      : 0.5,
    'moonriver'     : 0.5,
    'canto'         : 0.5,
    'metis'         : 0.5,
    'linea'         : 0.5,
    'mantle'        : 0.5,
    'zeta'          : 0.5,
    'blast'         : 0.5,
    'mode'          : 0.5,
    'opbnb'        : 0.5
}

MAINNET_RPC_URLS = [
    "https://cloudflare-eth.com",
    "https://bsc-dataseed1.binance.org",
    "https://rpc.mainnet.taiko.xyz",
    "https://linea.decubate.com",
    "https://mainnet.mode.network",
    "https://rpc.ftm.tools",
    "https://polygon-rpc.com",
    "https://evm.kava.io",
    "https://api.evm.eosnetwork.com",
    "https://rpc.mantle.xyz",
    "https://zetachain-evm.blockpi.network/v1/rpc/public",
    "https://rpc.taprootchain.io",
    "https://rpc.merlinchain.io/",
    "https://rpc.chiliz.com",
    "https://api.node.glif.io",
    "https://rpc-core.icecreamswap.com",
    "https://rpc.bsquared.network/",
    "https://rpc.ankr.com/avalanche",
    "https://cronos-rpc.elk.finance/",
    "https://mainnet.optimism.io",
    "https://gnosis.drpc.org",
    "https://mainnet.ethereumpow.org",
    "https://http-mainnet.hecochain.com",
    "https://kcc-rpc.com",
    "https://public-en-cypress.klaytn.net",
    "https://rpc-mainnet-2.bevm.io",
    "https://rpc.zkfair.io",
    "https://evm.confluxrpc.com"
]

LAYER2_RPC_URLS = [
    "https://rpc.ankr.com/arbitrum",
    "https://mainnet.era.zksync.io",
    "https://zkevm-rpc.com",
    "https://rpc.blast.io",
    "https://mainnet-rpc.scroll.io",
    "https://xlayerrpc.okx.com",
    "https://mainnet.base.org",
    "https://opbnb-mainnet-rpc.bnbchain.org"
]

NONEVM_RPC_URLS = [
    "https://fullnode.mainnet.sui.io:443",
    "https://api.trongrid.io",
    "https://mainnet-beta.solflare.network/"
]

ROOT_PATH = 'path_to_ur_root'

class Value_EVM_Balance_Checker:

    '''
    Coins checker
    Chains : ethereum | optimism | bsc | polygon | arbitrum | avalanche | fantom | nova | zksync | polygon_zkevm | celo | gnosis | core | harmony | linea | base
    '''

    # Comment out the chain / token if you do not want to check the balance of that chain / token
    evm_tokens = {
        'bsc': [
            '', # BNB
            '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d', # USDC
            '0x55d398326f99059ff775485246999027b3197955', # USDT
            # '0xe9e7cea3dedca5984780bafc599bd69add087d56', # BUSD
            # '0xB0b84D294e0C75A6abe60171b70edEb2EFd14A1B', # SnBNB
            ],
        'arbitrum': [
            '', # ETH
            '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9', # USDT
            '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8', # USDC
            # '0x6694340fc020c5e6b96567843da2df01b2ce1eb6', # STG
            # '0x912ce59144191c1204e64559fe8253a0e49e6548', # ARB
            ],
        'optimism': [
            '', # ETH
            '0x7f5c764cbc14f9669b88837ca1490cca17c31607', # USDC
            '0x4200000000000000000000000000000000000042', # OP
            '0x94b008aa00579c1307b0ef2c499ad98a8ce58e58', # USDT
            ],
        'polygon': [
            '', # MATIC
            '0xc2132d05d31c914a87c6611c10748aeb04b58e8f', # USDT
            '0x2791bca1f2de4661ed88a30c99a7a9449aa84174', # USDC
            ],
        'avalanche': [
            '', # AVAX
            '0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7', # USDT
            ],
        'ethereum': [
            '', # ETH
            '0xdac17f958d2ee523a2206206994597c13d831ec7', # USDT
            '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', # USDC
            # '0xaf5191b0de278c7286d6c7cc6ab6bb8a73ba2cd6', # STG
            # '0xb131f4a55907b10d1f0a50d8ab8fa09ec342cd74', # MEME
            ],
        # 'zksync': [
        #     '', # ETH
        #     ],
        # 'nova': [
        #     '', # ETH
        #     ],
        # 'fantom': [
        #     '', # FTM
        #     ],
        # 'polygon_zkevm': [
        #     '', # ETH
        #     ],
        # 'celo': [
        #     '', # CELO
        #     ],
        # 'gnosis': [
        #     '', # xDAI
        #     ],
        # 'harmony': [
        #     '', # ONE
        #     ],
        # 'core': [
        #     '', # CORE
        #     ],
        # 'linea': [
        #     '', # ETH
        #     ],
        # 'base': [
        #     '', # ETH
        #     ],
        # 'scroll': [
        #     '', # ETH
        #     ],
        # 'mantle': [
        # '', # MNT
        # ],
        # 'blast': [
        #     '', # ETH
        #     ],
        # 'mode': [
        #     '', # ETH
        #     ],
        # 'zora': [
        #     '', # ETH
        #     ],
        # 'opbnb': [
        #     '', # BNB
        #     ],
    }

    min_token_balance = {
        'chain'     : 'avalanche',
        'coin'      : 'AVAX',
        'amount'    : 0.02 # If the balance is less than this amount, the wallet will be highlighted
    }

    min_value_balance = 0 # If the wallet balance in $ is less than this amount, the wallet will be highlighted