---
title: How stake distribution works
---

#### Validator statistics

The validators are tracked by an automated bot that collect statistics on each validator, several times per epoch.  You can access that information directly at [www.metapool.app/stakevote](https://www.metapool.app/stakevote).

#### Top performers and voted nodes

Each epoch, if there is NEAR to be distributed, the bot takes the top 50 performing nodes, considering the AVG APY for the best 5 of the last 7 epochs), plus voted nodes with more than 5% of the votes (if they have good performance), and that list of nodes are staked first, starting with the highest performers.

Having votes in a validator means that the assigned stake is increased, for example: if a validator  should get 20,000 NEAR because its performance, but it also has 30,000 NEAR assigned by votes, the total assigned stake for that node will be 50,000 NEAR.

Read the [vote-for-validators.md](vote-for-validators.md "mention") section to learn how to get votes if you're a validator.

The rest of the nodes (below the top 50 performers and less voted nodes) get stake if, after processing the initial list, there's more stake to distribute.&#x20;

**Remember that staking distribution is a slow process**. Moving stake from one validator to another, takes 4 epochs time, and during those 4 epochs the stake is not receiving rewards.&#x20;

#### Forced Rebalance

If there's no natural stake movement (users staking and unstaking), the automated bot rebalances between 1% and 2% of the stake every 4 epochs (it takes 4 epochs to unstake and re-stake). This rebalance ensures that the assigned stake is fulfilled in terms of performance and votes, but you must consider that if 30% of the stake is assigned by votes, and 1% is rebalanced every 4 epochs (30 hours), it could take _up to 40 days_ to fully re-balance the voted (30%) part of the stake.

#### Selection criteria

Any validator node can obtain a delegation, if it meets the following criteria:

1. Above average APY  (AVG APY is computed from the best five of the last seven epochs)
2. Up-time > 95%
3. Fees <= 10% (Note: the fee also affects the APY)
4. Staking in the validator doesn't reduce the Nakamoto Coefficient (the validator is not part of the top  concentrated set)

#### Notes:

* 30% of the Meta Pool TVL provided by users staking will be delegated by vote of DAO members
* 70% of the Meta Pool TVL is distributed by performance and programs like the node-studio
* If the TVL increases, the distributed amount increases, so the support of validators and the community is very important in order to grow the stake at Meta Pool.

