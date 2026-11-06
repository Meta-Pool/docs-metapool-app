---
title: Vote for Validators
description: Solve your doubts on how The Vote for Validators works.
---

<details>

<summary>What percentage of the TVL does Meta Staking Vote delegates?</summary>

By decision of the DAO ([MPIP-0](https://near.org/meta-pool-official.near/widget/ImprovementProposals?tab=proposal\&mpip_id=0)) the bot distrbutes 25% of the TVL staked by users to distribute according to DAO member voting at [Validators](https://www.metapool.app/stakevote).

</details>

<details>

<summary>How does Meta Pool delegate by performance?</summary>

75% of the TVL of the Meta Pool is delegated by performance. Validators are chosen by having (1) an uptime >95% and APY above average, (2) fee of <10%, (3) not being over the Nakamoto Coefficient and (4) have enough tokens to accomplish seat price of NEAR protocol. You can see the stats for each validator at the [vote for validators section](https://www.metapool.app/stakevote) of [metapool.app](https://app.gitbook.com/u/kWssFwdDdAV7LwyRE3nVkm0AZm53)

</details>

<details>

<summary>How does Meta Pool delegate by votes?</summary>

The delegation by votes, depends on the voting by DAO members.

The validator performance has priority over votes, if a validator performance (APY) is below average, votes will not be applied to stake calculation.

Twice per epoch, the delegation of NEAR to each validator is calculated based on votes and performance, but the stake delegation movements are performed gradually.&#x20;

Only 1% of TVL is rebalanced every 4 epochs. If there are no natural stake/unstake movements, the assigned stake can take months to be made effective.\
\
Therefore, "Assigned by votes" indicates the delegation target of the NEAR delegated by votes for each validator.

If the automated bot only rebalances 1% every 4 epochs, it means that it takes 2 months (25x4 = 100 epochs) to rebalance the full 25% assigned by votes.&#x20;

Only if there's a natural "tide" of users staking and unstaking the rebalance can be completed faster.

</details>

<details>

<summary>Why is the allocation by votes not instantaneous?</summary>

It takes 4 epochs in order to move delegation from one validator to another (this is a limitation imposed by proof of stake), and those 4 epochs are without rewards, so the rebalance is costly. The bot rebalances only 1% of the stake every 4 epochs, so it means that it takes 2 months (25x4 = 100 epochs) to rebalance the full 25% assigned by votes.&#x20;

</details>

<details>

<summary>Why not rebalancing more than 1% every 4 epochs?</summary>

To move NEAR tokens from one validator to another takes 4 epochs, and during that period rewards are not generated.

Moving 1% does not significantly affect APY. On the other hand, if let's say 15% were unstaked and restaked every 4 epochs, it would greatly affect stNEAR's APY on each redistribution, greatly affecting stNEAR APY.

</details>

<details>

<summary>What does “Assigned by Votes” means?</summary>

The “Assigned by votes” shows the NEAR tokens that would be staked if nothing changes during the next 100 epochs.

Considering that the TVL changes constantly and validators performance also changes, the delegation strategy is constantly chasing the “Assigned by Votes” number.

</details>

<details>

<summary>What is “Assigned Total”?</summary>

This number represents the sum of the NEAR tokens to be assigned by performance (75%) and by votes (25%).&#x20;

</details>

<details>

<summary>What is an epoch?</summary>

An epoch in the NEAR protocol is the interval of time that consists of several consensus rounds. Note that there is no guarantee of the exact number of consensus rounds. Currently, one epoch lasts between 13 and 16 hours and is used to:

* measure the performance and uptime of validators;
* collect the bids from new validators.

An epoch lasts 43.200 blocks and a block lasts approx. 1.1 seconds.

</details>

<details>

<summary>Where can I see more information of the NEAR Protocol network and Validators info?</summary>

You can see the stats for each validator at the [vote for validators section](https://www.metapool.app/stakevote) of [metapool.app](https://app.gitbook.com/u/kWssFwdDdAV7LwyRE3nVkm0AZm53), and also the [NEAR blockchain explorer](https://nearblocks.io/node-explorer) provides information about validators, such as current seat price, the validator’s uptime and fee, account and transaction details, etc.

</details>
