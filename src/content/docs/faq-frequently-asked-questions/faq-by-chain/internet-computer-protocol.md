---
title: Internet Computer Protocol
---

<details>

<summary>What is Meta Pool liquid staking on ICP?</summary>

Meta Pool provides liquid staking for ICP (historically known as StakedICP). It lets users stake their ICP - without locking assets or maintaining infrastructure - whilst participating in on-chain activities, e.g. lending.

</details>

<details>

<summary>How does Meta Pool stICP work?</summary>

When staking with Meta Pool on ICP, users receive stICP tokens representing their staked ICP and earned maturity. stICP balances can be used like regular ICP to earn yields and lending rewards, and represent your staked ICP, and earned staking rewards.

`stICP:ICP ratio = (total stICP supply) / (total ICP staked + total NNS maturity earned)`

Rewards are based on the underlying NNS voting rewards, so can fluctuate based on the number of proposals (among other factors).

Since the NNS voting rewards will constantly accumulate, this means that stICP's value effectively always increases relative to ICP. The ICP/stICP exchange rate is updated approximately every 24 hours based on the NNS voting rewards earned by the staking neurons.\
Let's do a simple example as a demonstration.

Say you stake at the very beginning when 1 ICP = 1 stICP. You deposit 10 ICP and receive 10 stICP back.

After a few years, the balances in the protocol grow due to NNS voting rewards. Say 128 ICP had been staked with Meta Pool and the sum of all neuron balances on the NNS was 160 ICP. Then 1 ICP would be worth (128/160) = 0.8 stICP; conversely, 1 stICP would be worth (160/128) = 1.25 ICP.

At this point, you could unstake or trade your 10 stICP and receive 12.5 ICP in return.

This means as long as you are holding stICP, you are earning Meta Pool ICP staking rewards. You do not need to mint stICP from Meta Pool directly. For example, you can purchase stICP on an exchange; as every stICP token is exactly the same, you will automatically receive the benefits of staking just by holding the token!

In v1 of the protocol (released 2022), both the staking neurons and the canisters were controlled by the original StakedICP team directly. This allowed us to ship faster and test the product.

As of May 2023, v2 of the protocol launched. In v2, staking neurons are no longer directly controlled by the team, but are owned and controlled on-chain by the canisters themselves. Canister upgrades remain under protocol operator management (Meta Pool / the former StakedICP stack). This allows the team to upgrade the code, adding features and continuing to build.

Eventually, we would like for the protocol to be fully under community goverenance. Full DAO control is the goal.

</details>

<details>

<summary>What is liquid staking?</summary>

Liquid staking protocols allow users to earn staking rewards without locking assets or maintaining staking infrastructure. Users can stake tokens and receive tradable liquid tokens in return.

</details>

<details>

<summary>What is stICP?</summary>

stICP is a token that represents staked ICP in the Meta Pool NNS neurons. The token combines the value of the initial stake + earned staking rewards. stICP tokens are minted upon stake and burned when redeemed. stICP token’s balances do not update, but the value of stICP increases relative to ICP.

The stICP/ICP exchange rate is updated approximately every 24 hours based on the NNS voting rewards earned by the protocol neurons.

stICP tokens are a standard [ICRC-1 token](https://github.com/dfinity/ICRC-1), allowing you to earn ICP staking rewards while benefitting from e.g. yields across decentralised finance products. They do not confer any voting or governance rights.

</details>

<details>

<summary>How do I add stICP to my Bitinfinity Wallet? .</summary>

1. Open wallet
2. Click the large blue plus icon to add a token
3. Click "Custom", to add a custom token
4.  For "Token Canister ID", paste:

    ```
    qfr6e-biaaa-aaaak-qafuq-cai
    ```
5.  For "Token Standard", select:

    ```
    ICRC1
    ```
6. Click "Continue"
7. Click "Add"
8. "Staked ICP" should now appear in your plug token list, with your balance

</details>

<details>

<summary>How do I add stICP to my Plug Wallet?</summary>

1. Go to the app and open wallet
2. Click on the Manage button
3. Go to the “Enter token name”
4. Search “Staked ICP”
5. Click on the button to the right of “Staked ICP” and mark it green.

</details>

<details>

<summary>How can stICP be converted to ICP?</summary>

If you go to "Unstake" above, you can begin withdrawing your stICP. This will burn the stICP, and begin unstaking the corresponding ICP from the NNS. There can be a delay to this process.

Faster conversion via secondary markets or liquidity pools is not documented as a Meta Pool–operated feature in these docs. Check [metapool.app](https://www.metapool.app) or community channels for any available swap venues; otherwise use the standard Unstake flow.

</details>
