---
title: BlockSec audit
---

We’re happy to announce that [Meta Pool](https://metapool.app/dapp/mainnet/meta/) has been successfully audited by [BlockSec](https://www.blocksecteam.com/), one of the leading auditing firms in the blockchain space.&#x20;

The audit has been passed with only a handful of minor issues and suggestions that have since been fixed. Bellow you will find a summary of the auditing process and findings.

## **The Auditing Process**

BlockSec preliminary reports contained some issues reported belonging to Medium or Low categories. There were no High-risk issues reported at any point during the audit.

The first Low-risk issue was related to conflicts between admin account roles that were not fully considered. The issue was fixed.&#x20;

The third Low-risk issue was more a recommendation by Blocksec, where treasury\_account could not be read or modified, that issue was fixed.

Finally, there was a Middle-security issue, also again a recommendation, that noted that the admin is allowed to fail when setting the total weight of all the staking pools in a way that all pool might not add to 100%.This is only related to administrative tasks (rebalance weights).

## **Implementing Audit Results**

The Meta Pool team immediately acknowledged and got to work to address the minor issues and suggestions identified. The team has now implemented all the necessary changes and recommendations. &#x20;

If you have any doubt regarding this audit process,  please visit our [Discord](https://discord.com/invite/znPg3dsTzM) server. We will answer all questions and comments regarding the security report.

Our team will be working to hold the platform to the highest standard possible, showing transparency and respect to our users and always committed to security.

## Reports

### Security Audit for Metapool-ethereum (ETH)

[BlocksecAudit_ETH_staking.pdf](/assets/BlocksecAudit_ETH_staking.pdf)

### Audit Lockup Stake Meta Pool

[blocksec_lockup_v1.0-signed.pdf](/assets/blocksec_lockup_v1.0-signed.pdf)

### Audit staking ETH with Meta Pool on Ethereum

[blocksec_mpeth_v1.0_signed.pdf](/assets/blocksec_mpeth_v1.0_signed.pdf)

### Audit staking NEAR with Meta Pool on NEAR

[MetaPool_BlockSec_Audit_signed_v1.1.pdf](/assets/MetaPool_BlockSec_Audit_signed_v1.1.pdf)

### Audit staking wNEAR with Meta Pool on Aurora

[main_signed_blocksec_report_march2022.pdf](/assets/main_signed_blocksec_report_march2022.pdf)



### Audit for Solana **Restake Aggregator**



[tpyrced_blocksec_metapool_restaking_v1.0-signed.pdf](/assets/tpyrced_blocksec_metapool_restaking_v1.0-signed.pdf)
