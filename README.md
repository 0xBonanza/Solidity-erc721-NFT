<h1>General</h1>
<p>This repo can be used to create ERC-721 tokens, upload the artworks on IPFS and list them on a customized marketplace.&nbsp;</p>
<h1>Contracts</h1>
<h2>ShelterCollectible.sol</h2>
<p>This contract is used to mint ERC-721 tokens. For our use case, the tokens are minted directly to the Marketplace (not to the user!), hence can only be called by the admin of the contract.</p>
<h2>ShelterMarketplace.sol</h2>
<p>This contract is used as an adoption platform for the ERC-721 tokens.&nbsp;</p>
<h1>Dependencies</h1>
<p>This contract mostly depends on the <strong>ERC20.sol</strong> contract from OpenZeppelin.</p>
<h1>.env file</h1>
<p>Make sure you have a <strong>.env</strong> file in your working directory containing:</p>
<ul>
<li>export PRIVATE_KEY="<em>YOUR_KEY</em>"</li>
<li>export WEB3_INFURA_PROJECT_ID="<em>YOUR_INFURA_ID</em>"</li>
<li>export ETHERSCAN_TOKEN="<em>YOUR_ETHERSCAN_TOKEN</em>"</li>
</ul>
<p><em>NB</em>: the&nbsp;ETHERSCAN_TOKEN is only needed if you want your contract to be verified upon deployment.&nbsp;</p>
<h1>Deployment</h1>
<p>The contracts have been deployed successfully on Kovan test network at the following addresses:</p>
<ul>
<li>Collectible:&nbsp;0x2f6b3F8e9b5a95D7cfc46F877e372eb266Ad1e14</li>
<li>Marketplace: 0x92B50E5d85cD6c52e3Fb5084092f50B6D678D05B</li>
</ul>
<h1>How to use?</h1>
<p dir="auto">This contract has been created by using Python and Brownie. So you should consider using both these tools to reproduce the exact result.</p>