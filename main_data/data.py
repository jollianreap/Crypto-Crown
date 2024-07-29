from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

DATA = {
    "ethereum": {
        "rpc": ["https://rpc.ankr.com/eth", "https://eth-pokt.nodies.app", "https://rpc.mevblocker.io"],
        "scan": "https://etherscan.io/tx",
        "token": "ETH",
        "chain_id": 1
    },
    "optimism": {
        "rpc": ["https://rpc.ankr.com/optimism", "https://optimism-rpc.publicnode.com", "https://optimism.meowrpc.com"],
        "scan": "https://optimistic.etherscan.io/tx",
        "token": "ETH",
        "chain_id": 10
    },
    "bsc": {
        "rpc": ["https://rpc.ankr.com/bsc", "https://binance.llamarpc.com", "https://bsc-pokt.nodies.app"],
        "scan": "https://bscscan.com/tx",
        "token": "BNB",
        "chain_id": 56
    },
    "polygon": {
        "rpc": ["https://rpc.ankr.com/polygon", "https://polygon.llamarpc.com", "https://polygon.drpc.org"],
        "scan": "https://polygonscan.com/tx",
        "token": "MATIC",
        "chain_id": 137
    },
    "polygon_zkevm": {
        "rpc": ["https://zkevm-rpc.com"],
        "scan": "https://zkevm.polygonscan.com/tx",
        "token": "ETH",
        "chain_id": 1101
    },
    "arbitrum": {
        "rpc": ["https://rpc.ankr.com/arbitrum", "https://arbitrum.llamarpc.com", "https://arbitrum-one-rpc.publicnode.com"],
        "scan": "https://arbiscan.io/tx",
        "token": "ETH",
        "chain_id": 42161
    },
    "avalanche": {
        "rpc": ["https://rpc.ankr.com/avalanche", "https://avalanche-c-chain-rpc.publicnode.com", "https://avalanche.drpc.org"],
        "scan": "https://snowtrace.io/tx",
        "token": "AVAX",
        "chain_id": 43114
    },
    "fantom": {
        "rpc": ["https://rpc.ankr.com/fantom", "https://fantom.drpc.org", "https://fantom-rpc.publicnode.com"],
        "scan": "https://ftmscan.com/tx",
        "token": "FTM",
        "chain_id": 250
    },
    "nova": {
        "rpc": ["https://nova.arbitrum.io/rpc"],
        "scan": "https://nova.arbiscan.io/tx",
        "token": "ETH",
        "chain_id": 42170
    },
    "zksync": {
        "rpc": ["https://mainnet.era.zksync.io", "https://1rpc.io/zksync2-era", "https://1rpc.io/zksync2-era"],
        "scan": "https://explorer.zksync.io/tx",
        "token": "ETH",
        "chain_id": 324
    },
    "celo": {
        "rpc": ["https://1rpc.io/celo", "https://celo.drpc.org"],
        "scan": "https://celoscan.io/tx",
        "token": "CELO",
        "chain_id": 42220
    },
    "gnosis": {
        "rpc": ["https://rpc.ankr.com/gnosis", "https://1rpc.io/gnosis", "https://gnosis-rpc.publicnode.com"],
        "scan": "https://gnosisscan.io/tx",
        "token": "xDAI",
        "chain_id": 100
    },
    "core": {
        "rpc": ["https://rpc.coredao.org", "https://1rpc.io/core"],
        "scan": "https://scan.coredao.org/tx",
        "token": "CORE",
        "chain_id": 1116
    },
    "harmony": {
        "rpc": ["https://api.harmony.one", "https://1rpc.io/one" , "https://hmyone-pokt.nodies.app"],
        "scan": "https://explorer.harmony.one/tx",
        "token": "ONE",
        "chain_id": 1666600000
    },
    "moonbeam": {
        "rpc": ["https://rpc.ankr.com/moonbeam", "https://1rpc.io/glmr", "https://moonbeam-rpc.publicnode.com"],
        "scan": "https://moonscan.io/tx",
        "token": "GLMR",
        "chain_id": 1284
    },
    "moonriver": {
        "rpc": ["https://moonriver.public.blastapi.io"],
        "scan": "https://moonriver.moonscan.io/tx",
        "token": "MOVR",
        "chain_id": 1285
    },
    "linea": {
        "rpc": ["https://rpc.linea.build", "https://linea.decubate.com", "https://1rpc.io/linea"],
        "scan": "https://lineascan.build/tx",
        "token": "ETH",
        "chain_id": 59144
    },
    "base": {
        "rpc": ["https://mainnet.base.org", "https://base-pokt.nodies.app", "https://base.meowrpc.com"],
        "scan": "https://basescan.org/tx",
        "token": "ETH",
        "chain_id": 8453
    },
    "zora": {
        "rpc": ["https://zora.rpc.thirdweb.com"],
        "scan": "https://zora.superscan.network/tx",
        "token": "ETH",
        "chain_id": 7777777
    },
    "scroll": {
        "rpc": ["https://scroll.blockpi.network/v1/rpc/public", "https://1rpc.io/scroll", "https://scroll.drpc.org"],
        "scan": "https://scrollscan.com/tx",
        "token": "ETH",
        "chain_id": 534352
    },
    "metis": {
        "rpc": ["https://metis-mainnet.public.blastapi.io", "https://metis-pokt.nodies.app"],
        "scan": "https://andromeda-explorer.metis.io/tx",
        "token": "METIS",
        "chain_id": 1088
    },
    "canto": {
        "rpc": ["https://canto.slingshot.finance"],
        "scan": "https://cantoscan.com/tx",
        "token": "CANTO",
        "chain_id": 7700
    },
    "starknet": {
        "rpc": ["https://starknet-mainnet.public.blastapi.io"],
        "scan": "https://starkscan.co/tx",
        "token": "ETH",
        "chain_id": None
    },
    "mantle": {
        "rpc": ["https://1rpc.io/mantle", "https://mantle.drpc.org	"],
        "scan": "https://explorer.mantle.xyz/tx",
        "token": "MNT",
        "chain_id": 5000
    },
    "blast": {
        "rpc": ["https://blast.blockpi.network/v1/rpc/public", "https://rpc.envelop.is/blast", "https://blast-rpc.publicnode.com"],
        "scan": "https://blastscan.io/tx",
        "token": "ETH",
        "chain_id": 81457
    },
    "zeta": {
        "rpc": ["https://zetachain-evm.blockpi.network/v1/rpc/public", "https://zeta-chain.drpc.org"],
        "scan": "https://explorer.zetachain.com",
        "token": "ZETA",
        "chain_id": 7000
    },
    "mode": {
        "rpc": ["https://1rpc.io/mode"],
        "scan": "https://explorer.mode.network/tx",
        "token": "ETH",
        "chain_id": 34443
    },
    "opbnb": {
        "rpc": ["https://opbnb-rpc.publicnode.com", "https://1rpc.io/opbnb"],
        "scan": "https://opbnb.bscscan.com/tx",
        "token": "BNB",
        "chain_id": 204
    },
}

