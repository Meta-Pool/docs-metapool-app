---
title: NEAR Network
description: NEAR Network Smart Contracts Addresses
---

## stNEAR Token (NEP-141), Liquid staking Contract

mainne&#x74;_:_  `meta-pool.near`&#x20;

testne&#x74;_:_ stNEAR NEP-141 Token,  `meta-v2.pool.testnet`

source code: [`https://github.com/Meta-Pool/liquid-staking-contract`](https://github.com/Meta-Pool/liquid-staking-contract)

### Important Contract Methods

[get\_st\_near\_price(\&self) -> U128String](https://github.com/Narwallets/meta-pool/blob/master/metapool/src/owner.rs#L254)\
_&#x52;eturns how many near one stNEAR is worth._

Usage example, getting stNEAR price using a callback: [https://github.com/Narwallets/katherine-fundraising/blob/main/katherine-fundraising-contract/src/internal.rs#L80](https://github.com/Narwallets/katherine-fundraising/blob/main/katherine-fundraising-contract/src/internal.rs#L80)

[get\_contract\_state(\&self) -> GetContractStateResult](https://github.com/Narwallets/meta-pool/blob/master/metapool/src/owner.rs#L261)\
_&#x52;ecover multiple parameters related to metapool, including total tokens locked, available liquidity on liquidity pool, stNEAR price and close to 30 others params._

## mpDAO Governance Token:

mainnet: `mpdao-token.near`

testnet:  `mpdao-token.testnet`

## mpDAO Voting Contract:

mainnet: `mpdao-vote.near`

testnet:  `v1.mpdao-vote.testnet`

## Lockup:

`lockup-meta-pool.near`: frozen stake contract to stake `xxx.lockup.near accounts`

## (deprecated) META Governance Token:

mainnet:  `meta-token.near`

testnet:  `token.meta.pool.testnet`
