---
title: Liquidity
---

## Liquidity Pool and Liquidity Providers

<details>

<summary>What is Meta Pool liquidity pool (LP)?</summary>

A liquidity pool (LP) is a collection of funds locked in a smart contract. Meta Pool liquidity pool works for swapping:&#x20;

* stNEAR tokens to $NEAR
* stAUR tokens to $AURORA
* spETH tokens to $ETH

LP tokens represent the user's share of the total amount of locked liquidity in several tokens (usually two tokens), in liquidity pool on the Meta Pool platform.

</details>

<details>

<summary>How to provide liquidity?</summary>

Here is the tutorial [Liquidity](https://app.gitbook.com/o/-MklhgqOoctfcpHIH9zW/s/5HvxIwoS8YhIHItpA1lt/~/changes/17/meta-pool-ecosystem/liquidity) step by step on how to do it.

</details>

<details>

<summary>What are the benefits of being a liquidity provider?</summary>

Being a liquidity provider in Meta Pool you will receive a % of the payed liquidity fees.

The liquidity provider gets reward every liquid-unstake operation. The APY is fully based on liquid-unstake fees.

Calm market, no operations => 0 fee, 0% APY;\
Active market => lot of fees, high APY.

Note: LP APY can be high if the LP pool is depleted, so you may see a similarly high commission up to 3%. Liquid unstake fee is 0,3%-1.5% are normal.

</details>

<details>

<summary>What is the liquidity fee?</summary>

The liquidity fee is the commission that you pay to swap tokens when unstaking.

* $stNEAR to $NEAR&#x20;
* $stAUR to $AURORA
* $spETH to $ETH

</details>

<details>

<summary>How is the liquidity fee calculated?</summary>

Meta Pool liquidity fee is in a range from:

* $spETH to $ETH: 0.3% to 5%
* $stAUR to $AURORA: 2%
* $stNEAR to $NEAR: from 0.3% to 3%

It varies linearly according to the quantity of liquidity available in Meta Pool liquidity pool (LP).&#x20;

</details>

<details>

<summary>How is the APY for liquidity providers calculated?</summary>

1. We take the LP price measure in NEAR/AURORA/ETH from 7 days ago, and the LP price now.
2. Divide /7 to get a day-to-day increase.
3. Multiply by 365 to annualize, compute the price in a year if the current trend is maintained.
4. Compute APY based on current price vs price in a year.

</details>

<details>

<summary>Who can be a liquidity provider?</summary>

Anyone who provides $NEAR/$AURORA/$ETH tokens to Meta Pool for allowing liquid unstake be done.

[Liquidity](https://app.gitbook.com/o/-MklhgqOoctfcpHIH9zW/s/5HvxIwoS8YhIHItpA1lt/~/changes/17/meta-pool-ecosystem/liquidity)

</details>

<details>

<summary>How can I become a liquidity provider?</summary>

Anyone can be a liquidity provider in Meta Pool, you just need to go to [Meta Pool App](https://www.metapool.app/liquidity) and go to Liquidity section and click to add liquidity.

[Liquidity](https://app.gitbook.com/o/-MklhgqOoctfcpHIH9zW/s/5HvxIwoS8YhIHItpA1lt/~/changes/17/meta-pool-ecosystem/liquidity)

</details>

[liquidity.md](../../meta-pool-ecosystem/liquidity.md)