MULTICALL_ETH_CONTRACTS = {
    'ethereum': '0xb1f8e55c7f64d203c1400b9d8555d050f94adf39',
    'arbitrum': '0x151E24A486D7258dd7C33Fb67E4bB01919B7B32c',
    'bsc': '0x2352c63A83f9Fd126af8676146721Fa00924d7e4',
    'polygon': '0x2352c63A83f9Fd126af8676146721Fa00924d7e4',
    'optimism': '0xB1c568e9C3E6bdaf755A60c7418C269eb11524FC',
    'avalanche': '0xD023D153a0DFa485130ECFdE2FAA7e612EF94818',
    'fantom': '0x07f697424ABe762bB808c109860c04eA488ff92B',
    'era': '0x875fb0451fb2787b1924edc1DE4083E5f63D99Df',
    'zksync': '0x875fb0451fb2787b1924edc1DE4083E5f63D99Df',
    'nova': '0x3008e6ad64a470c47f428e73214c2f1f4e79b72d',
    'zora': '0x6830d287fE1dab06ABe252911caD71F37a0514A3',
    'linea': '0x3008e6ad64a470c47f428e73214C2F1f4e79b72d',
    'base': '0x162708433f00dbc8624795f181ec1983e418ef11',
    'polygon_zkevm': '0x162708433F00DBC8624795F181EC1983E418EF11',
    'core': '0xdAd633A2Ff9fb3Ab5d7a8bcfd089593c503c11a2',
    'gnosis': '0xd08149E71671A284e3F99b371BaF29BB8eEA7387',
    'goerli': '0x8242cd33761782f02bf10b7329cea5faf17b2bea',
    'moonbeam': '0xf614056a46e293DD701B9eCeBa5df56B354b75f9',
    'moonriver': '0xDEAa846cca7FEc9e76C8e4D56A55A75bb0973888',
    'aurora': '0x100665685d533F65bdD0BD1d65ca6387FC4F4FDB',
    'tron': 'TN8RtFXeQZyFHGmH1iiSRm5r4CRz1yWkCf',
    'celo': '0x6830d287fE1dab06ABe252911caD71F37a0514A3',
    'harmony': '0x3008e6ad64a470c47f428e73214c2f1f4e79b72d',
    'scroll': '0xD44a774539062bB4dC032df336595161c8a0CC52',
    'mantle': '0x3439cD286f92713db1d60Cf183597689eaF19117',
    'blast': '0x7ca5f6398cb59a64b4ebe61181c6045c2f15064a',
    'mode': '0xEbc45eBC6B4f74b5411771900999c51c98E5CccA',
    'zora': '0x41CD56d7A899bF9c284ca04DCb16bE0B65c74917',
    'opbnb': '0x72b3797e1edbeefcb3d8ac720b15b078d797d547',
}

contract_abi = '[{"constant":true,"inputs":[{"name":"user","type":"address"},{"name":"token","type":"address"}],"name":"tokenBalance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"users","type":"address[]"},{"name":"tokens","type":"address[]"}],"name":"balances","outputs":[{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"}]'
