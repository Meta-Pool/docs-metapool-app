---
title: spETH
description: Start earning ETH with Meta Pool  Liquid Staking.
---

spETH Liquid Staking solution is designed to provide a passive income to holders within the Ethereum ecosystem. Stake $ETH for rewards and still have access to your assets with a liquid staking token from Meta Pool.

This innovative solution enhances the functionality of the $ETH token by offering a staking service that allows users to earn rewards while their tokens remain liquid and accessible.

## What is $spETH?

spETH is a yield bearing asset, **accruing in value every second** meaning that you keep earning staking rewards, while you can use spETH for DeFi (coming soon) on Ethereum Network.

<figure><img src="/assets/imagen%20%28132%29.png" alt=""><figcaption></figcaption></figure>

### Benefit of Liquid staking with Meta Pool in ETH

* **spETH accruing in value every second.**&#x20;
* Liquid staking in Meta Pool allows users to stake small amounts of ETH (min. 0.01 ETH) instead of requiring 32 ETH which is needed to run a validator node on the Ethereum Network.
* Ethereum's staking rewards primarily come from two sources: **Block Rewards + Transaction Fees.**
* Fast Unstake. When you stake with Meta Pool you have the option to **access ETH immediately** (Liquid Unstaking) by paying a small fee (starting at 0.25%)

## Liquidity Pool (LP)

For the purpose of enabling fast unstaking for spETH holders, Meta Pool includes an spETH / ETH liquidity pool.

Users providing liquidity to the spETH<_>ETH_ liquidity pool can earn fees on each fast unstake.

The spETH<_>ETH_ Liquidity Pool is a single token AMM. Liquidity providers add only ETH to the liquidity pool.&#x20;

The pool allows other users to perform "Fast Unstakes". During a "Fast Unstake" users send spETH and receive ETH from the liquidity pool, minus a fee.&#x20;

## True price

All spETH is backed by staked ETH in validators. The protocol is sound in the sense that it can be wind down, meaning all spETH can be burned, validators shut down and the recovered ETH + rewards will be made available to the original spETH owners.&#x20;

Considering that all spETH is fully backed by ETH, there's a "true price" for spETH and that's the share price of the ERC-4626 standard the Meta Pool contract implements.

If you need to obtain the true price for spETH/ETH, you need to call the ERC-4626 standard function \`convertToAssets(1000000000000000000)\` [https://etherscan.io/address/0xD06f6a56c5f599cB375B616DF306f32B7F6f4A0E#readProxyContract#F13](https://etherscan.io/address/0xD06f6a56c5f599cB375B616DF306f32B7F6f4A0E#readProxyContract#F13)

This true price is the one used at all times, in fast-unstake operations and also in delayed-unstake operations.

## Delayed Unstake

Delayed unstake operations have no fee, thus honoring the true price, but since it could be required to exit validators in order to make the ETH available, a delayed unstake operation may require from 7 to 14 days in order to be completed
