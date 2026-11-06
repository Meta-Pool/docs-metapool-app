---
title: Validator Selection
description: Learn more about Meta Pool Principles of management
---

Meta Pool follows the **NEAR Foundation strategy** to spread the stake among the long tail of high-performance, lo&#x77;**-**&#x63;ommission, non-concentrated validators, in order to increase decentralization and censorship resistance for NEAR.&#x20;

We evaluate **all validators**, in our main product we do not have whitelists, and we publish the formula, the code we use to compute the formula and also the results that will be on chain. _The ethos is to be totally transparent and open to all validators._ =

We have **4 criteria for selecting validators** on the NEAR network, that are in line with our ethos of transparency and fairness:

1. Uptime > 95%
2. Fees < 10%
3. Making sure the validator doesn't reduce the Nakamoto Coefficient
4. Have enough tokens to accomplish the seat price of NEAR Protocol

### **How the NEAR stake is distributed?**

Every epoch, this tree stage process is executed to distribute the NEAR available to stake:

1. **Stake:** if people stake NEAR during the epoch, the NEAR is distributed with this procedure:
   1. We create a list of top 50 validators **by performance** ( average APY for the last 5 epochs)&#x20;
   2. We create a list of most voted validators (with more than 5% of votes)&#x20;
   3. We merge both lists and start going thru the list staking if the following conditions are met:&#x20;
      1. The validator has more assigned NEAR (performance+votes) than staked NEAR&#x20;
      2. The validator APY is in the top 50 performant validators&#x20;
      3. The validator comission is <= 8%&#x20;
      4. The validator has received less than 20K NEAR this epoch&#x20;
      5. If all the conditions are met, the validator is staked with a cap of 20K NEAR per epoch, and never more NEAR than currently assigned (performance+votes)
2. **Unstake**: If some validator goes offline for several epochs, it will be fully unstaked, and after 4 epochs, the above procedure applies to distribute the stake
3. **Rebalance**: Every 4 epochs, at most 0.15% of all the stake is unstaked from the worst performant validators with more staked than assigned. After the unstaking delay, that 0.15% goes to the procdure 1) to be distributed. This rebalancing process has a cost so it must be limited in the amount, because we don't receive rewards for that 0.15% being rebalanced during the 4 epoch delay for unstaking.

**Note:** The data, performance, votes, NEAR assigned, can be viewed in real-time here: [www.metapool.app/stakevote](https://www.metapool.app/stakevote)

**Note 2:** You can verify the actual list of Meta Pool staked validators using this [3rd party site](https://near-overview.genesislab.net/validators) by entering **meta-pool.near** in the account filter
